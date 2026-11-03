# SC-500 | Pakistan Software Export Board (PSEB)

<p align="center">
  <img src="https://img.shields.io/badge/PROGRAM-PSEB%20DEPLOY-1F4B99?style=for-the-badge" alt="PSEB DEPLOY">
  <img src="https://img.shields.io/badge/TRAINING-SC--500-0078D4?style=for-the-badge" alt="SC-500">
  <img src="https://img.shields.io/badge/DURATION-3%20MONTHS-444444?style=for-the-badge" alt="Three Months">
  <img src="https://img.shields.io/badge/STATUS-IN%20PROGRESS-D97706?style=for-the-badge" alt="In Progress">
</p>

<p align="center">
  <strong>Cybersecurity Training, Practical Labs, Technical Reports & Projects</strong>
</p>

<p align="center">
  <a href="https://github.com/hckr-zahid/pseb-deploy-bootcamp">PSEB DEPLOY BootCamp Repository</a>
  &nbsp;|&nbsp;
  <a href="https://nvd.nist.gov/">National Vulnerability Database</a>
  &nbsp;|&nbsp;
  <a href="https://www.first.org/cvss/">CVSS Documentation</a>
</p>

---

## About This Repository

This repository documents my three-month training journey under the **SC-500 program**, conducted through the **Pakistan Software Export Board (PSEB) DEPLOY AI BootCamps Initiative**.

It serves as a centralized technical record of the knowledge, practical exercises, security assessments, research activities, and projects completed throughout the training program.

The repository is intended to demonstrate practical learning through structured documentation, reproducible lab work, technical analysis, and supporting evidence.

The primary focus is to strengthen cybersecurity knowledge, develop hands-on technical skills, and apply security concepts through practical exercises and projects.

---

## Program Overview

<table>
  <tr>
    <td><strong>Program</strong></td>
    <td>PSEB DEPLOY AI BootCamps Initiative</td>
  </tr>
  <tr>
    <td><strong>Organization</strong></td>
    <td>Pakistan Software Export Board (PSEB)</td>
  </tr>
  <tr>
    <td><strong>Training Track</strong></td>
    <td>SC-500</td>
  </tr>
  <tr>
    <td><strong>Duration</strong></td>
    <td>Three Months</td>
  </tr>
  <tr>
    <td><strong>Repository Type</strong></td>
    <td>Technical Learning & Practical Documentation</td>
  </tr>
  <tr>
    <td><strong>Primary Domain</strong></td>
    <td>Cybersecurity</td>
  </tr>
  <tr>
    <td><strong>Current Status</strong></td>
    <td>In Progress</td>
  </tr>
</table>

---

## Learning Objectives

Throughout this program, the focus is on developing practical capabilities in cybersecurity through structured learning and hands-on implementation.

Key objectives include:

- Understand cybersecurity principles, concepts, and security practices.
- Perform network discovery, scanning, enumeration, and vulnerability assessments.
- Identify security weaknesses and evaluate their potential impact.
- Work with industry-relevant cybersecurity tools and technologies.
- Understand vulnerability classification, CVSS scoring, and risk assessment.
- Analyze security configurations and common vulnerabilities.
- Develop technical documentation and professional security reports.
- Perform practical exercises in controlled and authorized lab environments.
- Build projects that demonstrate the application of learned concepts.

---

## Training Progress

The repository is organized by individual training sessions. Each session has its own documentation, scripts, and supporting evidence.

<table>
  <thead>
    <tr>
      <th>Session</th>
      <th>Topic</th>
      <th>Status</th>
      <th>Documentation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>S01</td>
      <td>To be updated</td>
      <td>Pending</td>
      <td>—</td>
    </tr>
    <tr>
      <td>S02</td>
      <td>To be updated</td>
      <td>Pending</td>
      <td>—</td>
    </tr>
    <tr>
      <td>S03</td>
      <td>To be updated</td>
      <td>Pending</td>
      <td>—</td>
    </tr>
    <tr>
      <td>S04</td>
      <td>To be updated</td>
      <td>Pending</td>
      <td>—</td>
    </tr>
    <tr>
      <td>S05</td>
      <td>To be updated</td>
      <td>Pending</td>
      <td>—</td>
    </tr>
    <tr>
      <td>S06</td>
      <td>Network Scanning and Vulnerability Assessment</td>
      <td><strong>Completed</strong></td>
      <td><a href="s06-scanning/README.md">View Session</a></td>
    </tr>
    <tr>
      <td>S07 onwards</td>
      <td>To be updated</td>
      <td>Upcoming</td>
      <td>—</td>
    </tr>
  </tbody>
