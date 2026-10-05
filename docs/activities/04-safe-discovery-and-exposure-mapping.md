# Activity 04 — Safe Discovery and Exposure Mapping

## Purpose

Understand what local services the supplied simulation exposes and assess their process relevance without probing any external host or network.

## Tasks

1. Read the service/bind configuration in `labs/ot-security/student-lab-source/plant_sim/` and identify only the documented loopback endpoints and ports.
2. Prepare a scope card naming the assigned VM, loopback-only target, permitted observation method, time window, expected state, stop condition and recovery action.
3. Use source inspection and the Student Lab Guide’s approved read-only checks to confirm which services are active. Do not widen the range, change a target address or scan any non-loopback address.
4. Record each relevant endpoint’s component role, protocol, process significance and likely consequence of exposure or misuse.
5. Add evidence-based entries to the risk register with a preventative and detective control. Distinguish observed facts from inferred risk.

## Evidence to submit

Approved scope card; source-based local service inventory; relevant command/output or screenshot; risk-register entries; and a short conclusion explaining visibility versus safe operation.

## Safety boundary

This activity is not authorization to run general network discovery tools. Do not target any host except the documented loopback services in the student source. Stop if an endpoint resolves or binds outside `127.0.0.1`.
