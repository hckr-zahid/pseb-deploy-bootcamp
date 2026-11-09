# VMware Multi-Zone Cyber Range Architecture Reference

**Host Environment:** VMware Workstation Pro 17.x on Windows 10 Home (Intel Core i7-6700, 16 GB RAM)  
**Primary Gateway & Inter-VLAN Router:** pfSense 2.6.0 (UFS, 512 MB RAM)  
**Airgap Isolation:** Floating rule strictly drops all traffic to physical host home subnet (`192.168.0.0/24`).  
**Universal Credentials:** `labadmin` / `Lab2026!` (Domain: `sec\labadmin`) | pfSense WebGUI: `admin` / `Lab2026!`

---

## Network Segmentation & Interface Mapping

| Interface | Network Name | Virtual Switch | Subnet CIDR | Gateway IP | Role / Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **em0** | WAN | VMnet8 (NAT) | `192.168.80.0/24` | `192.168.80.2` | Controlled Internet egress / updates (`192.168.80.128`) |
| **em1** | ENTERPRISELAN | VMnet2 | `10.50.10.0/24` | `10.50.10.1` | Active Directory Domain, Workstations, Internal Services |
| **em2** | OFFENSIVE | VMnet3 | `10.50.20.0/24` | `10.50.20.1` | Red Team platforms, Vulnerable Targets, Assessment Tools |
| **em3** | SOC | VMnet4 | `10.50.30.0/24` | `10.50.30.1` | Security Monitoring, Wazuh SIEM, Indexer & Dashboard |
| **em4** | MANAGEMENT | VMnet6 | `10.50.50.0/24` | `10.50.50.1` | Out-of-Band Admin, pfSense GUI Management |
| **—** | AIRGAP SANDBOX| VMnet5 | `10.50.40.0/24` | *None* | Completely isolated malware detonation (Zero Routing) |

---

## Host Asset Inventory by Subnet

### 1. Enterprise LAN (`10.50.10.0/24` — VMnet2)
* **DC01 (`10.50.10.10`):** Windows Server 2022 Datacenter. Active Directory Domain Controller (`sec.lab`), DNS, Sysmon, Wazuh Agent.
* **WIN10VM (`10.50.10.21`):** Windows 10 Pro 64-bit. Domain workstation, Sysmon, Wazuh Agent, Client-side target.
* **WIN11-ENT (`10.50.10.22`):** Windows 11 Enterprise 64-bit. Modern workstation target, Sysmon, Wazuh Agent.
* **Windows 7 (`10.50.10.23`):** Windows 7 SP1 x64. Legacy target (EternalBlue MS17-010, SMBv1, unpatched RDP).

### 2. Offensive Zone (`10.50.20.0/24` — VMnet3)
* **Kali Linux (`10.50.20.10`):** Primary offensive security platform, Metasploit Framework, Nmap, Burp Suite, Python servers.
* **BlackArch Linux (`10.50.20.12`):** Secondary specialized security arsenal.
* **Ubuntu Target (`10.50.20.20`):** Dockerized application server:
  * Port `8080`: Damn Vulnerable Web App (DVWA)
  * Port `3000`: OWASP Juice Shop
  * Port `8000`: Mobile Security Framework (MobSF)
* **Metasploitable 2 (`10.50.20.30`):** Vulnerable Linux daemon server (vsftpd 2.3.4, Samba 3.0.20, bindshell, weak SSH).
* **Android 8.1 (`10.50.20.50`):** Mobile assessment target with rooted ADB listener on TCP port `5555`.

### 3. SOC & Security Telemetry (`10.50.30.0/24` — VMnet4)
* **Wazuh-SIEM (`10.50.30.10`):** Centralized SIEM platform (Wazuh Manager, Wazuh Indexer, OpenSearch Dashboard on HTTPS `443`).

### 4. Airgapped Malware Detonation Sandbox (`10.50.40.0/24` — VMnet5)
* **REMnux (`10.50.40.10`):** Linux reverse-engineering gateway running INetSim (simulated DNS, HTTP, SMTP).
* **FlareVM (`10.50.40.11`):** Windows malware detonation box with Defender disabled and dynamic debugging suites.

---

## Active Operational Profiles

* **Profile A (Active Directory Assessment):** Kali (`10.50.20.10`) $\rightarrow$ DC01 (`10.50.10.10`) + Domain Workstations.
* **Profile B (Network Service VA/PT):** Kali (`10.50.20.10`) $\rightarrow$ Metasploitable 2 (`10.50.20.30`).
* **Profile C (Web Application Pentest — CURRENT):** Kali (`10.50.20.10`) $\rightarrow$ Ubuntu Target (`10.50.20.20:8080` DVWA / `3000` Juice Shop).
* **Profile D (Client-Side & Endpoint):** Kali (`10.50.20.10`) $\leftrightarrow$ WIN10VM (`10.50.10.21`) across pfSense inter-VLAN.
* **Profile E (Malware Detonation):** FlareVM (`10.50.40.11`) $\leftrightarrow$ REMnux (`10.50.40.10`) isolated on VMnet5.
