# Activity 00 — Lab Preflight and Safety

## Purpose

Prepare the assigned Ubuntu VM and verify that you will use the authorized course source. This activity is mandatory before launching any simulation process.

## Tasks

1. Confirm repository access or obtain the approved archive from the instructor. Follow `labs/ot-security/STUDENT_LAB_GUIDE.md`.
2. Create or restore the instructor-assigned clean VM snapshot. Confirm the network adapter is not bridged and there is no port forwarding. Complete approved package downloads before disconnecting the adapter for the lab run.
3. Locate the canonical student source: `labs/ot-security/student-lab-source/`. Do not execute anything under `labs/ot-security/archive-original/`.
4. Verify that the student source uses `127.0.0.1` for its clients and service binds. If any target is not loopback, stop and contact the instructor; do not edit the source to make the check pass.
5. Record the course repository commit (`git rev-parse HEAD`), VM/snapshot, date and WAT time, permitted scope, stop condition and recovery method.
6. Start the evidence log and set up your private learner evidence workspace using `starter/README.md`.

## Evidence to submit

A completed preflight/evidence-log entry, VM and snapshot details, source path and commit, loopback check result, initial state and signed safety declaration.

## Completion check

Do not proceed until you and the instructor-approved scope agree, the canonical source path is confirmed, and no bridged/public connectivity or non-loopback target is present.
