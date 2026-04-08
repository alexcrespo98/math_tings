# Master Equations Reference

A curated list of famous and useful equations for engineering and physics,
especially useful for power generation, heat transfer, and fluid dynamics.
**All units are SI unless otherwise noted.**

---

## 1. Thermal Conductivity and Heat Transfer

### Fourier's Law of Heat Conduction
```
q = -k · (dT/dx)
```
| Variable | Description | Units |
|----------|-------------|-------|
| `q`      | Heat flux (power per unit area) | W/m² |
| `k`      | Thermal conductivity | W/(m·K) |
| `dT/dx`  | Temperature gradient | K/m |

Heat flows from hot to cold; the minus sign keeps `q` positive in the direction of flow.

---

### Newton's Law of Cooling
```
Q = h · A · ΔT
```
| Variable | Description | Units |
|----------|-------------|-------|
| `Q`      | Heat transfer rate | W |
| `h`      | Convective heat transfer coefficient | W/(m²·K) |
| `A`      | Surface area | m² |
| `ΔT`     | Temperature difference (surface − fluid) | K or °C |

---

### Thermal Resistance — Conduction
```
R = L / (k · A)
```
| Variable | Description | Units |
|----------|-------------|-------|
| `R`      | Thermal resistance | K/W |
| `L`      | Thickness of material | m |
| `k`      | Thermal conductivity | W/(m·K) |
| `A`      | Cross-sectional area | m² |

---

### Thermal Resistance — Convection
```
R = 1 / (h · A)
```
| Variable | Description | Units |
|----------|-------------|-------|
| `R`      | Thermal resistance | K/W |
| `h`      | Convective heat transfer coefficient | W/(m²·K) |
| `A`      | Surface area | m² |

---

### Resistances in Series
```
R_total = R1 + R2 + R3 + ...
```
Total thermal resistance is the sum of all individual resistances in the heat-flow path.

---

### Stefan-Boltzmann Law (Radiation)
```
q = ε · σ · T⁴
```
| Variable | Description | Units |
|----------|-------------|-------|
| `q`      | Radiated heat flux | W/m² |
| `ε`      | Emissivity (0–1) | dimensionless |
| `σ`      | Stefan-Boltzmann constant = 5.67×10⁻⁸ | W/(m²·K⁴) |
| `T`      | Absolute temperature | K |

---

## 2. Thermoelectrics (Seebeck / Peltier)

### Seebeck Voltage
```
V = S · ΔT
```
| Variable | Description | Units |
|----------|-------------|-------|
| `V`      | Open-circuit voltage generated | V |
| `S`      | Seebeck coefficient | V/K |
| `ΔT`     | Temperature difference across the module | K or °C |

---

### Maximum Power — Matched Load Condition
```
P = (S · ΔT)² / (4 · R_i)
```
| Variable | Description | Units |
|----------|-------------|-------|
| `P`      | Maximum electrical power output | W |
| `S`      | Seebeck coefficient | V/K |
| `ΔT`     | Temperature difference across the module | K or °C |
| `R_i`    | Internal electrical resistance of the module | Ω |

Maximum power is delivered when the external load resistance equals the internal resistance.

---

### Peltier Heating / Cooling
```
Q_peltier = π_coeff · I
```
where `π_coeff = S · T`

| Variable | Description | Units |
|----------|-------------|-------|
| `Q_peltier` | Heat pumped by Peltier effect | W |
| `π_coeff`   | Peltier coefficient | V (or W/A) |
| `S`         | Seebeck coefficient | V/K |
| `T`         | Absolute temperature at the junction | K |
| `I`         | Current through the module | A |

---

## 3. Fluid Dynamics

### Reynolds Number
```
Re = ρ · v · D / μ
```
| Variable | Description | Units |
|----------|-------------|-------|
| `Re`     | Reynolds number (dimensionless) | — |
| `ρ`      | Fluid density | kg/m³ |
| `v`      | Flow velocity | m/s |
| `D`      | Characteristic length (e.g., pipe diameter) | m |
| `μ`      | Dynamic viscosity | Pa·s = kg/(m·s) |

- `Re < 2300` → laminar flow
- `Re > 4000` → turbulent flow
- Between 2300–4000 → transitional

---

### Dittus-Boelter Correlation (Turbulent Convection in a Pipe)
```
Nu = 0.023 · Re^0.8 · Pr^n
```
where `n = 0.4` for heating, `n = 0.3` for cooling

| Variable | Description | Units |
|----------|-------------|-------|
| `Nu`     | Nusselt number = h·D/k | dimensionless |
| `Re`     | Reynolds number | dimensionless |
| `Pr`     | Prandtl number = μ·Cp/k | dimensionless |
| `h`      | Convective heat transfer coefficient | W/(m²·K) |
| `D`      | Pipe diameter | m |
| `k`      | Fluid thermal conductivity | W/(m·K) |

---

### Bernoulli's Equation
```
P + 0.5 · ρ · v² + ρ · g · h = constant
```
| Variable | Description | Units |
|----------|-------------|-------|
| `P`      | Static pressure | Pa |
| `ρ`      | Fluid density | kg/m³ |
| `v`      | Flow velocity | m/s |
| `g`      | Gravitational acceleration (9.81) | m/s² |
| `h`      | Elevation | m |

