# ACICP302ICS — Network Security & Attacks

## ICDFA Practical Build Repository

This repository contains the practical activity pathway for **ACICP302ICS — Network Security & Attacks** at the International Cybersecurity and Digital Forensics Academy (ICDFA).

There are **no lecture slides** in this course. Learners build, secure, test and defend their own simulated OT Modbus/TCP environment through the practical activities below.

> **Important:** This is not a completed solution repository. Each learner or approved team must write its own code, create its own topology, gather its own evidence and submit its own report. Do not copy another learner’s work or submit a third-party implementation as your own.

## What you will build

By the end of the course, you will have an isolated OT security testbed that includes:

- A simulated process or plant with Modbus/TCP data points.
- A normal-operations dashboard or HMI view.
- A documented Modbus register map and baseline packet capture.
- A safe, controlled exposure assessment performed only on your assigned lab environment.
- A defensive control that validates, blocks or alerts on unsafe process changes.
- Audit events, recovery evidence and a professional technical report.

Read the complete [Practical Build Challenge](PROJECT_CHALLENGE.md) before beginning the first activity.

## Practical pathway

| Activity | Build outcome | Main evidence |
|---|---|---|
| [00 — Lab preflight](docs/activities/00-lab-preflight-and-safety.md) | Authorised, isolated workspace | Safety declaration and snapshot record |
| [01 — Architecture and plant baseline](docs/activities/01-architecture-and-plant-baseline.md) | Working simulated OT process | Topology diagram and normal telemetry |
| [02 — Modbus/TCP data model](docs/activities/02-modbus-data-model-and-normal-operations.md) | Register map and HMI/dashboard | Register table and working-read evidence |
| [03 — Packet visibility](docs/activities/03-packet-visibility-and-protocol-analysis.md) | Baseline capture and analysis | Labelled PCAP/PCAPNG and packet analysis |
| [04 — Safe discovery](docs/activities/04-safe-discovery-and-exposure-mapping.md) | Asset and exposure record | Scoped discovery log and risk register |
| [05 — Defensive OT guard](docs/activities/05-design-a-defensive-ot-guard.md) | Working validation/alert control | Guard design, events and validation evidence |
| [06 — Controlled security validation](docs/activities/06-controlled-security-validation.md) | Defended-versus-undefended comparison | Test plan, logs and observations |
| [07 — Recovery and defence](docs/activities/07-recovery-evidence-and-project-defence.md) | Restored environment and final defence | Recovery proof, report and live demonstration |

## Before you begin

1. Read [Course Information](COURSE_INFORMATION.md), [Safety Rules](SECURITY_AND_SAFETY.md) and [Assessment](ASSESSMENT.md).
2. Read the [Practical Build Challenge](PROJECT_CHALLENGE.md) and [reference architecture](docs/reference-architecture.md).
3. Use only the ICDFA-issued isolated VMs, lab network and clean snapshots.
4. Start with [Activity 00](docs/activities/00-lab-preflight-and-safety.md).
5. Create your personal or team project folder using the structure in [starter/README.md](starter/README.md).
6. Keep an evidence log from the first activity; do not attempt to recreate evidence at the end.

## Submission standard

Every submission must contain your own:

- Source code and a clear `README.md` explaining how it runs.
- Topology and Modbus register map.
- Labelled screenshots and packet captures.
- Evidence log, risk register, findings and recovery record.
- Final professional report using the supplied template.

Use the templates in [`docs/templates`](docs/templates) and review the [integrated rubric](docs/rubrics/integrated-ot-testbed-rubric.md) before final submission.

## Absolute boundary

All testing is limited to your own simulated system inside the authorised ICDFA isolated environment. Never use production devices, public IP addresses, campus networks, bridged adapters, unauthorised systems or real critical-infrastructure equipment.

## Repository use

This is an ICDFA academic practical repository. It intentionally contains no completed attack tooling, target details, answer keys or deployable production implementation.