</table>

*Session topics and progress will be updated as the training continues.*

---

## Completed Practical Work

### S06 — Network Scanning and Vulnerability Assessment

<p>
  <img src="https://img.shields.io/badge/SESSION-S06-0078D4?style=flat-square" alt="Session S06">
  <img src="https://img.shields.io/badge/STATUS-COMPLETED-238636?style=flat-square" alt="Completed">
</p>

The S06 practical lab focused on network discovery, service enumeration, vulnerability identification, and security assessment using Kali Linux and Metasploitable 2.

#### Lab Environment

| Machine | IP Address | Role |
|---|---|---|
| Kali Linux | `192.168.199.128` | Assessment Machine |
| Metasploitable 2 | `192.168.199.129` | Vulnerable Target |

#### Tools Used

- Kali Linux
- Nmap
- FTP Client
- cURL
- Linux Terminal Utilities

#### Key Activities

1. Verified connectivity between the lab machines.
2. Performed network scanning using Nmap.
3. Identified running services and service versions.
4. Investigated the vsftpd 2.3.4 backdoor vulnerability.
5. Examined PHP information disclosure.
6. Tested anonymous FTP authentication.
7. Collected screenshots, logs, and scan outputs.
8. Researched CVSS scoring and the historical vsftpd supply-chain incident.

#### Security Findings

| Finding | Description | Preliminary Assessment |
|---|---|---|
| vsftpd 2.3.4 Backdoor | Detection of the known backdoor vulnerability, CVE-2011-2523 | Critical |
| PHP Information Disclosure | Publicly accessible PHP information page exposing configuration details | Medium |
| Anonymous FTP Access | Anonymous FTP authentication accepted by the target | Security Misconfiguration |

*Severity labels are preliminary lab assessments. Actual risk depends on system exposure, business context, and the security impact.*

#### Evidence

**Initial Network Scan**

<p align="center">
  <img src="s06-scanning/evidence/initial-nmap-scan.png" alt="Initial Nmap Scan" width="90%">
</p>

**vsftpd Backdoor Detection**

<p align="center">
  <img src="s06-scanning/evidence/vsftpd-backdoor.png" alt="vsftpd Backdoor Detection" width="90%">
</p>

**PHP Information Disclosure**

<p align="center">
  <img src="s06-scanning/evidence/phpinfo-page.png" alt="PHP Information Disclosure" width="90%">
</p>

**Anonymous FTP Authentication**

<p align="center">
  <img src="s06-scanning/evidence/anonymous-ftp.png" alt="Anonymous FTP Authentication" width="90%">
</p>

#### Additional Documentation

| Evidence File | Description |
|---|---|
| [Initial Nmap Results](s06-scanning/evidence/initial-nmap.nmap) | Human-readable scan results |
| [Nmap XML Output](s06-scanning/evidence/initial-nmap.xml) | Structured scan output |
| [Nmap Grepable Output](s06-scanning/evidence/initial-nmap.gnmap) | Grepable scan output |
| [vsftpd Backdoor Check](s06-scanning/evidence/vsftpd-backdoor-check.txt) | Vulnerability detection output |
| [PHP Response Headers](s06-scanning/evidence/phpinfo-headers.txt) | HTTP response headers |
| [PHP Information Page](s06-scanning/evidence/phpinfo.html) | Captured PHP information page |
| [Anonymous FTP Session](s06-scanning/evidence/anonymous-ftp-session.txt) | FTP authentication and session evidence |
| [CVSS Analysis — Task B3](s06-scanning/evidence/task-b3-cvss-notes.md) | Vulnerability severity analysis |
| [vsftpd Supply-Chain Research — Task B6](s06-scanning/evidence/task-b6-vsftpd-supply-chain.md) | Historical supply-chain incident research |

All S06 testing was performed against an intentionally vulnerable Metasploitable 2 machine in an isolated lab environment.

<a href="s06-scanning/README.md"><strong>View Complete S06 Lab Documentation</strong></a>

---

