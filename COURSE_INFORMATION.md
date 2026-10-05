# Course Information

## Course identity

| Item | Details |
|---|---|
| Course code | ACICP302ICS |
| Course title | Network Security & Attacks |
| Delivery mode | Practical laboratories |
| Academy | International Cybersecurity and Digital Forensics Academy (ICDFA) |
| Learning model | Inspect, run, observe, validate, document and defend a supplied simulation |

## Course purpose

This course develops practical ability to analyze an OT/ICS network, understand Modbus/TCP behaviour, assess an authorized simulated environment safely, evaluate defensive controls and communicate findings using evidence. The course provides the simulation source code. Learners use that source as the lab environment rather than building a replacement implementation.

The canonical student source is `labs/ot-security/student-lab-source/`. It is configured for loopback use in the assigned Ubuntu VM. `labs/ot-security/archive-original/` is an archival copy only and must not be executed. See the [Student Lab Guide](labs/ot-security/STUDENT_LAB_GUIDE.md).

## Intended learning outcomes

On successful completion, learners should be able to:

1. Explain the supplied simulated OT architecture, component roles and data flow.
2. Inspect and document the supplied Modbus/TCP data model and normal process state.
3. Capture and interpret normal industrial-protocol traffic from the approved simulation.
4. Assess the documented local services and explain process-relevant exposure and risk.
5. Explain the supplied defensive guard’s checks, outputs and limitations.
6. Compare normal and simulated validation behaviour using packets, logs and system observations.
7. Restore the simulation safely and communicate evidence-based findings in a professional report and demonstration.

## Prior knowledge and environment

This practical builds on introductory networking, PLC/SCADA concepts, Modbus and Wireshark. Learners use the instructor-issued isolated Ubuntu virtual machine and the course-provided source repository. The instructor supplies the exact VM, access arrangements and lab window. Do not substitute a personal, campus, public or production network.

The course repository is private. The instructor must grant enrolled learners access or provide the approved course archive through the LMS.

## Learner responsibility and academic integrity

- Use and study the supplied source as the lab platform; a new implementation is not required.
- Produce your own notes, diagrams, captures, screenshots, logs, analysis, risk assessment, test records and report.
- Cite the course repository and record the source commit used. Do not present the course source as code you wrote.
- Do not copy another learner’s evidence or report. Be prepared to explain every conclusion during the defence.
- Do not modify course code or safety parameters unless the instructor authorizes a specific extension.
- Submit evidence through your own private learner/team repository or instructor-approved workspace, not by changing the course-source repository.

## Required final artefacts

- Preflight/safety record identifying the assigned VM, source path and source commit.
- Annotated architecture and process/data-flow description.
- Register/data-point map and normal-operation baseline.
- Learner-created packet capture with annotated Modbus/TCP request/response analysis.
- Local-only service/exposure record and risk register.
- Guard behaviour/limitations analysis and relevant event evidence.
- Approved validation plan with at least three scenarios and recovery verification.
- Evidence log, final report and live technical defence.
