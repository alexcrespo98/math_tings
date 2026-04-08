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

An interactive Python tool that answers a practical question: **how thick can a metal block be between a water pipe and a Peltier module before you lose meaningful power compared to submerging the Peltier directly in the water?**

### The short answer

There is a **lot** of margin. A Peltier module mounted on a copper or brass housing that contacts a hot/cold water pipe **outperforms** direct water contact up to a surprisingly large block thickness — because an isothermal pipe surface delivers heat more efficiently than a convection boundary layer on a tiny flat Peltier face.

### What the tool does

A single interactive graph plots **power output (mW) vs. metal block thickness (mm)** for three materials:

| Material | Thermal conductivity | Line style |
|----------|---------------------|------------|
| Copper (C110) | 400 W/(m·K) | Solid |
| Lead-free brass | 109 W/(m·K) | Dashed |
| Conductive plastic | 20 W/(m·K) | Dotted |

A horizontal green dashed line shows the **direct water contact baseline** — a 10mm square Peltier with both faces submerged in flowing water (no block, no paste, just water-on-ceramic convection).

**● markers** on the graph show the exact **crossover thickness** where each material drops to match direct water contact performance.

### Usage

```bash
pip install matplotlib numpy
python peltier_power_analysis.py
```

**Controls:**
| Control | What it does |
|---------|-------------|
| Hot water slider | Drag to change hot water temperature (20–100°C) in real time |
| Block width +/− | Increase block cross-section (wider = more thermal mass = better fin efficiency) |
| Reset button | Snap everything back to defaults |

The x-axis auto-scales so all three crossover points are visible.

### Thermal model

**Direct water contact (baseline):**
```
water → flat-plate convection boundary layer → Peltier face
Nu = 0.664·Re^0.5·Pr^(1/3)   (laminar flat plate)
```

**Block on isothermal pipe:**
```
pipe surface (T_water) → paste → metal block (fin, sides lose heat to ambient) → paste → Peltier
Fin model: T_tip = T_amb + (T_base − T_amb) / cosh(m·a)
where m = sqrt(h_air · P / (k · Ac))
```

**Power at matched load:**
```
P = (S · ΔT_peltier)² / (4 · R_i)
```

### Constants (calibrated from experiment)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Seebeck coefficient S | 0.029 V/K | Calibrated from 12mm module experiment |
| Internal resistance R_i | 2.5 Ω | |
| Peltier ceramic k | 1.5 W/(m·K) | |
| Peltier thickness | 3 mm | |
| Thermal paste k | 4.0 W/(m·K) | 0.1 mm per layer |
| Cold water temp | 10°C (≈50°F) | Fixed |
| Ambient air | 25°C, h=10 W/(m²·K) | Natural convection on block sides |
| Water flow speed | 1.0 m/s | For direct-contact convection calc |

**Experimental calibration point:** 12mm round module, direct solid contact (ice + hot steel), ΔT ≈ 130°F (54.4°C) → measured 62.5 mW.

### Key findings and design implications

1. **Direct water contact is NOT the best case.** An isothermal pipe surface (kept at T_water by continuous flow) delivers heat with zero convection resistance. Direct water contact on a tiny flat Peltier face has a significant convection boundary layer bottleneck. A metal block on a pipe **starts better** and only degrades as the block gets thick enough for fin losses to matter.

2. **Copper blocks can be very thick.** At default settings (60°C hot, 10°C cold), a 10×10mm copper block can be 15–20+ mm thick per side before it matches direct water contact performance. For brass (like the Watts LFUSG mixing valve body at ~109 W/m·K), the margin is still many millimeters.

3. **Block width matters.** A wider block (larger cross-section than the Peltier) has a lower perimeter-to-area ratio, meaning less heat leaks from the sides to ambient. Increasing block width from 10mm to 20–30mm dramatically extends the usable thickness range.

4. **Mounting on the valve body works.** The Watts LFUSG mixing valve is lead-free brass (~109 W/m·K). Embedding or mounting a Peltier on the outside of this valve body with thermal paste gives performance comparable to (or better than) trying to submerge the Peltier in the water stream directly — with a much simpler, more practical mechanical design.

5. **Outside the insert is better than inside.** Placing the Peltier inside the mixing valve insert (where it contacts mixed water in a low-flow eddy) is worse than placing it on the outside of the hot and cold pipe sections:
   - Inside the insert: limited to ~12mm round, poor water turnover in the cavity, low-conductivity insert material, and the ΔT is the *mixed* temperature difference (smaller).
   - Outside on the pipes: no size limitation, can use larger square modules, access to full boiler-vs-cold ΔT (larger), and the copper/brass housing provides excellent thermal coupling.
   - **Exception:** if the Peltier inside the insert is being used to *monitor temperature* (as part of CrossSense-style measurement), then it makes sense to keep it there — but for pure power harvesting, outside is better.

6. **The model assumes ideal flow past the block.** In reality, the water inside the pipe creates eddies and recirculation zones. The Peltier-side isn't seeing a uniform laminar flow — it's sitting in a pocket where water molecules don't refresh as quickly. This could make direct water contact *worse* than the model predicts (helping the case for metal blocks on pipes even more), or could create local hot/cold spots. More experimentation needed.

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

This section will cover **micro-turbine generators** for low-flow applications — specifically undersink residential water lines running at low GPM. The goal is to harvest meaningful electrical power from everyday water usage.

**Planned content:**
- Faraday's law and generator EMF equations
- Inductance calculations for coil design
- Magnetic flux analysis for small permanent-magnet generators
- Target application: 1–3 GPM through 3/4-inch pipe
- Power yield estimates for micro-hydro vs. Peltier approaches

Stay tuned. 🌊⚡