## Repository Structure

Each training session follows a consistent directory structure to keep documentation, scripts, and evidence organized.

```text
pseb-deploy-bootcamp/
│
├── README.md
│
├── s01/
│   ├── Scripts/
│   ├── README.md
│   └── evidence/
│
├── s02/
│   ├── Scripts/
│   ├── README.md
│   └── evidence/
│
├── s03/
│   ├── Scripts/
│   ├── README.md
│   └── evidence/
│
├── s04/
│   ├── Scripts/
│   ├── README.md
│   └── evidence/
│
├── s05/
│   ├── Scripts/
│   ├── README.md
│   └── evidence/
│
├── s06/
│   ├── Scripts/
│   ├── README.md
│   └── evidence/
│
└── ...
```

### Directory Guidelines

| Directory / File | Purpose |
|---|---|
| `Scripts/` | Scripts, commands, configuration files, and automation developed during the session |
| `README.md` | Session overview, objectives, methodology, findings, and conclusion |
| `evidence/` | Screenshots, logs, scan outputs, reports, and supporting evidence |

This structure will be repeated for each session throughout the training program.

---

## Tools & Technologies

The following tools and technologies are used or may be introduced during practical exercises, depending on the course content.

<table>
  <thead>
    <tr>
      <th>Category</th>
      <th>Tools & Technologies</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Operating Systems</td>
      <td>Kali Linux, Linux</td>
    </tr>
    <tr>
      <td>Network Scanning</td>
      <td>Nmap</td>
    </tr>
    <tr>
      <td>Network Utilities</td>
      <td>Ping, FTP, cURL</td>
    </tr>
    <tr>
      <td>Vulnerability Assessment</td>
      <td>Nmap NSE and related assessment tools</td>
    </tr>
    <tr>
      <td>Virtualization</td>
      <td>VirtualBox, VMware</td>
    </tr>
    <tr>
      <td>Documentation & Version Control</td>
      <td>Markdown, Git, GitHub</td>
    </tr>
    <tr>
      <td>Security Research</td>
      <td>CVE, CVSS, NVD</td>
    </tr>
  </tbody>
</table>

The tools list will be expanded as additional technologies are introduced and used.

---

## Documentation Standards

Each session will follow a consistent documentation approach to ensure clarity, reproducibility, and professional presentation.

Where applicable, session documentation will include:

- **Objectives:** Purpose and expected learning outcomes.
- **Environment:** Systems, tools, and configurations used.
- **Methodology:** Steps and procedures followed.
- **Scripts and Commands:** Relevant commands, scripts, and configurations.
- **Findings:** Observed results and identified security issues.
- **Evidence:** Screenshots, logs, and supporting files.
- **Analysis:** Technical explanations and risk assessments.
- **Recommendations:** Suggested mitigation and remediation measures.
- **References:** Official documentation and reliable technical sources.

---

## Responsible Use & Disclaimer

All security testing and practical exercises documented in this repository are conducted for educational purposes in authorized environments.

- Testing is limited to systems owned by me or systems for which explicit authorization has been granted.
- Vulnerable machines are used in isolated laboratory environments.
- No unauthorized access or testing against third-party systems is intended.
- Security findings are documented for educational analysis and defensive improvement.

The information and techniques documented here must not be used against systems without proper authorization.

---

## Learning Journey

This repository will be continuously updated throughout the three-month training program.

Each session will contribute to a growing collection of practical exercises, scripts, technical reports, security research, and projects.

The objective is to build a structured record of practical cybersecurity experience and demonstrate the ability to understand, investigate, document, and analyze security challenges.

---

## References & Learning Resources

- [PSEB DEPLOY BootCamp Repository](https://github.com/hckr-zahid/pseb-deploy-bootcamp)
- [Pakistan Software Export Board](https://pseb.org.pk/)
- [National Vulnerability Database](https://nvd.nist.gov/)
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [FIRST CVSS Documentation](https://www.first.org/cvss/)
- [GitHub Markdown Documentation](https://docs.github.com/en/get-started/writing-on-github)

---

<p align="center">
  <strong>SC-500 | Pakistan Software Export Board</strong>
  <br>
  <span>Cybersecurity Training & Practical Documentation</span>
  <br><br>
  <sub>Learning through practice. Building through projects. Improving through documentation.</sub>
</p>
