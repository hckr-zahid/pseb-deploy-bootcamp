## Task B6 — vsftpd Supply-Chain Compromise

### What happened?

In 2011, the official vsftpd download site was compromised and its `vsftpd-2.3.4.tar.gz` source archive was replaced with a modified version containing a malicious backdoor. The compromised archive was available for approximately three days, from June 30 or July 1 until July 3, 2011. This was a supply-chain attack because the attacker tampered with the software distribution process rather than exploiting a normal programming flaw in the legitimate release.

The backdoor was designed to activate when an FTP login username contained the characters `:)`. After activation, it opened a shell on TCP port 6200, potentially allowing an attacker to execute commands on the affected machine. The issue was assigned **CVE-2011-2523**.

### How was it discovered?

Mathias Kresin was credited as the first person to notice the suspicious archive. Chris Evans, the author of vsftpd, investigated and publicly warned users that the download had been compromised. One important indication was that the archive's detached GPG signature failed verification. A failed signature check means the downloaded file could not be authenticated as an unmodified release signed by the expected project key.

### Why is it relevant today?

This incident demonstrates that trusting a software name or download location is not enough. An attacker who compromises a software project's distribution site can potentially affect users who download and install its packages. Modern software projects depend on many external packages, repositories, build systems, and distribution services, so the same type of risk remains relevant.

To reduce this risk, organizations should verify digital signatures and checksums, download software from trusted sources, keep software updated, monitor unexpected network services, and maintain an inventory of installed software. The incident shows why software supply-chain security and software provenance are important parts of cybersecurity.

### References

- Chris Evans, *Alert: vsftpd download backdoored* (July 2011): https://scarybeastsecurity.blogspot.com/2011/07/alert-vsftpd-download-backdoored.html
- The Register, *Popular FTP package download tarball poisoned* (July 5, 2011): https://www.theregister.com/security/2011/07/05/popular_ftp_package_download_tarball_poisoned/1385024
- NIST National Vulnerability Database, *CVE-2011-2523*: https://nvd.nist.gov/vuln/detail/CVE-2011-2523
