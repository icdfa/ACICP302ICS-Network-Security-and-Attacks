# Activity 08 — Supplied Source-Code Modbus/TCP OT Security Lab

## Purpose

Complete the hands-on run of the course-provided Modbus/TCP simulation. This is the core applied lab and is required unless the instructor explicitly waives it. Learners use the source supplied for this course; they are not asked to create a replacement simulator.

## Authorized source and boundary

Use only `labs/ot-security/student-lab-source/` inside the assigned Ubuntu guest VM. This source is the loopback-safe course copy: the clients and services use `127.0.0.1`. The directory `labs/ot-security/archive-original/` contains an archived copy from an earlier bundle and must not be executed; its scripts use a non-loopback target and broad listener defaults. Do not use bridged networking, port forwarding or any real/external device. Follow the complete [Student Lab Guide](../../labs/ot-security/STUDENT_LAB_GUIDE.md).

## Learning outcomes

Learners will identify the supplied plant and register model, compare direct and guarded telemetry, observe the provided range/step/drift checks, capture and interpret evidence, and state the guard’s limitations without overstating what this educational example can guarantee.

## Preparation

1. Complete Activity 00 and review `SECURITY_AND_SAFETY.md`.
2. Obtain repository access from the course owner or use the instructor-provided archive.
3. Prepare the assigned Ubuntu VM and clean snapshot. Install approved dependencies during the permitted setup window; disconnect the VM network adapter for execution.
4. Verify the canonical source path and record the course source commit.
5. Prepare the evidence log, topology/register-map, risk register and approved test plan.

## Learner tasks

1. Verify the student source contains only loopback destinations/binds. If the check reports a non-loopback address, stop and contact the instructor; do not edit or run it.
2. Start the supplied plant, guard and dashboards using the Student Lab Guide. Record a normal baseline and compare the direct and guarded views.
3. Capture normal local Modbus/TCP traffic and connect a request/response to the supplied data model.
4. Run at least three approved, bounded demonstrations one at a time using the documented defaults. Compare the direct and guarded path, dashboards, script output and relevant event records.
5. Explain which guard checks are evidenced, any difference from expected results, and limitations such as authentication, availability or correlated values.
6. Stop all processes, verify clean shutdown/recovery and preserve only evidence allowed by the instructor.

## Evidence and assessment

Submit your own source-version record, annotated architecture/register map, baseline and comparison evidence, learner-created capture and analysis, three-scenario test plan/results, relevant event evidence, risk entry, limitations analysis and cleanup statement. Use the [evidence log](../templates/evidence-log-template.md), [topology/register-map template](../templates/topology-and-register-map-template.md), [risk register](../templates/risk-register-template.csv), and [final report template](../templates/final-report-template.md).

Assessment rewards safe execution, accurate interpretation, reproducible evidence, honest limitations and recovery—not code volume. The provided source must be attributed, not described as learner-authored work.

## Instructor note

This is a small unauthenticated educational simulation, not an operational safety or production security product. The guard is limited and tuned to this simulated process. No request or demonstration against real devices or networks is authorized.
