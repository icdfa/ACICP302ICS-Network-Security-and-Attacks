# Learner Evidence Workspace Template

The course supplies the simulation source in `labs/ot-security/student-lab-source/`. Learners use that code as the lab environment; do not build a replacement source implementation unless the instructor assigns an extension.

Create your own private evidence repository or approved workspace. This suggested structure organizes your original observations and evidence; it is not a copy of the course source and is not a place to publish sensitive material.

```text
learner-evidence/
├── README.md                    # learner/team, course, source commit cited
├── docs/
│   ├── topology-and-flow.md     # your annotations of the supplied system
│   ├── register-map.md          # your verified data-point map
│   ├── risk-register.csv        # your scoped findings
│   └── test-plan.md             # approved scenarios and stop/recovery conditions
├── evidence/
│   ├── screenshots/             # labeled evidence from your assigned VM
│   ├── captures/                # approved PCAP/PCAPNG files
│   └── logs/                    # approved relevant outputs
├── evidence-log.md
└── report/
    ├── final-report.md
    └── evidence-index.md
```

Do not commit tokens, passwords, private keys, real site details or evidence the instructor has not approved for repository submission. Identify the course source URL and exact commit used. The supplied course code must be attributed and must not be described as learner-authored code.
