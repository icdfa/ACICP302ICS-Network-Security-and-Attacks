# Practical Activities

Complete Activities 00–08 in sequence using the instructor-provided source at `labs/ot-security/student-lab-source/`. You will analyze and safely operate the supplied simulation; you do not need to build a replacement implementation. Activity 08 is the guided run of the source-code lab. Use the [Student Lab Guide](../../labs/ot-security/STUDENT_LAB_GUIDE.md) for setup and exact commands.

| Activity | Source-code lab task | Main evidence |
|---|---|---|
| [00 — Lab preflight](00-lab-preflight-and-safety.md) | Confirm access, VM isolation, snapshot and canonical source path | Safety declaration and preflight/source-commit record |
| [01 — Architecture and plant baseline](01-architecture-and-plant-baseline.md) | Inspect and run the supplied process in normal state | Annotated topology and baseline observations |
| [02 — Modbus/TCP data model](02-modbus-data-model-and-normal-operations.md) | Derive the register map from the supplied source and verify normal reads | Register table and read evidence |
| [03 — Packet visibility](03-packet-visibility-and-protocol-analysis.md) | Capture and explain normal local Modbus/TCP traffic | Learner-created PCAP/PCAPNG and analysis |
| [04 — Safe discovery](04-safe-discovery-and-exposure-mapping.md) | Inventory only documented local services and process-relevant exposure | Loopback-only inventory and risk register |
| [05 — Defensive OT guard](05-design-a-defensive-ot-guard.md) | Inspect the supplied guard, decisions, event output and limitations | Safeguard/limitations analysis |
| [06 — Controlled validation](06-controlled-security-validation.md) | Run at least three approved bounded demonstrations | Test plan and expected/observed evidence |
| [07 — Recovery and defence](07-recovery-evidence-and-project-defence.md) | Verify clean shutdown/recovery and present findings | Recovery record, report and defence notes |
| [08 — Supplied source-code lab](08-modbus-tcp-simulation-lab.md) | Execute the Ubuntu VM lab using the canonical source | Source version, screenshots/logs and cleanup proof |

The instructor may set deadlines, team size, VM allocations and any additional approved task through the ICDFA E-Campus. Safety requirements in this repository always apply. The directory `labs/ot-security/archive-original/` is archival only and must not be executed.
