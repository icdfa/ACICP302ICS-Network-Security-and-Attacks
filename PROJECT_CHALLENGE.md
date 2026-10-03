# Practical Build Challenge

## Challenge statement

Build and defend an original, isolated **Modbus/TCP OT security testbed** that represents a small simulated industrial process.

Your implementation must show the difference between normal operation, an unsafe simulated condition and a protected state. The course assesses your engineering judgement, evidence and recovery—not a copied interface or a particular programming language.

## Minimum functional acceptance criteria

| Capability | Your implementation must demonstrate |
|---|---|
| Simulated process | At least three changing process values and one alarm/status state |
| Modbus/TCP service | A documented, functioning data model that the authorised client can read |
| Monitoring view | A dashboard/HMI or equivalent that makes normal state understandable |
| Packet evidence | A capture and explanation of normal Modbus/TCP request/response behaviour |
| Exposure record | A strictly scoped inventory of the simulation’s relevant services/data points and risks |
| Defensive control | At least three meaningful validation, restriction, detection or logging safeguards |
| Controlled validation | Evidence that the control reacts appropriately to authorised simulated abnormal conditions |
| Recovery | Proof that normal, safe operation is restored after validation |

## Required defensive design qualities

Your defensive component must be purposeful, observable and explainable. It should document the assumptions behind its decision-making, the conditions it checks and the resulting event record.

Examples of valid safety checks include normal-range validation, unusually large value-change detection, baseline-deviation detection, authorised-client controls and structured alerts. Your design may use a different defensible combination with instructor approval.

## Non-functional requirements

- The testbed must be runnable only in the authorised isolated ICDFA lab environment.
- All configuration values relevant to your environment must be documented; do not publish credentials or real target details.
- Use meaningful commit messages and retain a clear development history.
- Write an original `README.md` with setup, safety, design and evidence sections.
- Explain limits honestly; a control that does not address every risk should state what it cannot protect.

## Out of scope

- Real industrial devices, production services and external networks.
- Public deployment or bridged connectivity.
- Copying a completed implementation, attack script, report, capture or evidence set.
- Any activity not expressly authorised by the practical brief and instructor.
