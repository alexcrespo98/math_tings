"""
Peltier Power Analysis — Single Interactive Graph
==================================================
One graph comparing:
  - Horizontal line: 10mm square Peltier with direct water contact
  - Three curves vs. metal block thickness:
      Copper (400 W/m·K)
      Lead-free brass (109 W/m·K)
      Conductive plastic (20 W/m·K)

Sliders for hot water temperature and block width.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox, Slider

# ──────────────────────────────────────────────────────────────────────
# Water properties at ~30°C
# ──────────────────────────────────────────────────────────────────────
RHO_W  = 994.0
MU_W   = 0.72e-3
K_W    = 0.623
PR_W   = 4.8
NU_W   = MU_W / RHO_W

# ──────────────────────────────────────────────────────────────────────
# Constants
# ──────────────────────────────────────────────────────────────────────
T_COLD       = 10.0      # °C  cold water (≈50°F), fixed
T_AMB        = 25.0      # °C  ambient air
PELTIER_SIDE = 0.010     # m   10mm square
FLOW         = 1.0       # m/s
H_AIR        = 10.0      # W/(m²·K)
S            = 0.029     # V/K
R_I          = 2.5       # Ω
K_PASTE      = 4.0       # W/(m·K)
D_PASTE      = 0.0001    # m
K_P          = 1.5       # W/(m·K)
D_P          = 0.003     # m

MATERIALS = [
    ('Copper (400 W/m·K)',          400, '#B87333', '-',  2.8),
    ('Lead-free brass (109 W/m·K)', 109, '#C9B037', '--', 2.8),
    ('Conductive plastic (20 W/m·K)', 20, '#2E8B57', ':', 2.8),
]

# ──────────────────────────────────────────────────────────────────────
# Defaults
# ──────────────────────────────────────────────────────────────────────
DEFAULT_T_HOT     = 60.0    # °C
DEFAULT_CUBE_SIDE = 10.0    # mm

state = dict(T_hot=DEFAULT_T_HOT, cube_side_mm=DEFAULT_CUBE_SIDE)

# ──────────────────────────────────────────────────────────────────────
# X-axis (generous, trimmed at draw time)
# ──────────────────────────────────────────────────────────────────────
A_MM_MAX   = 500
a_mm_full  = np.linspace(0.5, A_MM_MAX, 2000)
a_m_full   = a_mm_full / 1000

# ──────────────────────────────────────────────────────────────────────
# Physics
# ──────────────────────────────────────────────────────────────────────
def h_flat_plate(v, L):
    Re = v * L / NU_W
    if Re > 5e5:
        Nu = 0.037 * Re**0.8 * PR_W**(1/3)
    else:
        Nu = 0.664 * Re**0.5 * PR_W**(1/3)
    return Nu * K_W / L

def direct_water_power(T_hot):
    dT = T_hot - T_COLD
    h = h_flat_plate(FLOW, PELTIER_SIDE)
    r_conv = 1.0 / h
    r_pelt = D_P / K_P
    r_total = 2 * r_conv + r_pelt
    dT_pelt = dT * (r_pelt / r_total)
    return (S * dT_pelt)**2 / (4 * R_I) * 1000

def block_power(a_m, T_hot, cube_side):
    A_block = cube_side ** 2
    A_pelt  = PELTIER_SIDE ** 2
    P_perim = 4 * cube_side

    R_paste_pipe = D_PASTE / (K_PASTE * A_block)
    R_paste_pelt = D_PASTE / (K_PASTE * A_pelt)
    R_pelt       = D_P / (K_P * A_pelt)
    R_mid  = 2 * R_paste_pipe + 2 * R_paste_pelt + R_pelt
    frac_p = R_pelt / R_mid

    out = {}
    for name, k_mat, color, ls, lw in MATERIALS:
        m = np.sqrt(H_AIR * P_perim / (k_mat * A_block))
        ma = m * a_m
        cosh_ma = np.where(ma < 700, np.cosh(ma), np.exp(ma) / 2)

        T_hot_tip  = T_AMB + (T_hot  - T_AMB) / cosh_ma
        T_cold_tip = T_AMB + (T_COLD - T_AMB) / cosh_ma

        dT_tips = T_hot_tip - T_cold_tip
        dT_pelt = np.maximum(dT_tips * frac_p, 0)
        P_mW = (S * dT_pelt)**2 / (4 * R_I) * 1000

        out[name] = dict(P_mW=P_mW, color=color, ls=ls, lw=lw)
    return out

def find_crossover(P_mW, P_water, a_mm):
    diff = P_mW - P_water
    cross_idx = np.where(np.diff(np.sign(diff)))[0]
    if len(cross_idx) > 0:
        i = cross_idx[0]
        return a_mm[i] + (a_mm[i+1]-a_mm[i]) * (-diff[i]) / (diff[i+1]-diff[i])
    return None

# ──────────────────────────────────────────────────────────────────────
# Figure
# ──────────────────────────────────────────────────────────────────────
fig = plt.figure(figsize=(11, 7.5))
fig.patch.set_facecolor('#fafafa')
fig._refs = []

ax = fig.add_axes([0.08, 0.22, 0.88, 0.68])

def draw():
    ax.clear()

    T_hot     = state['T_hot']
    cube_side = state['cube_side_mm'] / 1000
    dT        = T_hot - T_COLD

    P_water = direct_water_power(T_hot)
    bres    = block_power(a_m_full, T_hot, cube_side)

    # Find x-limit from all crossovers
    crossovers = []
    for name, mdata in bres.items():
        ac = find_crossover(mdata['P_mW'], P_water, a_mm_full)
        if ac is not None:
            crossovers.append(ac)

    if len(crossovers) > 0:
        x_max = max(crossovers) * 1.25
    else:
        x_max = A_MM_MAX
    x_max = max(min(x_max, A_MM_MAX), 20)

    mask = a_mm_full <= x_max
    a_plot = a_mm_full[mask]

    # Direct water line
    ax.axhline(P_water, color='forestgreen', linewidth=2.5, linestyle='--',
               label=f'Direct water contact ({P_water:.3f} mW)', zorder=3)

    # Material curves + crossover markers
    for name, mdata in bres.items():
        P_plot = mdata['P_mW'][mask]
        ax.plot(a_plot, P_plot, color=mdata['color'],
                linestyle=mdata['ls'], linewidth=mdata['lw'], label=name)

        ac = find_crossover(mdata['P_mW'], P_water, a_mm_full)
        if ac is not None and ac <= x_max:
            ax.plot(ac, P_water, 'o', color=mdata['color'], markersize=10,
                    zorder=5, markeredgecolor='black', markeredgewidth=1)
            ax.annotate(f'{ac:.1f} mm',
                        xy=(ac, P_water),
                        xytext=(ac + x_max * 0.03, P_water * 0.75),
                        fontsize=9, color=mdata['color'], fontweight='bold',
                        arrowprops=dict(arrowstyle='->', color=mdata['color'],
                                        lw=1.2))

    cube_label = (f"{state['cube_side_mm']:.0f}×{state['cube_side_mm']:.0f}mm block"
                  if state['cube_side_mm'] != 10
                  else "10×10mm block (= Peltier size)")

    ax.set_title(
        f"ΔT = {dT:.0f}°C  (hot {T_hot:.0f}°C − cold {T_COLD:.0f}°C)     "
        f"{cube_label}     ● = crossover",
        fontsize=12, fontweight='bold')

    ax.set_xlabel('Metal block thickness per side (mm)', fontsize=11)
    ax.set_ylabel('Power output (mW)', fontsize=11)
    ax.set_xlim(a_plot[0], x_max)
    ax.set_ylim(bottom=0)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right', fontsize=9,
              framealpha=0.9, edgecolor='gray')

    fig.canvas.draw_idle()

draw()

# ──────────────────────────────────────────────────────────────────────
# Controls
# ──────────────────────────────────────────────────────────────────────

# Hot water temperature slider
ax_temp = fig.add_axes([0.08, 0.10, 0.55, 0.03])
slider_temp = Slider(ax_temp, 'Hot water (°C)', 20.0, 100.0,
                      valinit=DEFAULT_T_HOT, valstep=1.0,
                      color='tomato')

# Block width: label + box + nudge buttons
fig.text(0.08, 0.045, 'Block width (mm):', fontsize=10,
         fontweight='bold', ha='left', va='center')

ax_box = fig.add_axes([0.24, 0.03, 0.07, 0.035])
tb_cube = TextBox(ax_box, '', initial=f'{DEFAULT_CUBE_SIDE:.0f}')

fig.text(0.315, 0.045, 'mm', fontsize=10, ha='left', va='center')

ax_dn = fig.add_axes([0.32, 0.03, 0.035, 0.035])
ax_up = fig.add_axes([0.36, 0.03, 0.035, 0.035])
btn_dn = Button(ax_dn, '−', color='#ffe0e0', hovercolor='#ffb0b0')
btn_up = Button(ax_up, '+', color='#e0ffe0', hovercolor='#b0ffb0')
btn_dn.label.set_fontsize(12)
btn_dn.label.set_fontweight('bold')
btn_up.label.set_fontsize(12)
btn_up.label.set_fontweight('bold')

# Reset button
ax_reset = fig.add_axes([0.85, 0.03, 0.08, 0.035])
btn_reset = Button(ax_reset, 'Reset', color='lightgray', hovercolor='silver')
btn_reset.label.set_fontsize(10)
btn_reset.label.set_fontweight('bold')

# Info line
info = (
    f"Peltier: 10×10mm, {D_P*1000:.0f}mm, S={S} V/K, Rᵢ={R_I}Ω  |  "
    f"Paste: {D_PASTE*1000:.1f}mm @ {K_PASTE} W/m·K  |  "
    f"Cold water: {T_COLD}°C  |  Water flow: {FLOW} m/s  |  "
    f"Ambient: {T_AMB}°C  h_air={H_AIR} W/m²·K"
)
fig.text(0.5, 0.005, info, ha='center', fontsize=7, family='monospace',
         alpha=0.45)

# ──────────────────────────────────────────────────────────────────────
# Callbacks
# ──────────────────────────────────────────────────────────────────────
def on_temp_change(val):
    state['T_hot'] = val
    draw()

slider_temp.on_changed(on_temp_change)

def update_cube(new_val):
    new_val = max(new_val, PELTIER_SIDE * 1000)
    state['cube_side_mm'] = round(new_val, 1)
    tb_cube.set_val(f"{state['cube_side_mm']:.0f}")
    draw()

def on_cube_submit(text):
    try:
        update_cube(float(text))
    except ValueError:
        tb_cube.set_val(f"{state['cube_side_mm']:.0f}")

tb_cube.on_submit(on_cube_submit)

def on_dn(event):
    update_cube(state['cube_side_mm'] - 1)

def on_up(event):
    update_cube(state['cube_side_mm'] + 1)

btn_dn.on_clicked(on_dn)
btn_up.on_clicked(on_up)

def on_reset(event):
    state['T_hot'] = DEFAULT_T_HOT
    state['cube_side_mm'] = DEFAULT_CUBE_SIDE
    slider_temp.set_val(DEFAULT_T_HOT)
    tb_cube.set_val(f"{DEFAULT_CUBE_SIDE:.0f}")
    draw()

btn_reset.on_clicked(on_reset)

fig._refs = [slider_temp, tb_cube, btn_dn, btn_up, btn_reset]

# ──────────────────────────────────────────────────────────────────────
# Console
# ──────────────────────────────────────────────────────────────────────
print("=" * 65)
print("  Peltier Power: Block on Pipe vs. Direct Water Contact")
print("=" * 65)
print("  Slide hot water temp to see ΔT effect in real time")
print("  Adjust block width to see thermal mass effect")
print("  ● = thickness where block becomes worse than water contact")
print("=" * 65)

plt.show()
