"""
Peltier Power Analysis Tool
============================
Interactive plot: Surface Area (m²) vs Electrical Power Output (W)
for a round 12mm-diameter Peltier module with water flowing past it,
either directly or through a copper pipe of adjustable wall thickness.

All units are SI.

Assumptions / Model Summary
----------------------------
- Round Peltier module: 12 mm diameter  →  actual area ≈ π*(0.006)² ≈ 1.13e-4 m²
- Thermal resistance network (both the hot-side and cold-side resistances are
  assumed identical and symmetric):
    R_total = 2*R_conv + 2*R_cond + R_p
- Convection coefficient (simplified Dittus-Boelter-like):
    h = 3000 * b**0.8   [W/(m²·K)]
- Pipe diameter assumed 3/4 inch (0.01905 m) for flow reference
- Max electrical power at matched-load condition:
    P = (S * ΔT_peltier)² / (4 * R_i)

Sliders
-------
  a  Copper pipe wall thickness (m),  0 → 0.01   default 0.002
       a = 0 means direct water contact (no pipe)
  b  Water flow speed (m/s),          0.1 → 5.0  default 1.5
  c  Temperature difference ΔT (°C), 5 → 100    default 40

Constants
---------
  k_cu = 400   W/(m·K)   – copper thermal conductivity (high purity, best case)
  k_p  = 1.5   W/(m·K)   – Peltier module thermal conductivity
  d_p  = 0.003 m          – Peltier thickness (3 mm)
  S    = 0.04  V/K        – Seebeck coefficient
  R_i  = 2.5   Ω          – internal electrical resistance
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
k_cu = 400      # W/(m·K)  — copper thermal conductivity (high purity)
k_p  = 1.5      # W/(m·K)  — Peltier module thermal conductivity
d_p  = 0.003    # m         — Peltier ceramic thickness
S    = 0.04     # V/K       — Seebeck coefficient
R_i  = 2.5      # Ω         — internal electrical resistance

# Reference surface area of the 12 mm-diameter round module
r_module = 0.006                     # radius = 6 mm
A_module = np.pi * r_module**2       # ≈ 1.131e-4 m²

# ---------------------------------------------------------------------------
# Slider defaults
# ---------------------------------------------------------------------------
a_default = 0.002   # m  — copper wall thickness
b_default = 1.5     # m/s — flow speed
c_default = 40.0    # °C  — ΔT

# ---------------------------------------------------------------------------
# Surface-area sweep (x-axis)
# ---------------------------------------------------------------------------
x = np.linspace(1e-4, 0.02, 500)    # m²  (0.0001 → 0.02)

# ---------------------------------------------------------------------------
# Core calculation function
# ---------------------------------------------------------------------------
def compute_power(x, a, b, c):
    """
    Given:
        x  – surface area array (m²)
        a  – copper pipe wall thickness (m);  0 = direct contact
        b  – water flow speed (m/s)
        c  – bulk ΔT (°C) between hot and cold water streams

    Returns:
        y  – electrical power output array (W)
    """
    # Conduction resistance through copper pipe wall [K/W]
    # Edge case: a=0 → direct contact → R_cond = 0 (no copper layer)
    if a == 0:
        R_cond = np.zeros_like(x)
    else:
        R_cond = a / (k_cu * x)

    # Convective heat transfer coefficient [W/(m²·K)] — simplified correlation
    h = 3000 * b**0.8

    # Convection thermal resistance [K/W]
    R_conv = 1 / (h * x)

    # Peltier ceramic conduction resistance [K/W]
    R_p = d_p / (k_p * x)

    # Total thermal resistance (both sides: convection + conduction + Peltier)
    R_total = 2 * R_conv + 2 * R_cond + R_p

    # Temperature difference actually across the Peltier module [K]
    D_p = c * (R_p / R_total)

    # Max electrical power at matched-load condition [W]
    y = (S * D_p)**2 / (4 * R_i)

    return y

# ---------------------------------------------------------------------------
# Console summary of assumptions
# ---------------------------------------------------------------------------
print("=" * 60)
print("  Peltier Power Analysis — Assumptions & Model Summary")
print("=" * 60)
print(f"  Module diameter : 12 mm  (radius = 6 mm)")
print(f"  Module area     : {A_module:.4e} m²")
print(f"  Peltier thickness (d_p) : {d_p*1000:.1f} mm")
print(f"  Seebeck coeff   (S)     : {S} V/K")
print(f"  Internal resist (R_i)   : {R_i} Ω")
print(f"  Copper k (k_cu) : {k_cu} W/(m·K)  [high-purity, best-case]")
print(f"  Peltier k (k_p) : {k_p} W/(m·K)")
print(f"  Pipe diameter   : 3/4 inch (0.01905 m)  [flow ref only]")
print()
print("  Thermal model:  R_total = 2·R_conv + 2·R_cond + R_p")
print("  Convection:     h = 3000 · b^0.8  [simplified Dittus-Boelter]")
print("  Power:          P = (S·ΔT_peltier)² / (4·R_i)  [matched load]")
print()
print("  Sliders:  a = pipe wall thickness (0 = direct contact)")
print("            b = water flow speed")
print("            c = bulk temperature difference ΔT")
print("=" * 60)

# ---------------------------------------------------------------------------
# Build the initial figure
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6))
plt.subplots_adjust(left=0.10, bottom=0.32, right=0.97, top=0.88)

y_init = compute_power(x, a_default, b_default, c_default)
[line] = ax.plot(x, y_init, color="steelblue", linewidth=2)

# Vertical dashed reference line at the actual module area
ax.axvline(A_module, color="tomato", linestyle="--", linewidth=1.4,
           label=f"12 mm module  (A ≈ {A_module:.2e} m²)")
ax.legend(loc="upper left", fontsize=9)

ax.set_xlabel("Surface Area (m²)", fontsize=12)
ax.set_ylabel("Power Output (W)", fontsize=12)
ax.set_xlim(x[0], x[-1])
ax.set_ylim(bottom=0)
ax.grid(True, alpha=0.3)

def make_title(a, b, c):
    contact = "direct contact" if a == 0 else f"wall = {a*1000:.2f} mm"
    return (f"Peltier Power Output   |   "
            f"{contact},  flow = {b:.2f} m/s,  ΔT = {c:.0f} °C")

ax.set_title(make_title(a_default, b_default, c_default), fontsize=11)

# ---------------------------------------------------------------------------
# Sliders
# ---------------------------------------------------------------------------
ax_slider_a = plt.axes([0.12, 0.20, 0.76, 0.03])
ax_slider_b = plt.axes([0.12, 0.13, 0.76, 0.03])
ax_slider_c = plt.axes([0.12, 0.06, 0.76, 0.03])

slider_a = widgets.Slider(ax_slider_a, "a  wall (m)",  0.0,  0.01,  valinit=a_default, valstep=0.0001)
slider_b = widgets.Slider(ax_slider_b, "b  flow (m/s)", 0.1,  5.0,  valinit=b_default)
slider_c = widgets.Slider(ax_slider_c, "c  ΔT (°C)",    5.0, 100.0, valinit=c_default)

# ---------------------------------------------------------------------------
# Update callback
# ---------------------------------------------------------------------------
def update(_):
    a = slider_a.val
    b = slider_b.val
    c = slider_c.val

    y_new = compute_power(x, a, b, c)
    line.set_ydata(y_new)

    # Rescale y-axis to fit new data
    ax.set_ylim(0, max(y_new.max() * 1.15, 1e-6))

    ax.set_title(make_title(a, b, c), fontsize=11)
    fig.canvas.draw_idle()

slider_a.on_changed(update)
slider_b.on_changed(update)
slider_c.on_changed(update)

plt.show()
