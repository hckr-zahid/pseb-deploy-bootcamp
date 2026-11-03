## Task B3 — CVSS Metric Decoding: CVE-2011-2523

### Vulnerability
**vsftpd 2.3.4 Backdoor — CVE-2011-2523**

### CVSS 3.1 Vector

`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

| Metric | Value | My interpretation |
|---|---|---|
| Attack Vector (AV) | N | The attacker can reach the vulnerable FTP service through a network connection. |
| Attack Complexity (AC) | L | The attack does not require unusual conditions or complicated preparation. |
| Privileges Required (PR) | N | The attacker does not need an existing account or prior login privileges. |
| User Interaction (UI) | N | No action from another user is necessary for the attack. |
| Scope (S) | U | The consequences remain within the security authority of the affected system. |
| Confidentiality (C) | H | Successful exploitation can expose sensitive information on the system. |
| Integrity (I) | H | Successful exploitation can allow unauthorized modification of system data. |
| Availability (A) | H | Successful exploitation can interrupt services or make the system unavailable. |

### CVSS 2.0 Vector

`AV:N/AC:L/Au:N/C:C/I:C/A:C`

| Metric | Value | My interpretation |
|---|---|---|
| Access Vector (AV) | N | The attack can be launched over a network. |
| Access Complexity (AC) | L | The attack requires relatively few special conditions. |
| Authentication (Au) | N | No authentication is required before attempting the attack. |
| Confidentiality (C) | C | The attack can expose all information protected by the affected system. |
| Integrity (I) | C | The attack can allow extensive unauthorized changes. |
| Availability (A) | C | The attack can cause complete loss of service availability. |

### My Assessment

The vector describes a remotely reachable vulnerability that does not require prior authentication or user interaction. Its potential consequences affect confidentiality, integrity, and availability.

In my practical assessment, Nmap detected the vsftpd 2.3.4 backdoor and successfully executed the `id` command, returning `uid=0(root) gid=0(root)`. This demonstrates root-level command execution on the Metasploitable 2 target.

The published base scores are 9.8 under CVSS 3.1 and 10.0 under CVSS 2.0. The two versions use different metric systems, so their scores should not be treated as directly interchangeable.

### References
- https://nvd.nist.gov/vuln/detail/CVE-2011-2523
- https://www.first.org/cvss/v3.1/specification-document
- https://www.first.org/cvss/v2/guide
