# Activity 06 — Controlled Security Validation

## Purpose

Run approved demonstrations supplied with the course source, compare direct and guarded simulation behaviour, and document evidence-based conclusions. The demonstrations must remain on loopback in the assigned Ubuntu VM.

## Required approach

Before execution, complete the [test-plan template](../templates/security-validation-test-plan-template.md). For each scenario, record the canonical source and script, loopback target/path, starting state, expected outcome, evidence method, stop condition and recovery. Obtain instructor approval where required.

## Tasks

1. Select at least three scenarios explicitly permitted by the Student Lab Guide or instructor. Use the supplied script defaults unchanged.
2. Record a normal/baseline state before each scenario.
3. Run one demonstration at a time against the documented direct or guarded local path, as planned. Do not change target address, port, request count, duration, threads or other parameters.
4. Observe relevant process/dashboard state, script output and guard events. Capture only evidence needed for the analysis.
5. Compare expected with observed behaviour. State whether the path accepted, rejected, alerted on or otherwise responded to the simulated condition; explain unexpected or variable results honestly.
6. Stop the scenario and verify recovery before proceeding to the next one.

## Evidence to submit

Completed test plan; evidence for at least three scenarios; expected-versus-observed comparison; source/script identification; and recovery verification after each scenario.

## Safety boundary

Use only the canonical loopback-only student source. Do not execute archived scripts, widen test scope, or target any external system. Stop immediately if an address other than `127.0.0.1` appears or a VM becomes unstable.
