# ACICP302ICS - Network Security & Attacks

## Source-Code-Guided Practical Laboratory

This course uses the **instructor-provided OT simulation source code** as the lab environment. Learners inspect, run, observe, test and explain the supplied code; they are **not required to build a replacement simulator or write a guard from scratch**.

> **Start here:** Use only [`labs/ot-security/student-lab-source/`](labs/ot-security/student-lab-source/) and follow the [Student Lab Guide](labs/ot-security/STUDENT_LAB_GUIDE.md). Do not run files under [`labs/ot-security/archive-original/`](labs/ot-security/archive-original/); that is an archival copy, not the student lab.

The canonical student source is the loopback-only course copy. It is intended to run inside the assigned Ubuntu virtual machine and uses `127.0.0.1`. The archived source came from an earlier project bundle and contains unsafe network defaults; it is retained only for reference and must not be executed.

## How the course works

Learners use the same supplied source code to examine the simulated process, map the Modbus/TCP data model, establish a normal baseline, capture and interpret traffic, assess only the local simulated services, inspect the defensive guard, run the bounded demonstrations and verify recovery. The assessed work is each learner/team’s **own observations, analysis, test records, evidence and report**.

| Activity | Focus | Main evidence |
|---|---|---|
| [00 — Lab preflight and safety](docs/activities/00-lab-preflight-and-safety.md) | Access, VM isolation, snapshots and source verification | Safety declaration, source path/commit and preflight record |
| [01 — Architecture and plant baseline](docs/activities/01-architecture-and-plant-baseline.md) | Understand the supplied plant, guard and dashboards | Annotated architecture and normal-state observations |
| [02 — Modbus/TCP data model](docs/activities/02-modbus-data-model-and-normal-operations.md) | Read the supplied register/data model | Register map and normal-read evidence |
| [03 — Packet visibility](docs/activities/03-packet-visibility-and-protocol-analysis.md) | Capture and explain normal local traffic | Learner-created PCAP/PCAPNG and packet analysis |
| [04 — Safe discovery](docs/activities/04-safe-discovery-and-exposure-mapping.md) | Map only the lab’s documented loopback services | Local service inventory and risk register |
| [05 — Defensive OT guard](docs/activities/05-design-a-defensive-ot-guard.md) | Inspect and evaluate the supplied guard | Safeguard/limitations analysis and event evidence |
| [06 — Controlled validation](docs/activities/06-controlled-security-validation.md) | Run only the supplied bounded demonstrations | Approved test plan and expected/observed comparison |
| [07 — Recovery and defence](docs/activities/07-recovery-evidence-and-project-defence.md) | Stop processes, verify recovery and present findings | Recovery proof, report and demonstration |
| [08 — Supplied source-code lab](docs/activities/08-modbus-tcp-simulation-lab.md) | Complete the Ubuntu VM run of the supplied simulation | Source-version record, screenshots, logs and cleanup proof |

## Before starting

1. Read [Course Information](COURSE_INFORMATION.md), [Assessment](ASSESSMENT.md), and [Security and Safety Rules](SECURITY_AND_SAFETY.md).
2. Read the [Practical Lab Challenge](PROJECT_CHALLENGE.md) and [reference architecture](docs/reference-architecture.md).
3. Obtain access to this private repository, or ask the instructor for the approved course archive.
4. Follow the [Student Lab Guide](labs/ot-security/STUDENT_LAB_GUIDE.md) to prepare the assigned Ubuntu VM and verify the canonical source path.
5. Keep an evidence log from Activity 00. Record the course-source commit used for your work.

## What learners submit

Do not modify or submit the course repository as if it were your own implementation. Submit your own private learner/team evidence repository or approved workspace containing the evidence log, annotated diagrams, register map, capture and packet analysis, local exposure record, risk register, test plan, screenshots/log references, final report and defence notes. Cite the supplied course source and identify its commit. Code changes are not required unless an instructor separately authorizes a specific extension.

Use the documents in [`docs/templates/`](docs/templates/) and review the [integrated rubric](docs/rubrics/integrated-ot-testbed-rubric.md). The reference repository is private; the instructor must grant learners access or provide the approved archive through the LMS.

## Safety boundary

Run the student source only in the assigned, isolated Ubuntu VM. The canonical copy is configured for loopback (`127.0.0.1`). Do not use bridged networking, port forwarding, real industrial devices, campus/home/public networks or any other host. If the address/bind check fails or a script proposes a non-loopback target, stop and contact the instructor.
