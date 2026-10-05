# Student Lab Guide — Supplied OT Security Simulation on Ubuntu

**Course:** ACICP302ICS — Network Security & Attacks
**Guide prepared by:** Aminu Idris, AMCPN

This course uses the instructor-provided simulation source. Run only `labs/ot-security/student-lab-source/` inside the assigned Ubuntu guest VM. The `labs/ot-security/archive-original/` directory is an archival copy with unsafe network defaults and **must not be executed**. You are expected to inspect and use the supplied code; building a replacement simulator is not required. Your assessed work is your own analysis, observations, captures, logs, report and evidence.

## 1. Non-negotiable safety rules

- Use only the canonical `student-lab-source/` directory identified in this guide.
- Do not run or copy commands from `archive-original/`.
- Keep all simulation traffic on `127.0.0.1` inside the assigned Ubuntu VM. Do not use bridged networking, port forwarding, real devices, public/campus/home networks or another learner’s VM.
- Do not change targets, bind addresses, ports, request counts, durations or thread counts in the supplied scripts.
- If a target/bind address is not `127.0.0.1`, stop and notify the instructor. Do not edit the source to force the check to pass.
- This is an educational simulation, not a production security or process-safety product.

## 2. Prepare the Ubuntu VM

Use the instructor-approved Ubuntu LTS image and VMware or VirtualBox installation. Create a fresh guest VM for this lab and take a clean snapshot. Never install or run this lab on a production OT computer.

