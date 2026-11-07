# Day 3 Bootcamp VA/PT Evidence & Screenshot Tracker

| Finding / Step | Vulnerability / Activity | Target / Port | Evidence Log | Screenshot File | Result / Impact | Status |
|:---:|:---|:---|:---|:---|:---|:---:|
| **Step 1** | Network Isolation & IP Verification | `10.50.20.10` / `10.50.20.30` | `logs/01_network_verification.txt` | `01_network_verification.png` | Isolated lab verified (`exit=1`) |  Completed |
| **Step 2** | Full Service & OS Reconnaissance | `10.50.20.30` (All TCP) | `logs/02_nmap_services.txt` | `02_nmap_service_scan_part1.jpg`<br>`02_nmap_service_scan_part2.jpg`<br>`02_nmap_service_scan_part3.jpg` | 20+ open ports identified |  Completed |
| **Finding 1** | vsftpd 2.3.4 Backdoor RCE (CVE-2011-2523) | `10.50.20.30:21` (FTP) | `logs/03_msf_vsftpd_exploit.txt`<br>`logs/04_post_exploit_root_proof.txt` | `03_msf_vsftpd_exploit_session.jpg`<br>`04_post_exploit_root_proof.png` | **Root Remote Code Execution** (Meterpreter) |  Completed |
| **Post-Exploit** | Post-Exploitation Persistence & Shadow Access | `10.50.20.30` (Host) | `logs/05_post_exploitation.txt` | `05_post_exploitation_persistence.png` | `/etc/shadow` dump + Cron backdoor demonstration |  Completed |
| **Finding 2** | Weak Default Credentials & Privilege Escalation | `10.50.20.30:22` (SSH) | `evidence/06_ssh_default_credentials_login.jpg` | `06_ssh_default_credentials_login.jpg`<br>`06_ssh_sudo_root_proof.png` | Sudo takeover to **root** via `msfadmin:msfadmin` |  Completed |
| **Finding 3** | Unauthenticated Root Listener (`bindshell`) | `10.50.20.30:1524` | Shell session log | `07_bindshell_port1524_root.png` | Direct unauthenticated **root** shell via netcat |  Completed |
| **Finding 4** | Samba 3.0.20 usermap_script RCE (CVE-2007-2447) | `10.50.20.30:139,445` | `logs/08_msf_samba_root_shell.txt` | `08_msf_samba_root_shell.png` | **Root Remote Code Execution** via Metasploit |  Completed |
| **Task 1 (20%)** | GVM / OpenVAS vs Manual Scan Comparison | Analysis Document | `s07-report/gvm_comparison.md` | Analytical Tables & Benchmarks | ⏳ In Progress |
| **Task 2 (20%)** | Metasploit Step-by-Step Exploitation Write-up | Full Technical Narrative | Embedded in Final Report | Shell & Payload Evidence | ⏳ In Progress |
| **Task 3 (60%)** | Formal VA/PT Deliverable Report (Template 6) | Client Deliverable | `s07-report/VA_PT_Report.pdf` | Complete Executive & Technical Report | ⏳ In Progress |
