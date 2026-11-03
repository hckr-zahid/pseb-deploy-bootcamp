# SC-500 | Security Operations & Cybersecurity Learning Portfolio

<p align="center">
  <img src="https://img.shields.io/badge/Program-PSEB%20DEPLOY-blue?style=for-the-badge" alt="PSEB DEPLOY">
  <img src="https://img.shields.io/badge/Certification-SC--500-0078D4?style=for-the-badge" alt="SC-500">
  <img src="https://img.shields.io/badge/Duration-3%20Months-success?style=for-the-badge" alt="Three Months">
  <img src="https://img.shields.io/badge/Status-In%20Progress-orange?style=for-the-badge" alt="In Progress">
</p>

<p align="center">
  <b>Learn • Practice • Document • Build • Improve</b>
</p>

Welcome to my **three-month cybersecurity learning journey**, documented through practical labs, technical reports, projects, research, and hands-on exercises.

This repository serves as my central portfolio for the **SC-500 Certification course**, undertaken under the **PSEB DEPLOY AI BootCamps Initiative**.

My objective is to develop practical cybersecurity knowledge, strengthen technical problem-solving skills, and build a well-documented portfolio demonstrating what I learn throughout the program.

---

## 📌 Program Overview

| Detail | Information |
|---|---|
| Program | PSEB DEPLOY AI BootCamps Initiative |
| Certification Track | SC-500 |
| Learning Duration | 3 Months |
| Repository Type | Learning Portfolio & Practical Documentation |
| Primary Focus | Cybersecurity |
| Learning Approach | Hands-on Labs, Reports, Projects & Research |
| Current Status | In Progress |