---

### Volumetric Flow Rate
```
Q = A · v
```
| Variable | Description | Units |
|----------|-------------|-------|
| `Q`      | Volumetric flow rate | m³/s |
| `A`      | Cross-sectional area of flow | m² |
| `v`      | Flow velocity | m/s |

---

### Pressure Drop — Darcy-Weisbach
```
ΔP = f · (L/D) · 0.5 · ρ · v²
```
| Variable | Description | Units |
|----------|-------------|-------|
| `ΔP`     | Pressure drop | Pa |
| `f`      | Darcy friction factor (dimensionless) | — |
| `L`      | Pipe length | m |
| `D`      | Pipe inner diameter | m |
| `ρ`      | Fluid density | kg/m³ |
| `v`      | Flow velocity | m/s |

---

## 4. Electrical Fundamentals

### Ohm's Law
```
V = I · R
```
| Variable | Description | Units |
|----------|-------------|-------|
| `V`      | Voltage | V |
| `I`      | Current | A |
| `R`      | Resistance | Ω |

---

### Electrical Power
```
P = V · I = I² · R = V² / R
```
| Variable | Description | Units |
|----------|-------------|-------|
| `P`      | Power | W |
| `V`      | Voltage | V |
| `I`      | Current | A |
| `R`      | Resistance | Ω |

---

### Kirchhoff's Laws
**Kirchhoff's Voltage Law (KVL):** The sum of all voltages around any closed loop is zero.
```
ΣV = 0
```
**Kirchhoff's Current Law (KCL):** The sum of all currents entering a node equals the sum leaving.
```
ΣI_in = ΣI_out
```

---

### Faraday's Law of Induction
```
EMF = -N · dΦ/dt
```
| Variable | Description | Units |
|----------|-------------|-------|
| `EMF`    | Induced electromotive force | V |
| `N`      | Number of turns in the coil | dimensionless |
| `Φ`      | Magnetic flux | Wb = V·s |
| `t`      | Time | s |

---

### Inductance Voltage
```
V = L · dI/dt
```
| Variable | Description | Units |
|----------|-------------|-------|
| `V`      | Voltage across the inductor | V |
| `L`      | Inductance | H (Henry) |
| `I`      | Current | A |
| `t`      | Time | s |

---

## 5. Electromagnetism and Generators

### Magnetic Flux
```
Φ = B · A · cos(θ)
```
| Variable | Description | Units |
|----------|-------------|-------|
| `Φ`      | Magnetic flux | Wb (Weber) |
| `B`      | Magnetic flux density | T (Tesla) |
| `A`      | Area of the coil | m² |
| `θ`      | Angle between B and the normal to A | rad |

---

### Generator EMF (Rotating Coil)
```
V(t) = N · B · A · ω · sin(ωt)
```
| Variable | Description | Units |
|----------|-------------|-------|
| `V(t)`   | Instantaneous induced voltage | V |
| `N`      | Number of turns | dimensionless |
| `B`      | Magnetic flux density | T |
| `A`      | Coil area | m² |
| `ω`      | Angular velocity | rad/s |
| `t`      | Time | s |

Peak EMF: `V_peak = N · B · A · ω`

---

### Force on a Current-Carrying Wire in a Magnetic Field
```
F = I · L × B
```
(magnitude: `F = I · L · B · sin(θ)`)

| Variable | Description | Units |
|----------|-------------|-------|
| `F`      | Force on wire | N |
| `I`      | Current | A |
| `L`      | Length of wire in the field | m |
| `B`      | Magnetic flux density | T |
| `θ`      | Angle between wire and B | rad |

---

### Inductance of a Solenoid
```
L = μ₀ · N² · A / l
```
| Variable | Description | Units |
|----------|-------------|-------|
| `L`      | Inductance | H |
| `μ₀`     | Permeability of free space = 4π×10⁻⁷ ≈ 1.2566×10⁻⁶ | H/m |
| `N`      | Number of turns | dimensionless |
| `A`      | Cross-sectional area of the solenoid | m² |
| `l`      | Length of the solenoid | m |

---

## 6. Unit Conversions

| Quantity | From | To | Factor |
|----------|------|----|--------|
| Flow rate | 1 GPM (US gallon/min) | m³/s | × 6.309×10⁻⁵ |
| Flow rate | 1 GPM | L/min | × 3.785 |
| Length | 1 inch | m | × 0.0254 |
| Length | 1 foot | m | × 0.3048 |
| Pressure | 1 PSI | Pa | × 6894.76 |
| Pressure | 1 atm | Pa | = 101325 |
| Temperature | °F → °C | | (°F − 32) × 5/9 |
| Temperature | °C → K | | °C + 273.15 |
| Energy | 1 BTU | J | × 1055.06 |
| Power | 1 HP (mechanical) | W | × 745.7 |
| Power | 1 BTU/hr | W | × 0.29307 |
| Volume | 1 US gallon | L | × 3.78541 |
| Volume | 1 US gallon | m³ | × 3.78541×10⁻³ |
