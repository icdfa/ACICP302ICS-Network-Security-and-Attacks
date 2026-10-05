# Activity 05 — Analyze the Supplied Defensive OT Guard

## Purpose

Explain how the course-provided guard evaluates simulated Modbus/TCP changes, what evidence it produces and which risks it does not address. A new guard implementation is not required.

## Tasks

1. Inspect `guard.py` and the guarded dashboard in `labs/ot-security/student-lab-source/plant_sim/`.
2. Build a decision table identifying each implemented check, input, condition, action (accept/reject/alert), and any relevant event/log output. Confirm your interpretation from the source and a normal run.
3. Identify assumptions and limits. Consider client authentication/authorization, direct-path access, availability, correlated process values, threshold tuning and recovery.
4. Map the guard’s demonstrated checks to the risks in your risk register. Separate implemented safeguards from recommended future controls.
5. Do not change the source or thresholds unless the instructor authorizes a defined extension.

## Evidence to submit

A learner-created architecture/decision table; relevant source references; screenshot or structured event sample from normal operation; guard limitations/residual-risk analysis; and updated risk-register entries.

## Success criteria

You accurately describe what the supplied guard does and does not do, and support each statement with source or runtime evidence. Do not claim the guard makes a real process safe.
