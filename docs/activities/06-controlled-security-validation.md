# Activity 06 — Controlled Security Validation

## Purpose

Validate your own defensive design using authorised simulation scenarios, then compare the observed protected state with the baseline state.

## Required approach

Create a test plan before running any scenario. The plan must state the authorised target, expected impact, success measure, collection method, stop condition and recovery step.

Use only your own simulation. Select at least three relevant scenarios, such as:

- A process value request outside the documented safe range.
- An unusually large or rapid value change.
- A gradual deviation from the baseline.
- Repeated normal-looking requests that require visibility or rate control.

## Complete these tasks

1. Capture the baseline state before each scenario.
2. Execute the authorised simulation scenario only within the assigned lab.
3. Observe the process, dashboard, packet capture and defensive event logs.
4. Compare expected and actual guard behaviour.
5. Record whether the control allowed, rejected, alerted on or contained the event.
6. Restore a safe normal state and verify recovery.

## Evidence to submit

- Completed [test-plan template](../templates/security-validation-test-plan-template.md).
- Relevant capture/log evidence for each scenario.
- Defended-versus-baseline comparison table.
- Recovery verification for each scenario.

## Success criteria

Your conclusion is based on packet, log and process-state evidence—not assumption or screenshots alone.
