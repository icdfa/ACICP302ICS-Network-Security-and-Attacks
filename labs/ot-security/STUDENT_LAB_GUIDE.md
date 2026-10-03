# Student Lab Guide: OT Security Testbed on Ubuntu

**Course:** ACICP302ICS — Network Security & Attacks
**Guide prepared by Aminu Idris, AMCPN**

This guide is for students running Ubuntu Linux **inside a VMware or VirtualBox virtual machine**. The original project files from `ot-security-main.zip` are preserved unchanged in this folder. Use the separate `local-linux/` copy for the lab: it binds services and directs demonstration clients to **127.0.0.1 only**, so it does not contact another computer on your network.

## 1. Safety rules

- Run this lab only in your own course VM, using the `local-linux/` copy described below.
- Do not run the original `plant_sim` scripts in the root of this folder. They target `192.168.2.139` and bind servers to `0.0.0.0`, which can reach/expose systems beyond the VM.
- Do not change the local copy's address, ports, request count, or duration; do not point any script at a real PLC, HMI, SCADA system, industrial device, public IP, campus network, or another student’s VM.
- Do not configure bridged networking, port forwarding, or a connection to a production network for the lab.
- If the network or destination behaves unexpectedly, stop all programs and tell the instructor.
- This is a learning simulation, not a production defense, safety system, or authorization to test real critical infrastructure.

## 2. Create an Ubuntu VM

Use an instructor-approved Ubuntu LTS installer and a supported VMware or VirtualBox version. Create a fresh VM for this lab; do not install the software on a production or shared OT computer. A practical student setup is a normal Ubuntu Desktop or Server VM with enough memory and disk for the OS, Python, and browser.

### VirtualBox

