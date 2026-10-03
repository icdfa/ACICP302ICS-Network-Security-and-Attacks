# Student Project Starter

Create your own private project repository or instructor-approved workspace from this structure. Do not place completed learner solutions in the course repository.

```text
your-acicp302ics-project/
├── README.md
├── src/                 # Your original implementation
├── docs/
│   ├── topology.md
│   ├── register-map.md
│   ├── risk-register.csv
│   └── test-plan.md
├── evidence/
│   ├── screenshots/
│   ├── captures/
│   └── logs/
├── report/
└── requirements.txt     # Or equivalent dependency manifest
```

## Minimum project README

Your own `README.md` must include:

1. Project title, learner/team name and course code.
2. Purpose and simulated process description.
3. Isolated-lab-only safety statement.
4. Component diagram and data flow.
5. Setup prerequisites and safe local run instructions.
6. Evidence inventory and how to reproduce normal operation.
7. References and third-party library acknowledgements.

## Optional dependency reference

If your approved design uses a Python Modbus simulator and web dashboard, begin with `requirements.example.txt` as a dependency reference. You remain responsible for choosing compatible versions and documenting your own implementation.
