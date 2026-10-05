# Instructor Delivery Guide

This guide supports delivery of the source-code-guided ACICP302ICS practical. Learners use the course-provided OT simulation as the lab platform; they are not required to build a replacement implementation.

## Before release

1. Grant enrolled learners access to the private course repository, or provide the approved course archive through the LMS.
2. Direct learners to `labs/ot-security/STUDENT_LAB_GUIDE.md` and confirm they understand the canonical student source path: `labs/ot-security/student-lab-source/`.
3. Explicitly identify `labs/ot-security/archive-original/` as an archival, non-executable copy. Do not use it in demonstrations or learner instructions.
4. Confirm learner VMs use assigned snapshots and that the lab run is isolated; dependency downloads, if required, must be complete before disconnecting the adapter.
5. Allocate the evidence naming convention, team size, activity deadlines and submission path in the E-Campus.
6. Review the loopback-only boundary and stop conditions before every practical session.

## During delivery

- Demonstrate the supplied source as the common lab system. Do not imply that learners must reproduce or rewrite the implementation.
- Ask learners to trace code to observed process state, register/data model, packets, guard decisions and event records.
- Approve the validation scenarios before they run; ensure the learner uses the bounded instructions and loopback-only target.
- Assess technical reasoning, evidence quality, risk interpretation, recovery and live explanation—not code volume.
- Stop and investigate any non-loopback target, unexpected connectivity, unsafe configuration or report of instability.
- Authorize any source-code change as a separate, explicit extension and specify its scope.

## After delivery

- Confirm that all learner processes have stopped and the VM is in the approved normal/snapshot state.
- Confirm each learner/team has retained only evidence permitted by institutional policy.
- Assess each learner’s own analysis and evidence and verify they can explain the course source they used.
- Keep marks, learner submissions and answer material out of the course-source repository.
