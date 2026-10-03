# Activity 00 — Lab Preflight and Safety

## Purpose

Establish an authorised, isolated and recoverable workspace before you build or test anything.

## Complete these tasks

1. Record the assigned VM names, snapshot names and the approved isolated network name in your evidence log.
2. Confirm that the VM network is host-only or instructor-approved internal networking; it must not be bridged or public.
3. Create a clean working folder/repository using the structure in [`starter/README.md`](../../starter/README.md).
4. Draw the initial topology: process/PLC, HMI/dashboard, analyst workstation and defensive component (if separate).
5. Record the starting state and create or confirm a clean rollback snapshot.
6. Read and sign the project safety declaration in your report.

## Evidence to submit

- Completed first entry in the [evidence log](../templates/evidence-log-template.md).
- Topology draft showing only your authorised simulated components.
- Screenshot or record proving the clean snapshot/start state.
- Safety declaration signed by every team member.

## Success criteria

You can identify every system in scope, explain the isolation boundary and restore the lab to its initial state.

## Stop condition

Stop and notify the instructor if any adapter is bridged, an address is externally routable, a real device is visible, or the allocated network is unclear.
