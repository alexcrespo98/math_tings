# Turbines — Micro-Hydro Power Generation _(Future Work)_

> 🚧 This section is a placeholder. Work in progress. 🚧

---

## What This Will Be

A set of equations, models, and scripts for designing **micro-turbine generators** that harvest electrical power from low-flow residential water lines — think undersink supply lines, low-GPM faucets, and similar applications where flow is continuous but modest.

---

## Target Application

- **Pipe size:** 3/4 inch nominal (ID ≈ 0.01905 m)
- **Typical flow:** 1 – 3 GPM (≈ 6.3 – 18.9 × 10⁻⁵ m³/s)
- **Goal:** Extract meaningful DC power from water flow using a small inline generator

---

## Key Physics to Be Covered

### Faraday's Law of Induction
```
EMF = -N · dΦ/dt
```
The foundation of generator design — a changing magnetic flux induces a voltage.

### Generator EMF (rotating coil)
```
V(t) = N · B · A · ω · sin(ωt)
```
Relates the geometry (coil turns, area) and magnet strength to the output voltage at a given rotation speed.

### Magnetic Flux
```
Φ = B · A · cos(θ)
```
Links magnetic field strength, coil geometry, and orientation to the usable flux.

### Inductance of a Solenoid
```
L = μ₀ · N² · A / l
```
Used to size the coil and predict the impedance at the expected rotation frequency.

### Force on a Wire in a Magnetic Field
```
F = I · L · B · sin(θ)
```
Useful for estimating the electromagnetic braking torque (and thus the pressure drop penalty on the water line).

---

## Planned Outputs

- [ ] Estimate peak and average voltage output for a given flow rate and coil design
- [ ] Model pressure drop caused by the turbine (energy extracted from the water)
- [ ] Size the generator coil for maximum power transfer
- [ ] Compare micro-hydro yield vs. Peltier thermoelectric yield for the same water line
- [ ] Interactive script similar to `peltier_power_analysis.py`

---

## Assumptions (Preliminary)

| Parameter | Assumed Value | Notes |
|-----------|--------------|-------|
| Pipe inner diameter | 0.01905 m (3/4 in) | Standard residential supply |
| Flow rate | 1 – 3 GPM | Typical undersink |
| Magnet type | NdFeB (neodymium) | High B field, small size |
| Coil wire | Copper, AWG 28–30 | Trade-off: turns vs. resistance |
| Load | Matched (R_load = R_coil) | Max power transfer condition |

---

*See [`equations/master_equations.md`](../equations/master_equations.md) for the full electromagnetic equation reference.*
