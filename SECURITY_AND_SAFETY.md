# Security and Safety Rules

## Non-negotiable authorisation boundary

This course permits testing **only** against the learner’s own simulated OT testbed inside the ICDFA-issued isolated environment.

Never direct activity at:

- A real PLC, HMI, SCADA server, industrial controller or field device.
- Any production, campus, home, public or third-party network.
- A bridged adapter, publicly reachable address or unauthorised VM.
- Any target outside the written practical scope.

## Required lab controls

1. Start from the clean snapshot assigned by the instructor.
2. Use host-only or instructor-approved internal virtual networking only.
3. Keep services bound to the assigned isolated interface or local host; do not make them publicly reachable.
4. Record the initial state before every validation activity.
5. Stop immediately if behaviour leaves the simulated environment, a VM becomes unstable, or a scope doubt arises.
6. Restore the snapshot or approved recovery state after testing.
7. Escalate any abnormal behaviour to the instructor before continuing.

## Controlled validation only

The course explores process-integrity and availability risks through **controlled simulation**. The objective is to understand detection, validation, logging, containment and recovery—not to target external systems.

Your documentation must state:

- The authorised target and boundary.
- The expected and observed system behaviour.
- The defensive control being evaluated.
- The recovery action and final verified state.

## Academic integrity

Your report, code, packet capture, screenshots and logs must originate from your own assigned environment. Misrepresentation of evidence, copied work, unauthorised target interaction or unsafe lab conduct is a serious academic and safety breach.
