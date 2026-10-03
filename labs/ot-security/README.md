# Modbus/TCP ICS Security Testbed

A small lab project exploring how intrusion prevention works differently in OT (operational technology) environments compared to IT. Built as a simulated green hydrogen facility control system, with an inline "guard" process that validates every write before it reaches the plant.

**This is a lab simulation on an isolated VM. It is not a real facility, vendor product, or production system.**

## Why

Modbus/TCP — still one of the most widely deployed industrial protocols — has no built-in authentication or encryption. Any device that can reach the port can read or write any register. That's a deliberate consequence of its design (a 1979 protocol built for point-to-point serial links, later carried over TCP largely unchanged), not an oversight, but it means perimeter and inline monitoring carry more weight in OT than they typically do in IT, where you can lean on the protocol layer for some baseline security.

This project builds a minimal example of that kind of inline monitoring, then tries to break it.

## Architecture

```
Attacker ──► [undefended path]  ──► Plant (port 5020)
Attacker ──► Guard (port 5021)  ──► Plant (port 5020)
```

- **`plant.py`** — Simulates a hydrogen plant: electrolyzer temperature, tank pressure, H2 flow rate. Runs a background loop that drifts values slightly every second to mimic real sensor noise, and exposes them over Modbus/TCP.
- **`guard.py`** — Sits between an external Modbus client and the plant. Every write is checked against three layers before being forwarded:
  1. **Absolute range check** — hard reject outside physical safe limits.
  2. **Step check** — hard reject any single write that changes a value too fast.
  3. **Rolling-baseline drift check** — compares the current accepted value against the accepted value N writes ago (not just the previous write), to catch slow, incremental creep that a naive step check would miss.
- **`dashboard.py`** / **`dashboard_guarded.py`** — Two Flask dashboards, one reading the undefended plant directly, one reading through the guard, so the two can be compared side by side in real time.
- **Attack scripts** — direct injection, sustained hold, correlated false-data injection, slow drift, replay, recon scan, and DoS flood.

## Results

Ran the same attack sequence against both the undefended port and the guarded port.

**Attack: sustained pressure hold (target 95.0 bar, safe range 30.0–40.0 bar)**

| | Undefended (5020) | Guarded (5021) |
|---|---|---|
| Peak pressure observed | 95.0 bar | 39.0 bar |
| Readings outside safe range | 75/75 (100%) | 0/74 (0%) |

**Attack: correlated false data injection (temp 110.0°C / pressure 55.0 bar / flow 200.0 Nm³/h, safe ranges 60–75°C / 30–40 bar / 50–150 Nm³/h)**

| | Undefended (5020) | Guarded (5021) |
|---|---|---|
| Peak temp | 110.0°C | 74.7°C |
| Peak pressure | 55.0 bar | 39.4 bar |
| Peak flow | 200.0 Nm³/h | 150.0 Nm³/h |
| Unsafe readings (all 3 registers) | 6/6 each | 0/6 each |

## What was harder than expected: slow drift

A naive filter that only rejects large single-step changes can still be walked past — an attacker just takes many small steps, each individually under the threshold, until the cumulative change is unsafe. The fix was comparing each newly accepted value against the accepted value from a fixed number of writes earlier (a rolling baseline), rather than only comparing consecutive writes. That catches cumulative drift that a step-only check lets through.

## Limitations

- Single-register checks only — a coordinated attack that spoofs multiple correlated readings while keeping each individually within its safe range (e.g. a physically implausible but individually-legal temp/pressure/flow combination) would not be caught by this version.
- No authentication on the guard itself — it protects the plant from writes that violate physical safety bounds, but doesn't address who is allowed to write in the first place. A production system would need this as a separate layer (e.g. network segmentation, allow-listing).
- Tuned for this specific simulated process; thresholds are not general-purpose and would need re-deriving for any other process.

## Running it

```bash
python3 plant.py &
python3 guard.py &
python3 dashboard.py &          # undefended view, port 8080
python3 dashboard_guarded.py &  # guarded view, port 8081
```

Then run any of the attack scripts against port 5020 (undefended) or 5021 (through the guard) to compare.

## Stack

Python, Flask, pymodbus.
