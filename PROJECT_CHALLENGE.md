# Practical Lab Challenge — Analyze, Operate, Defend and Recover the Supplied OT Simulation

## Challenge statement

Use the **instructor-provided source code** in `labs/ot-security/student-lab-source/` to investigate a simulated Modbus/TCP industrial process. Establish its normal behaviour, explain its architecture and data model, capture and interpret local protocol traffic, evaluate the supplied defensive guard, run the bounded demonstrations within the approved scope, and verify recovery.

This is a source-code-guided practical. You are **not required to create a replacement plant simulator, dashboard, Modbus service or guard**. Your assessed contribution is your own safe execution, technical reasoning, evidence, risk analysis and report. Do not alter course code unless the instructor authorizes a specific extension.

## Required practical outcomes

| Area | What you must demonstrate using the supplied source |
|---|---|
| Preflight and scope | Confirm repository access, the assigned Ubuntu VM, snapshot and isolated configuration; record the source path and commit. |
| Architecture and baseline | Trace the plant, Modbus/TCP service, dashboards, guard and event flow from the code; run the normal simulation and document its baseline. |
| Data model | Inspect the provided process/register definitions; document addresses, units, ranges, state meaning and normal update behaviour. |
| Packet analysis | Capture normal lab traffic and explain a matching Modbus/TCP request/response in relation to the simulated process. |
| Exposure assessment | Inventory only the documented local lab services and their roles; identify risks and appropriate controls. |
| Guard evaluation | Explain the supplied validation checks, observable decisions and limitations using source and runtime evidence. |
| Controlled validation | Prepare a plan and run at least three instructor-approved, bounded demonstrations from the supplied source against the loopback-only simulator. |
| Recovery and communication | Stop the lab cleanly, verify the normal/safe state, link each conclusion to evidence and present the result. |

## Authorized student source

The single student-execution source is [`labs/ot-security/student-lab-source/`](labs/ot-security/student-lab-source/). Follow [`labs/ot-security/STUDENT_LAB_GUIDE.md`](labs/ot-security/STUDENT_LAB_GUIDE.md) exactly. The directory `labs/ot-security/archive-original/` contains an archival copy from an earlier bundle; its scripts use non-loopback network defaults and are **not authorized for execution**.

## Minimum evidence package

- Preflight record, VM/snapshot details, source path and source commit.
- Learner-annotated architecture/data-flow diagram and normal baseline.
- Register/data-point map with units, ranges and alarm/status meaning.
- Learner-created local packet capture, annotated request/response and explanation.
- Loopback-only service inventory, risk-register entries and control recommendations.
- Guard source analysis, safeguards/limitations table and relevant event/log evidence.
- Approved test plan for at least three bounded scenarios, with expected-versus-observed results.
- Recovery/cleanup verification, final report and demonstration notes.

## Non-functional requirements

- Use the supplied course source in the assigned isolated Ubuntu VM; never target any real or external system.
- Preserve the canonical loopback configuration. Do not change target addresses, bind addresses, ports, request counts, duration, thread counts or script scope.
- Record the method, starting state, exact authorized action, observation, evidence reference, conclusion and recovery for each test.
- Keep credentials, personal information and sensitive evidence out of the public web and out of the course-source repository.
- Attribute the course-provided source and any additional references. Your analysis and evidence must be your own and explainable during the defence.

## Out of scope

- Building a new simulator/guard as a prerequisite.
- Executing files from `labs/ot-security/archive-original/`.
- Real industrial equipment, production systems, external networks, bridged networking or port forwarding.
- Scanning or testing any host other than the documented loopback services in the student source.
- Unapproved code changes or demonstrations beyond the published lab guide.
