# Canonical Student Lab Source — Loopback Only

This is the instructor-provided source code learners use for the ACICP302ICS practical. It is a safety-constrained course copy of the simulation, configured for loopback (`127.0.0.1`) inside the assigned Ubuntu VM. Learners should inspect and run this source, then submit their own analysis and evidence; writing a replacement simulator is not required.

Use the [Student Lab Guide](../STUDENT_LAB_GUIDE.md) for all setup, run, demonstration and cleanup instructions. Do not change target addresses, bind addresses, ports, request counts, durations or thread counts.

The sibling `../archive-original/` directory is an archival copy only. It has non-loopback defaults and must not be executed. This student source is an educational demonstration, not production OT security or a safety product.

Dependencies for this source are listed in `requirements.txt`. Install them only in a project-local virtual environment during the approved setup window. Disconnect the VM network adapter before running the lab where instructed.
