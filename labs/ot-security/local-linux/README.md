# Localhost-only Ubuntu/Linux lab copy

This is a separate, localhost-only copy prepared for running the OT simulation inside an Ubuntu guest VM. It is distinct from the original project files in the parent folder; those original files remain unchanged.

Use the [Student Lab Guide](../STUDENT_LAB_GUIDE.md) for VMware/VirtualBox setup, dependencies, run steps, exercises, evidence, and cleanup.

## Safety configuration

- Modbus clients target `127.0.0.1` only.
- The plant, guard, and dashboards bind to `127.0.0.1` only.
- Use this copy inside an Ubuntu VM; do not change the host or port settings or expose ports through VM forwarding.
- This is an educational simulation, not production OT protection.

The source code is based on the supplied project, with network defaults changed only in this separate copy to constrain all lab traffic to loopback. Flask is included in this copy's `requirements.txt` because the dashboards import it.
