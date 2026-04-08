# math_tings

it's mafamatics love... x

A math and physics reference repo for power generation projects — starting with a Peltier thermoelectric module analysis tool and building toward micro-hydro turbine generators. All units SI.

---

## What's in here

```
peltier_power_analysis.py      ← interactive simulation script (run this!)
equations/master_equations.md  ← famous + useful equations you should know
reference/normal_conditions.md ← assumed "normal" values in SI units
turbines/README.md             ← placeholder for future turbine work
```

---

## Peltier Module Power Analysis

An interactive Python script that plots **Surface Area vs. Electrical Power Output (W)**
for a round 12 mm-diameter Peltier module with water flowing past it — either directly
or through a copper pipe of adjustable wall thickness.

### Usage

```bash
pip install matplotlib numpy
python peltier_power_analysis.py
```

Three sliders update the plot in real time:

| Slider | Variable | Range | Default | Meaning |
|--------|----------|-------|---------|---------|
| `a` | Pipe wall thickness | 0 – 0.01 m | 0.002 m | 0 = direct water contact, no copper pipe |
| `b` | Water flow speed | 0.1 – 5.0 m/s | 1.5 m/s | Higher flow → better convection |
| `c` | Temperature difference ΔT | 5 – 100 °C | 40 °C | Between hot and cold water streams |

A vertical dashed line marks the actual surface area of the 12 mm-diameter module (≈ 1.13×10⁻⁴ m²) so you can see where you'd actually be operating.

### Model (thermal resistance network)
```
R_cond  = a / (k_cu * x)
h       = 3000 * b^0.8
R_conv  = 1 / (h * x)
R_p     = d_p / (k_p * x)
R_total = 2*R_conv + 2*R_cond + R_p
D_p     = c * (R_p / R_total)
P_out   = (S * D_p)^2 / (4 * R_i)
```

**Constants used:**
- `k_cu = 400` W/(m·K) — copper (high-purity, best-case)
- `k_p = 1.5` W/(m·K) — Peltier ceramic
- `d_p = 0.003` m — Peltier thickness
- `S = 0.04` V/K — Seebeck coefficient
- `R_i = 2.5` Ω — internal resistance

---

## Equations Reference

[`equations/master_equations.md`](equations/master_equations.md) — a master list of famous and useful equations organized by category:
- Thermal conductivity & heat transfer (Fourier, Newton, Stefan-Boltzmann)
- Thermoelectrics (Seebeck, max power, Peltier coefficient)
- Fluid dynamics (Reynolds, Dittus-Boelter, Bernoulli, Darcy-Weisbach)
- Electrical fundamentals (Ohm's Law, power, Kirchhoff, Faraday, inductance)
- Electromagnetism & generators (flux, EMF, force on wire, solenoid inductance)
- Unit conversions (GPM, inches, PSI, °F, BTU, HP)

---

## Normal Conditions Reference

[`reference/normal_conditions.md`](reference/normal_conditions.md) — assumed "normal" values in SI:
- Water and air properties at ~20 °C
- Common metals (thermal conductivity, density, specific heat)
- Standard conditions (STP, NTP, atmospheric pressure, gravity)
- Common copper pipe sizes (1/2", 3/4", 1" nominal)
- Typical convective heat transfer coefficients
- Typical residential / undersink flow conditions and velocities

---

## Turbines _(future work)_

[`turbines/README.md`](turbines/README.md)

This section will cover **micro-turbine generators** for low-flow applications — specifically undersink residential water lines running at low GPM. The goal is to harvest meaningful electrical power from water flow that would otherwise go unused.

**Planned content:**
- Faraday's law and generator EMF equations
- Inductance calculations for coil design
- Magnetic flux analysis for small permanent-magnet generators
- Target application: 1–3 GPM through 3/4-inch pipe
- Power yield estimates for micro-hydro vs. Peltier approaches

Stay tuned. 🌊⚡