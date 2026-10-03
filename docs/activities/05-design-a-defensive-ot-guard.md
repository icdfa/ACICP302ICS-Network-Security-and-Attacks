# Activity 05 — Design a Defensive OT Guard

## Purpose

Build a defensive control that makes unsafe process changes visible and prevents or contains them within your simulation.

## Build requirement

Create an inline guard, validation layer, monitoring service or equivalent defensive component between the authorised client and your simulated process. Your design must implement at least three of the following safeguards:

- Physical safe-range validation.
- Maximum step/change-rate validation.
- Rolling-baseline or drift detection.
- Authorised-client allow-list or role validation.
- Alert generation and structured event logging.
- Fail-safe handling and clear recovery state.

## Complete these tasks

1. Define safe operating assumptions for each protected process value.
2. Document the rule logic in a simple decision table or flow diagram.
3. Implement the control in your own project.
4. Demonstrate normal operations passing through the control.
5. Record accepted, rejected or alerted events in a structured log.

## Evidence to submit

- Guard/control architecture diagram.
- Decision table or validation logic description.
- Screenshot/log of normal accepted activity.
- Sample structured event record and explanation.
- Updated risk register showing the controls mapped to findings.

## Success criteria

The control makes an evidence-based decision, produces an understandable record and does not silently obscure normal process behaviour.