**Program Reference:** [PSEB DEPLOY Bootcamp](https://github.com/hckr-zahid/pseb-deploy-bootcamp)

---

## 🎯 Learning Objectives

Throughout this journey, I aim to:

- Develop a strong understanding of cybersecurity concepts and security practices.
- Perform practical security assessments in controlled lab environments.
- Understand network discovery, scanning, enumeration, and vulnerability assessment.
- Identify security weaknesses and understand their potential impact.
- Work with cybersecurity tools and document their results.
- Understand vulnerability severity, risk assessment, and remediation.
- Develop technical reporting and evidence-collection skills.
- Complete practical projects that demonstrate applied knowledge.
- Build a professional GitHub portfolio of my learning progress.

---

## 🗂️ Repository Contents

This repository will grow throughout the three-month program. It will contain learning materials and practical work organized into separate modules.

| Directory | Purpose |
|---|---|
| `Labs/` | Hands-on cybersecurity exercises |
| `Reports/` | Lab reports and technical documentation |
| `Projects/` | Practical and independent projects |
| `Research/` | Security research, case studies, and analysis |
| `Scripts/` | Useful scripts and automation |
| `Screenshots/` | Supporting screenshots and visual evidence |
| `Resources/` | References, notes, and learning resources |

*The structure may evolve as new course modules and projects are added.*

---

## 📚 Learning Progress

<details open>
<summary><b>Phase 01 — Foundations & Practical Security Labs</b></summary>

This phase focuses on understanding security fundamentals, working with lab environments, and developing practical assessment skills.

| Module | Topic | Status |
|---|---|---|
| S06 | Network Scanning and Vulnerability Assessment | ✅ Completed |
| Future Modules | Additional course labs and exercises | ⏳ Upcoming |

</details>

<details>
<summary><b>Phase 02 — Advanced Practical Exercises</b></summary>

Planned repository space for additional technical exercises, security analysis, and practical assignments as covered by the course.

</details>

<details>
<summary><b>Phase 03 — Projects & Portfolio Development</b></summary>

Planned repository space for larger practical projects, consolidated reports, research, and final learning outcomes.

</details>

---

## 🧪 Completed Lab: S06 — Network Scanning and Vulnerability Assessment

<kbd>LAB 01</kbd> <kbd>COMPLETED</kbd>

My first documented practical lab focuses on network discovery, service enumeration, vulnerability identification, and security assessment.

**Lab environment:**

| Machine | IP Address | Role |
|---|---|---|
| Kali Linux | `192.168.199.128` | Attacker / Assessment Machine |
| Metasploitable 2 | `192.168.199.129` | Vulnerable Target |

**Tools used:**
- Kali Linux
- Nmap
- FTP client
- cURL
- Terminal-based network utilities

### Key Activities

1. Verified connectivity between the lab machines.
2. Performed network scanning using Nmap.
3. Identified running services and their versions.
4. Investigated the vsftpd 2.3.4 backdoor vulnerability.
5. Examined PHP information disclosure.
6. Tested anonymous FTP authentication.
7. Documented findings and supporting evidence.
8. Researched CVSS scoring and the historical vsftpd supply-chain incident.

### Security Findings

| Finding | Description | Assessment |
|---|---|---|
| vsftpd 2.3.4 Backdoor | Nmap detection of the known backdoor vulnerability (CVE-2011-2523) | Critical |
| PHP Information Disclosure | Publicly accessible PHP information page exposing configuration details | Medium |
| Anonymous FTP Access | Anonymous FTP authentication accepted by the target | Security Misconfiguration |

**Important:** Severity labels are preliminary lab assessments. The actual risk depends on the affected system, exposure, and business context.

### Evidence Preview

**1. Initial Nmap Scan**

![Initial Nmap Scan](evidence/initial-nmap-scan.png)

**2. vsftpd Backdoor Detection**

![vsftpd Backdoor Detection](evidence/vsftpd-backdoor.png)

**3. PHP Information Disclosure**

![PHP Information Disclosure](evidence/phpinfo-page.png)

**4. Anonymous FTP Authentication**

![Anonymous FTP Authentication](evidence/anonymous-ftp.png)

### Additional Lab Documentation

- [Initial Nmap Results](evidence/initial-nmap.nmap)
- [Nmap XML Output](evidence/initial-nmap.xml)
- [Nmap Grepable Output](evidence/initial-nmap.gnmap)
- [vsftpd Backdoor Check](evidence/vsftpd-backdoor-check.txt)
- [PHP Response Headers](evidence/phpinfo-headers.txt)
- [PHP Information Page HTML](evidence/phpinfo.html)
- [Anonymous FTP Session](evidence/anonymous-ftp-session.txt)
- [CVSS Analysis — Task B3](evidence/task-b3-cvss-notes.md)
- [vsftpd Supply-Chain Research — Task B6](evidence/task-b6-vsftpd-supply-chain.md)

All testing was performed against the intentionally vulnerable Metasploitable 2 machine in an isolated lab environment.

---

## 🧰 Tools & Technologies

Tools used or planned for practical learning, depending on the course modules:

| Category | Tools |
|---|---|
| Operating Systems | Kali Linux, Linux |
| Network Scanning | Nmap |
| Network Utilities | Ping, FTP, cURL |
| Vulnerability Assessment | Nmap NSE and related assessment tools |
| Documentation | Markdown, Git, GitHub |
| Virtualization | VirtualBox / VMware |
| Security Research | CVE, CVSS, NVD |

This list will be updated as I work with additional tools.

---

## 📁 Repository Structure

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

The S06 evidence currently exists in the `evidence/` directory alongside this repository's main README. As the repository grows, I may organize individual labs into their own folders.

---

## 📝 Documentation Standards

To keep this portfolio consistent and easy to review, each practical lab or project will aim to include:

- **Objective:** What the exercise is intended to achieve.
- **Environment:** Systems, tools, and configurations used.
- **Methodology:** Steps followed during the exercise.
- **Commands:** Relevant commands and configurations.
- **Findings:** Observations and identified security issues.
- **Evidence:** Screenshots, logs, and output files.
- **Analysis:** Technical explanation and risk assessment.
- **Recommendations:** Appropriate mitigation or remediation steps.
- **References:** Official documentation and reliable sources.

---

## 🔐 Responsible Use & Disclaimer

All security testing and practical exercises documented in this repository are intended for **educational purposes and authorized environments only**.

- Testing is performed on systems I own or have explicit permission to assess.
- Vulnerable machines are used in isolated lab environments.
- No unauthorized access or testing against third-party systems is intended.
- Security findings are documented for learning, analysis, and defensive improvement.

**Please do not use the techniques documented here against systems without proper authorization.**

---

## 📈 Learning Journey

This repository will be updated throughout the three-month course as I complete new labs, assignments, reports, and projects.

My goal is not simply to complete exercises, but to understand the underlying concepts, document the process, analyze the results, and build practical skills.

<p align="center">
  <b>Every Lab Is a Lesson. Every Project Is Progress.</b>
</p>

---

## 🔗 Useful Links

- [PSEB DEPLOY Bootcamp Repository](https://github.com/hckr-zahid/pseb-deploy-bootcamp)
- [National Vulnerability Database (NVD)](https://nvd.nist.gov/)
- [Nmap Official Documentation](https://nmap.org/book/man.html)
- [FIRST CVSS Documentation](https://www.first.org/cvss/)
- [GitHub Markdown Guide](https://guides.github.com/features/mastering-markdown/)

---

<p align="center">
  <i>Documenting my journey from learning cybersecurity concepts to applying them through practical projects.</i>
</p>