**VirtualBox:** In VM Settings → Network, do not select Bridged Adapter and do not configure port forwarding. Use NAT temporarily only if the instructor permits it for package/repository downloads. Shut down the VM and set the adapter to Not attached before running the lab. See the [VirtualBox networking manual](https://www.virtualbox.org/manual/ch06.html).

**VMware Workstation/Player:** Do not select Bridged and do not configure port forwarding. Use NAT temporarily only for approved downloads. Disconnect the virtual adapter before the lab run. If the instructor requires an attached adapter, use an approved Host-only configuration, never Bridged. See [VMware Host-only networking](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/configuring-host-only-networking.html) and [networking modes](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/understanding-common-networking-configurations.html).

The simulation itself uses Linux loopback and does not need internet access. Complete approved downloads first, shut down the guest, disconnect its adapter, then start the lab.

## 3. Obtain the course repository

The GitHub repository is private. Ask the course owner to grant you access, or use the instructor-provided approved archive. Do not share passwords, access tokens or credentials.

If repository access is authorized, use NAT only temporarily for cloning and package setup. In an Ubuntu terminal:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
mkdir -p ~/course
cd ~/course
git clone https://github.com/icdfa/ACICP302ICS-Network-Security-and-Attacks.git
cd ACICP302ICS-Network-Security-and-Attacks
```

If you received an archive, extract it inside the guest and change to the extracted course-repository directory instead. If you used a shared folder to transfer files, copy the repository into the guest’s home directory and disable/unmount the shared folder before running the lab.

Record the course-source commit before starting:

```bash
git rev-parse HEAD
```

## 4. Use the canonical student source only

Change to the single authorized runnable source directory:

```bash
cd ~/course/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/student-lab-source
```

If your repository is stored elsewhere, adjust only the parent path; do not change the final `labs/ot-security/student-lab-source` path. Confirm the archived copy is not your working directory. Before installing or launching anything, check that the runnable scripts do not contain the archive’s unsafe defaults:

```bash
grep -R -nE '192\.168\.2\.139|0\.0\.0\.0' plant_sim || true
```

This command should produce no matching output. Then confirm that the expected loopback configuration is present:

```bash
grep -R -n '127\.0\.0\.1' plant_sim
```

If the first command finds a match or the second finds no loopback configuration, stop and notify the instructor. Do not run scripts from `archive-original/`.

The source uses these local-only services:

| Component | Local address/port |
|---|---|
| Simulated plant, direct Modbus path | `127.0.0.1:5020` |
| Validation guard Modbus path | `127.0.0.1:5021` |
| Direct dashboard | <http://127.0.0.1:8080> |
| Guarded dashboard | <http://127.0.0.1:8081> |

The dashboards do not require login. Open them only in the browser inside the Ubuntu guest. Do not forward these ports to the host.

## 5. Install dependencies

Complete package installation only during the instructor-approved setup window. Create a project-local virtual environment:

```bash
cd ~/course/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/student-lab-source
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The provided requirements include the packages needed by this lab version. Do not use `sudo pip`, install packages globally or remove `.venv` while lab processes are running. If the installation needs internet access, use NAT only temporarily as approved, then shut down the guest and disconnect its adapter before the exercise. Ask the instructor for an approved offline package source if downloads are prohibited.

## 6. Start the supplied simulation

Keep the VM network adapter disconnected for the lab run. Open four terminal windows inside Ubuntu. In **each** terminal, activate the environment and enter the supplied code folder:

```bash
cd ~/course/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/student-lab-source
source .venv/bin/activate
cd plant_sim
```

Start the services in this order, one process per terminal:

| Terminal | Command | Expected behaviour |
|---|---|---|
| 1 | `python3 plant.py` | Simulated process starts on loopback port 5020. |
| 2 | `python3 guard.py` | Guard starts on loopback port 5021 and forwards accepted writes to the local plant. |
| 3 | `python3 dashboard.py` | Direct dashboard starts on loopback port 8080. |
| 4 | `python3 dashboard_guarded.py` | Guarded dashboard starts on loopback port 8081. |

Open the dashboards in Ubuntu:

- Direct view: <http://127.0.0.1:8080>
- Guarded view: <http://127.0.0.1:8081>

Initial values are approximately 67.0 °C, 34.0 bar and 90.0 Nm³/h; values may move slightly as the simulator runs. The guard is rule-based, not an AI model.

## 7. Baseline and packet capture

Before any demonstration, record the VM name, date/time, source commit, loopback check, disconnected network adapter, dashboard readings and normal observations. Save learner-created screenshots with relevant context.

For the packet activity, capture only a short period of the Ubuntu guest’s loopback (`lo`) traffic for the documented Modbus/TCP lab port. Do not capture other interfaces or unrelated traffic. In Wireshark, identify one request and matching response, then relate the observed fields to your register map and process state. Stop the capture and store it only in the instructor-approved private evidence location.

## 8. Run approved demonstrations

Keep the four services running and use a fifth Ubuntu terminal. Activate the same environment and enter the source folder:

```bash
cd ~/course/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/student-lab-source
source .venv/bin/activate
cd plant_sim
```

Use the activity test plan and instructor approval. Select at least three permitted demonstrations; run them one at a time and use the supplied arguments unchanged. Each script is limited to the local simulator; port `5020` is the direct path and port `5021` is the guarded path.

| Script | Demonstration | Supplied command pair |
|---|---|---|
| `attack_hold.py` | Requests a pressure value outside the simulated range | `python3 attack_hold.py 5020` then `python3 attack_hold.py 5021` |
| `false_data_attack.py` | Sends the provided batches of out-of-range process values | `python3 false_data_attack.py 5020` then `python3 false_data_attack.py 5021` |
| `slow_drift_attack.py` | Sends the provided incremental pressure changes | `python3 slow_drift_attack.py 5020` then `python3 slow_drift_attack.py 5021` |
| `replay_attack.py` | Repeats the provided pressure write | `python3 replay_attack.py 5020` then `python3 replay_attack.py 5021` |
| `recon_scan.py` | Reads the limited register range documented by the script | `python3 recon_scan.py 5020` then `python3 recon_scan.py 5021` |
| `dos_attack.py` | Fixed demonstration of 200 read requests using 10 threads | Run only if the instructor approves; then use `python3 dos_attack.py 5020` followed by `python3 dos_attack.py 5021` |

Do not increase request counts, duration, rate or thread count. Run any availability/load demonstration only if it is explicitly approved. After each scenario, record actual script output, dashboard observations and relevant `plant_sim/events.jsonl` entries. Results may vary with timing; report what occurred rather than trying to force a particular result.

## 9. Analysis and evidence

For each scenario, explain which check is relevant (for example, absolute range, step-size or rolling-baseline drift); whether the direct/guarded views and event record agree; and what the result does and does not show. Consider limits such as authentication, client authorization, availability, correlated process values, direct-path bypass and process-specific thresholds. This guard is not a real safety system.

Use the course templates for the evidence log, topology/register map, risk register, test plan and final report. Record the script, local port/path, starting state, expected and observed results, evidence reference, conclusion and recovery. Attribute the course source and record its commit; your analysis and evidence must be your own. Do not commit `.venv`, credentials, personal/site data or unapproved logs/captures to the shared course-source repository.

## 10. Stop and clean up

When finished:

1. Stop each service with **Ctrl+C** in its terminal and wait for each demonstration script to finish.
2. Confirm the lab processes have stopped and the local ports are no longer listening.
3. Deactivate the virtual environment with `deactivate`.
4. Handle `plant_sim/events.jsonl` and evidence according to the instructor’s policy.
5. Restore the clean VM snapshot if directed and leave the network adapter disconnected.

If a dashboard disconnects, check that the plant was started first and the guard second. If any target/bind check fails, stop; do not edit the source or run the archived scripts.

## Official VM networking references

- [VirtualBox User Manual — Virtual Networking](https://www.virtualbox.org/manual/ch06.html)
- [VMware Workstation — Host-Only Networking](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/configuring-host-only-networking.html)
- [VMware Workstation — Common Networking Configurations](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/understanding-common-networking-configurations.html)