1. Create a new VM and install Ubuntu from the instructor-approved ISO.
2. In the VM's **Settings → Network**, do not select **Bridged Adapter** and do not configure port forwarding.
3. If internet access is needed to install Ubuntu updates or Python packages, use **NAT temporarily**. Shut the VM down afterward and set the adapter to **Not attached** for the lab run. VirtualBox describes “Not attached” as a virtual network card with no connection; see the [VirtualBox networking manual](https://www.virtualbox.org/manual/ch06.html).
4. Take a clean snapshot before starting the lab.

### VMware Workstation / Player

1. Create a new VM and install Ubuntu from the instructor-approved ISO.
2. Do not select **Bridged** networking and do not configure port forwarding.
3. If internet access is needed to install Ubuntu updates or Python packages, use **NAT temporarily**. Shut the VM down afterward and disconnect the virtual network adapter before the lab run. If the adapter must remain connected, use **Host-only** rather than Bridged; VMware documents Host-only as a private network contained within the host ([Host-only networking](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/configuring-host-only-networking.html), [networking modes](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/understanding-common-networking-configurations.html)).
4. Take a clean snapshot before starting the lab.

**The lab itself needs no network adapter or internet connection.** The local copy uses Linux loopback (`127.0.0.1`) for the plant, guard, dashboards, and demonstrations. For the safest setup, disconnect the VM network adapter after installation and dependency setup. Run the browser inside Ubuntu, not on the host computer.

## 3. Put the repository files in the VM

While the VM is temporarily connected by NAT for setup, install the basic Ubuntu tools needed for Python virtual environments and Git:

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
```

Complete any repository download and Python dependency installation during this temporary setup window. Then shut down the VM and disconnect its virtual network adapter before running the lab. If you already received the files through an instructor-approved archive, Git is optional.

The GitHub repository is currently **private**. Students need access granted by the repository owner, or an instructor-provided approved archive. Do not share passwords, access tokens, or credentials with classmates. If authorized access is available, clone the repo inside Ubuntu while the VM has temporary NAT access:

```bash
git clone https://github.com/icdfa/ACICP302ICS-Network-Security-and-Attacks.git
```

Use the instructor-approved method to copy the repository or ZIP into the Ubuntu guest. If you use a temporary VMware/VirtualBox shared folder to transfer files, copy the files into the guest’s home directory and then unmount/disable the shared folder before running the lab.

In a terminal inside Ubuntu, move to the repository’s safe copy (adjust only the repository’s parent directory if it is stored elsewhere):

```bash
cd ~/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/local-linux
```

The `local-linux/` folder contains its own `plant_sim/` directory and its own `requirements.txt`. The original supplied project remains one level above, unchanged. **Use only `local-linux/plant_sim` for the student exercises.**

## 4. Install Python dependencies in a virtual environment

Check Python and create a project-local environment:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

The copied local requirements include `pymodbus` and Flask, both needed by this version of the lab. Do not use `sudo pip`, install packages globally, or remove the virtual environment while services are running.

If pip needs internet access, use NAT only temporarily for this installation, then shut down the VM and disconnect the virtual adapter before running the demonstrations. If course rules prohibit package downloads, ask the instructor for an approved offline wheelhouse.

## 5. Verify the local-only copy

Before launching anything, from the `local-linux` folder run:

```bash
cd ~/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/local-linux
grep -R -nE '192\.168\.2\.139|0\.0\.0\.0' plant_sim || true
```

For this safe copy, the command should produce **no matching output**. It is a check only; do not edit the files to make the check pass. If it reports either address, stop and notify the instructor. The original copy in the parent folder is expected to contain those addresses and must not be used for the student run.

The lab uses these local-only services:

| Component | Local address/port |
|---|---|
| Simulated plant, direct Modbus path | `127.0.0.1:5020` |
| Validation guard Modbus path | `127.0.0.1:5021` |
| Direct dashboard | <http://127.0.0.1:8080> |
| Guarded dashboard | <http://127.0.0.1:8081> |

The dashboards are development interfaces without login. They bind to loopback in the local copy, so open them in a browser **inside the Ubuntu guest**. Do not add port forwarding to view them from the host.

## 6. Start the simulation

Keep the virtual environment active. Open four terminals inside the Ubuntu VM. In each terminal, run:

```bash
cd ~/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/local-linux
source .venv/bin/activate
cd plant_sim
```

Then start one program in each terminal, in order:

| Terminal | Command | Expected behavior |
|---|---|---|
| 1 | `python3 plant.py` | Simulated process starts on loopback port 5020 and logs readings about once a second. |
| 2 | `python3 guard.py` | Guard starts on loopback port 5021 and forwards accepted writes to the local plant. |
| 3 | `python3 dashboard.py` | Direct-path dashboard starts on loopback port 8080. |
| 4 | `python3 dashboard_guarded.py` | Guarded dashboard starts on loopback port 8081 with a block log. |

Open these in the Ubuntu guest's browser:

- Direct view: <http://127.0.0.1:8080>
- Guarded view: <http://127.0.0.1:8081>

Expected initial readings are approximately 67.0 °C, 34.0 bar, and 90.0 Nm³/h. Register values may move slightly as the simulator runs.

The guarded dashboard in the original archive has an “AI protection active” label. In the safe local copy, that label is corrected to “rule-based protection active”: the guard uses fixed rules and does not contain an AI model.

## 7. Record a baseline

Before running a demonstration:

1. Record the VM name, date/time, the fact that the lab is running inside Ubuntu, and that the scripts are the `local-linux/` copy.
2. Confirm the no-match check passed and that the VM network adapter is disconnected (or instructor-approved Host-only, never Bridged).
3. Confirm both dashboards show live values.
4. Take a screenshot of each dashboard and note the initial readings.
5. Keep the four service terminals running while you use a fifth terminal for one demonstration at a time.

## 8. Run the guided demonstrations

From the fifth terminal, activate the same virtual environment and change to `local-linux/plant_sim`:

```bash
cd ~/ACICP302ICS-Network-Security-and-Attacks/labs/ot-security/local-linux
source .venv/bin/activate
cd plant_sim
```

Run only the provided values and request rates. Compare port **5020** (direct path) with port **5021** (guarded path). Each pair below should be run one command at a time:

| Script | What it demonstrates | Commands |
|---|---|---|
| `attack_hold.py` | Repeated request for 95.0 bar, outside the simulated range, for about eight seconds | `python3 attack_hold.py 5020` then `python3 attack_hold.py 5021` |
| `false_data_attack.py` | Six batches of out-of-range temperature, pressure, and flow values | `python3 false_data_attack.py 5020` then `python3 false_data_attack.py 5021` |
| `slow_drift_attack.py` | Twelve incremental pressure changes over about 24 seconds | `python3 slow_drift_attack.py 5020` then `python3 slow_drift_attack.py 5021` |
| `replay_attack.py` | Repeats the same pressure write three times | `python3 replay_attack.py 5020` then `python3 replay_attack.py 5021` |
| `recon_scan.py` | Reads a limited range of holding registers | `python3 recon_scan.py 5020` then `python3 recon_scan.py 5021` |
| `dos_attack.py` | Fixed burst of 200 read requests using 10 threads | `python3 dos_attack.py 5020` then `python3 dos_attack.py 5021` |

The local copy hardcodes the destination to `127.0.0.1`; the port argument selects only the direct or guarded simulator port. The request flood is small but still creates load: run it only against this local simulator, one time at a time, and do not increase its duration, rate, or thread count.

After each run, record the script output, dashboard observations, and any relevant `plant_sim/events.jsonl` entries. Results can vary with timing; record what actually happened rather than forcing a particular result.

## 9. Analysis questions

Answer in your own words:

1. Which requested values did the direct path accept, and which did the guard reject?
2. Which validation mechanism is relevant: absolute range, step size, or rolling-baseline drift?
3. Did the dashboard, script output, and event log agree? Describe timing differences.
4. What does the limited register read reveal in this model, and why would the same action still need explicit authorization on any real system?
5. What does this guard not address (for example, client identity, authentication, availability, correlated process values, or bypass through a direct path)?
6. What additional controls would a real critical-infrastructure operator consider through formal engineering and security review?

Do not claim this lab guard makes any real process safe.

## 10. Evidence and cleanup

Use the course evidence-log, topology/register-map, risk-register, and final-report templates. Include:

- [Evidence log](../../docs/templates/evidence-log-template.md)
- [Topology and register map](../../docs/templates/topology-and-register-map-template.md)
- [Risk register](../../docs/templates/risk-register-template.csv)
- [Final report](../../docs/templates/final-report-template.md)

- A simple architecture and register map.
- Baseline and comparison screenshots.
- A results table with script, port, requested action, observed result, timestamp, and guard event.
- A short analysis of the checks, limitations, and residual risks.
- Confirmation that all processes were stopped and the VM was restored/cleaned up.

Store evidence only in the instructor-approved submission location. Do not commit `.venv`, generated logs, captures, screenshots, reports, or personal/site data to the shared source repository.

When finished:

1. Stop all four services with **Ctrl+C** in their terminals.
2. Wait for each demonstration script to finish; do not leave processes running.
3. Deactivate the environment with `deactivate`.
4. Handle `plant_sim/events.jsonl` according to the instructor's evidence policy.
5. Revert to the clean VM snapshot if required and leave the VM's network adapter disconnected.

If a dashboard says disconnected, verify the plant was started first and the guard second. If the safety check finds a non-loopback address, stop; do not edit targets or run the original scripts.

## Official VM networking references

- [VirtualBox User Manual — Virtual Networking](https://www.virtualbox.org/manual/ch06.html)
- [VMware Workstation — Host-Only Networking](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/configuring-host-only-networking.html)
- [VMware Workstation — Common Networking Configurations](https://techdocs.broadcom.com/us/en/vmware-cis/desktop-hypervisors/workstation-pro/17-0/using-vmware-workstation-pro/configuring-network-connections/understanding-common-networking-configurations.html)
