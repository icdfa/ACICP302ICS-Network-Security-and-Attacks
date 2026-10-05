# OT Security Simulation — Student Start Here

This folder contains the source-code lab used in ACICP302ICS. Learners use and analyze the supplied simulation; they do not need to build a replacement implementation.

## Use this source

Run only [`student-lab-source/`](student-lab-source/), the course’s loopback-only student copy. Follow [`STUDENT_LAB_GUIDE.md`](STUDENT_LAB_GUIDE.md) for VM setup, dependency installation, run steps, approved demonstrations, evidence and cleanup.

## Do not run the archive

[`archive-original/`](archive-original/) is a preserved reference copy of the earlier project bundle. Its scripts have non-loopback network defaults. It is included for provenance/reference only and **must not be executed by students**. Do not copy commands from its legacy materials. The current activity instructions and safe commands are in the Student Lab Guide.

## Safety configuration

The canonical student source targets and binds to `127.0.0.1` and is intended to run inside the assigned Ubuntu guest. Do not change its addresses, ports, demonstration parameters or scope. Do not use bridged networking, port forwarding, real equipment or external networks. If any source target is not loopback, stop and notify the instructor.

This educational simulator is not production OT protection or a process-safety system. Students must submit their own analysis and evidence, cite the course source and never claim the provided code as their own.
