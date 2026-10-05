# Security and Safety Rules

## Non-negotiable authorization boundary

This course uses the instructor-provided simulation source only. Execute only `labs/ot-security/student-lab-source/` inside the assigned Ubuntu VM. The source is intended to use loopback (`127.0.0.1`) only.

**Never execute files under `labs/ot-security/archive-original/`.** That archived project copy contains non-loopback target/bind defaults and is retained for reference, not student use. If a script or configuration points to any address other than loopback, stop and contact the instructor.

Never direct activity at:

- A real PLC, HMI, SCADA server, industrial controller or field device.
- Any production, campus, home, public or third-party network.
- A bridged adapter, publicly reachable address, port forward or unauthorized VM.
- Any host other than the documented loopback services in the student source.

## Required lab controls

1. Start from the clean snapshot assigned by the instructor.
2. Use the assigned Ubuntu VM; disconnect its network adapter for lab execution after any approved dependency installation.
3. Do not change the student source’s loopback address, bind address, ports, request counts, durations, thread counts or target scope.
4. Record the source path, source commit, initial state and approved scope before each validation activity.
5. Stop immediately if a non-loopback address appears, a VM becomes unstable, a process behaves unexpectedly or a scope doubt arises.
6. Stop all lab processes and verify the approved safe/normal state after testing; restore the assigned snapshot if directed.
7. Escalate unexpected behaviour to the instructor before continuing.

## Controlled validation only

The demonstrations are bounded simulations intended to explain process-integrity, visibility, defensive response and recovery. They are not authorization to test a real or external system. Before each scenario, record:

- The specific student-source script and documented loopback target.
- The expected and observed system behaviour.
- The defensive control and evidence being evaluated.
- A stop condition and recovery action.

Run only scenarios specified by the Student Lab Guide and the instructor. Do not improvise targets or intensify a test.

## Academic integrity

The provided code may be used as course lab material and must be attributed. Your diagrams, captures, observations, analysis, risk register, test records and report must be your own and come from your assigned environment. Never present the instructor-provided code as code you authored, fabricate evidence, or share another learner’s evidence.
