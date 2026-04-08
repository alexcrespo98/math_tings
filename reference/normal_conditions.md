# Normal Conditions Reference

Standard "assumed normal" values for engineering calculations.
**All values in SI units** unless a common alternative is shown for convenience.

---

## Water Properties (at ~20 °C / 293 K, 1 atm)

| Property | Symbol | Value | Units |
|----------|--------|-------|-------|
| Density | ρ | 998 | kg/m³ |
| Dynamic viscosity | μ | 1.002 × 10⁻³ | Pa·s  (= kg/(m·s)) |
| Kinematic viscosity | ν | 1.004 × 10⁻⁶ | m²/s |
| Specific heat (constant pressure) | Cp | 4182 | J/(kg·K) |
| Thermal conductivity | k | 0.598 | W/(m·K) |
| Prandtl number | Pr | 7.01 | dimensionless |

---

## Air Properties (at ~20 °C / 293 K, 1 atm)

| Property | Symbol | Value | Units |
|----------|--------|-------|-------|
| Density | ρ | 1.204 | kg/m³ |
| Dynamic viscosity | μ | 1.81 × 10⁻⁵ | Pa·s |
| Kinematic viscosity | ν | 1.51 × 10⁻⁵ | m²/s |
| Specific heat (constant pressure) | Cp | 1005 | J/(kg·K) |
| Thermal conductivity | k | 0.0257 | W/(m·K) |
| Prandtl number | Pr | 0.713 | dimensionless |

---

## Common Metals — Thermal and Physical Properties (~20 °C)

| Material | Thermal Conductivity k [W/(m·K)] | Density ρ [kg/m³] | Specific Heat Cp [J/(kg·K)] |
|----------|----------------------------------|-------------------|------------------------------|
| Copper (pure) | 400 | 8960 | 385 |
| Aluminum (pure) | 237 | 2700 | 897 |
| Steel (carbon, ~1%) | 50 | 7850 | 490 |
| Stainless Steel (304) | 16 | 7900 | 500 |
| Brass (70Cu/30Zn) | 110 | 8520 | 380 |

> **Note:** Copper at 400 W/(m·K) is the best-case assumption used in this repo's Peltier analysis script.
> Real copper pipe may be slightly lower (~385 W/(m·K)) depending on purity and cold-working.

---

## Standard Conditions

| Condition | Value | Notes |
|-----------|-------|-------|
| STP (IUPAC) | 0 °C (273.15 K), 100 kPa | Standard Temperature & Pressure |
| NTP | 20 °C (293.15 K), 1 atm (101.325 kPa) | Normal Temperature & Pressure |
| Room temperature | 20–25 °C (293–298 K) | Typical lab / home assumption |
| Atmospheric pressure | 101325 Pa = 101.325 kPa = 1 atm | At sea level |
| Standard gravity | g = 9.80665 | m/s² |
| Speed of sound in air | ~343 | m/s at 20 °C |

---

## Common Copper Pipe Sizes (Nominal, Type L / Type M)

> Nominal size refers to the approximate outer diameter category, not the actual ID.
> Actual dimensions vary by pipe type (K, L, M). Values below are for **Type L** (common residential).

| Nominal Size | Outer Diameter (m) | Inner Diameter (m) | Inner Diameter (in) |
|---|---|---|---|
| 1/2 inch | 0.01588 | 0.01373 | 0.540 in |
| 3/4 inch | 0.02223 | 0.01905 | 0.750 in |
| 1 inch | 0.02858 | 0.02527 | 0.995 in |

> The **3/4 inch** pipe (ID = 0.01905 m) is the assumed pipe diameter in the Peltier analysis script.

---

## Typical Convective Heat Transfer Coefficients

| Situation | h [W/(m²·K)] |
|-----------|--------------|
| Natural convection in air | 5 – 25 |
| Forced convection in air (fan-cooled) | 25 – 250 |
| Forced convection in water (low flow) | 300 – 1000 |
| Forced convection in water (moderate flow) | 1000 – 5000 |
| Forced convection in water (high flow) | 5000 – 15000 |
| Pool boiling of water | 2500 – 35000 |
| Flow boiling of water | 5000 – 100000 |

> The Peltier analysis script uses `h = 3000 · v^0.8`, which falls in the moderate forced convection range for typical residential water flow.

---

## Typical Residential / Undersink Flow Conditions

| Parameter | Typical Range | SI Value | Notes |
|-----------|--------------|----------|-------|
| Faucet flow rate | 1.5 – 2.5 GPM | 9.5 – 15.8 × 10⁻⁵ m³/s | US standard aerator |
| Low-flow faucet | 1.0 – 1.5 GPM | 6.3 – 9.5 × 10⁻⁵ m³/s | WaterSense compliant |
| Undersink supply | 1 – 3 GPM | 6.3 – 18.9 × 10⁻⁵ m³/s | Typical supply line |
| Residential line pressure | 40 – 80 PSI | 275 – 550 kPa | At the point of use |
| Supply water temperature | 10 – 20 °C | 283 – 293 K | Varies by climate/season |

### Flow Velocity in a 3/4-inch Pipe (ID = 0.01905 m)

Cross-sectional area: A = π × (0.01905/2)² ≈ 2.850 × 10⁻⁴ m²

| Flow Rate | m³/s | Velocity v = Q/A |
|-----------|------|-----------------|
| 1 GPM | 6.31 × 10⁻⁵ m³/s | ~0.22 m/s |
| 1.5 GPM | 9.46 × 10⁻⁵ m³/s | ~0.33 m/s |
| 2 GPM | 1.26 × 10⁻⁴ m³/s | ~0.44 m/s |
| 3 GPM | 1.89 × 10⁻⁴ m³/s | ~0.66 m/s |

> These velocities are relatively low for the Dittus-Boelter correlation, which works best in turbulent flow (Re > 4000). Use as a best-effort estimate for moderate-to-turbulent conditions.
