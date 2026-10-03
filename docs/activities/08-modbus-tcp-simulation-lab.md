# Activity 08 — Local Modbus/TCP OT Security Simulation

## Purpose

Use the local simulated plant to compare direct Modbus/TCP writes with a simple guarded path. This activity reinforces register mapping, safe test planning, detection evidence, and critical-infrastructure security principles without interacting with real equipment.

## Authorization boundary

Students should run this activity in their own Ubuntu guest VM using VMware or VirtualBox. The original project files target `192.168.2.139` and bind to `0.0.0.0`; **do not run those original scripts**. Use only the separate `local-linux/` copy, which is configured for `127.0.0.1`. Avoid bridged networking and port forwarding; disconnect the VM network adapter during the lab run. The provided student guide gives setup instructions and official hypervisor networking references. All work remains inside the student's authorized VM and simulated environment.

## Learning outcomes

Learners will:

- Start a simulated Modbus/TCP process and identify its holding-register map.
- Compare direct and guarded telemetry using two local dashboards.
- Observe bounded examples of range, step, and rolling-baseline checks.
- Collect and interpret evidence without overstating what a small lab guard can guarantee.
- Explain why authorization, isolation, segmentation, monitoring, and operational review matter in critical-infrastructure security.

## Required preparation

1. Complete [Activity 00 — Lab preflight and safety](00-lab-preflight-and-safety.md).
2. Review [`SECURITY_AND_SAFETY.md`](../../SECURITY_AND_SAFETY.md), the assigned scope, and instructor directions.
3. Read the complete [student setup and lab guide](../../labs/ot-security/STUDENT_LAB_GUIDE.md) and the supplied [project README](../../labs/ot-security/README.md).
4. Prepare an evidence log, risk register, and topology sketch using the course templates.

## Learner tasks

1. Create an Ubuntu VM in VMware or VirtualBox and take a clean snapshot.
2. Install the dependencies in a virtual environment under `labs/ot-security/local-linux/`, then disconnect the VM network adapter.
3. Verify the local copy uses loopback only and start the plant, validation guard, and dashboards in separate terminals.
4. Record a baseline and confirm that the VM is not using Bridged networking or port forwarding.
5. Run the pressure-hold demonstration against the direct port and then the guarded port; compare the output, dashboard values, and guard events.
6. Run the remaining demonstrations one at a time, following the student guide. Do not modify targets, ports, duration, request counts, or threads.
7. Explain the observed results, relevant validation layer, limitations, and possible additional controls in the final report.
8. Stop all programs, remove or retain generated files according to the course evidence policy, and record clean-up status.

## Evidence and assessment

Submit the architecture/register map, baseline and test screenshots, concise results table, relevant guard-event evidence, risk-register entry, limitations analysis, and clean-up statement. Use the supplied [evidence log](../templates/evidence-log-template.md), [topology/register map](../templates/topology-and-register-map-template.md), [risk register](../templates/risk-register-template.csv), and [final report](../templates/final-report-template.md).

Assessment should reward safe scope control, reproducibility, accurate interpretation, honest limitations, and clear evidence—not simply whether a demonstration produced a particular value. Learners must use their own observations and must not submit another learner's evidence.

## Instructor note

This is a deliberately small educational simulator, not an operational safety product. The code and dashboards are unauthenticated, and the guard does not provide comprehensive process, identity, or availability protection. The original archive files are preserved unchanged; the student guide's separate local copy is loopback-only. Do not request or perform demonstrations against real devices or networks.
