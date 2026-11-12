import os
import sys
import io
from PIL import Image
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = r"c:\Users\JeemZa\.gemini\antigravity\scratch\pseb-deploy-bootcamp\s09-recon-and-upload"
EVIDENCE_DIR = os.path.join(BASE_DIR, "evidence")
OUTPUT_DOCX = os.path.join(BASE_DIR, "S09_Recon_and_Upload_Report.docx")

def set_cell_background(cell, hex_color):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E1", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:right w:val="none"/>
            <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def add_header_paragraph(doc, text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.bold = True
    run.font.name = "Arial"
    if level == 1:
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B) # Navy
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
    elif level == 2:
        run.font.size = Pt(13)
        run.font.color.rgb = RGBColor(0x02, 0x84, 0xC7) # Primary blue
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
    elif level == 3:
        run.font.size = Pt(11)
        run.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
    return p

def add_body_p(doc, text, bold_prefix=None, space_after=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.bold = True
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    run = p.add_run(text)
    run.font.name = "Calibri"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
    return p

def add_code_block(doc, code_text):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, "F1F5F9")
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.05
    run = p.add_run(code_text)
    run.font.name = "Consolas"
    run.font.size = Pt(8.5)
    run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_callout(doc, title, body, hex_bg="EFF6FF", hex_border="3B82F6"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0, 0)
    set_cell_background(cell, hex_bg)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="{hex_border}"/>
            <w:top w:val="none"/>
            <w:right w:val="none"/>
            <w:bottom w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    set_cell_margins(cell, top=100, bottom=100, left=150, right=150)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    r_title = p.add_run(title + "\n")
    r_title.bold = True
    r_title.font.name = "Arial"
    r_title.font.size = Pt(9.5)
    r_title.font.color.rgb = RGBColor(0x1E, 0x3A, 0x8A)
    r_body = p.add_run(body)
    r_body.font.name = "Calibri"
    r_body.font.size = Pt(9)
    r_body.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)

def add_image_evidence(doc, filename, caption, width_in=5.8):
    filepath = os.path.join(EVIDENCE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"Warning: file {filepath} not found")
        return
    try:
        with Image.open(filepath) as im:
            buf = io.BytesIO()
            im.save(buf, format="PNG")
            buf.seek(0)
            
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(6)
            p_img.paragraph_format.space_after = Pt(2)
            p_img.paragraph_format.keep_with_next = True
            run_img = p_img.add_run()
            run_img.add_picture(buf, width=Inches(width_in))
            
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_after = Pt(8)
            run_cap = p_cap.add_run(caption)
            run_cap.italic = True
            run_cap.font.name = "Calibri"
            run_cap.font.size = Pt(8.5)
            run_cap.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
    except Exception as e:
        print(f"Error adding {filename}: {e}")

def build_docx():
    doc = Document()
    
    # Page Margins
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)
        
    # Title Block Table
    t_title = doc.add_table(rows=1, cols=1)
    t_title.alignment = WD_TABLE_ALIGNMENT.CENTER
    c_title = t_title.cell(0, 0)
    set_cell_background(c_title, "1E293B")
    set_cell_margins(c_title, top=180, bottom=180, left=200, right=200)
    p_t = c_title.paragraphs[0]
    p_t.paragraph_format.space_after = Pt(2)
    r1 = p_t.add_run("PSEB / ATOMCAMP DEPLOY AI BOOTCAMP\n")
    r1.font.name = "Arial"
    r1.font.size = Pt(9.5)
    r1.font.bold = True
    r1.font.color.rgb = RGBColor(0x38, 0xBD, 0xF8) # Sky blue
    
    r2 = p_t.add_run("Module S09: Recon Workflow & File Upload Exploitation\n")
    r2.font.name = "Arial"
    r2.font.size = Pt(16)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    
    r3 = p_t.add_run("Technical Pentest Report, 10-Step Recon Framework & Executive Advisory Brief")
    r3.font.name = "Calibri"
    r3.font.size = Pt(10)
    r3.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)
    
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    
    # Metadata Block Table
    meta_table = doc.add_table(rows=2, cols=3)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(meta_table, color="CBD5E1")
    meta_data = [
        [("Trainer:", " Waseem Abbas Khan (CEI Master Trainer)"), ("Target System:", " Metasploitable 2 (10.50.20.30)"), ("Environment:", " DVWA v1.0.7 / Apache 2.2.8")],
        [("Authorized Operator:", " badguy (10.50.20.10)"), ("Lab Boundary:", " Isolated Host-Only (VMnet3)"), ("Evaluation Date:", " November 12, 2026")]
    ]
    for r_idx, row in enumerate(meta_data):
        for c_idx, (k, v) in enumerate(row):
            cell = meta_table.cell(r_idx, c_idx)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            rk = p.add_run(k)
            rk.bold = True
            rk.font.name = "Arial"
            rk.font.size = Pt(8.5)
            rk.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            rv = p.add_run(v)
            rv.font.name = "Calibri"
            rv.font.size = Pt(8.5)
            rv.font.color.rgb = RGBColor(0x47, 0x55, 0x69)
            
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    # Executive Summary
    add_header_paragraph(doc, "Executive Summary", level=1)
    add_body_p(doc, "Web application penetration testing departs fundamentally from network infrastructure scanning. While infrastructure scanning evaluates numbered ports bound to operating system daemons, modern web application assessments evaluate client-server transactions, endpoint routing logic, input validation filters, and server execution environments. Scanning a web port reveals only that a web server daemon is active; operational security insight emerges from systematically dissecting application behavior.")
    add_body_p(doc, "Among web application vulnerabilities, Unrestricted File Upload (CWE-434 / OWASP A04:2021) represents one of the most critical risks to organizational infrastructure. When an application accepts external user files and places them directly into a publicly accessible web directory without validating content, normalizing extensions, and denying script execution, an attacker can achieve instantaneous remote command execution (RCE) at the privilege level of the web server daemon.")
    add_body_p(doc, "This assessment report documents the complete fulfillment of the Day 6 Bootcamp requirements against Metasploitable 2 (10.50.20.30):")
    add_body_p(doc, "1. Task 1 (35%): A customized ten-step reconnaissance workflow detailing the investigative question, primary/secondary tooling, output artifacts, and defensible stopping conditions for each stage, complete with technical justification for tooling choices.", bold_prefix="• ")
    add_body_p(doc, "2. Task 2 (40%): A full technical walkthrough of the DVWA File Upload module across all four security tiers (Low, Medium, High, and Impossible), supported by 17 visual evidence captures and in-depth defensive source code analysis.", bold_prefix="• ")
    add_body_p(doc, "3. Task 3 (25%): An executive remediation brief written specifically for senior non-technical leadership, articulating business risk, operational impact, and mandatory architectural controls without relying on technical jargon (strictly omitting the words 'payload' and 'shell').", bold_prefix="• ")

    # Evidence Inventory Table
    add_header_paragraph(doc, "Evidence Inventory", level=1)
    add_body_p(doc, "The following 17 visual evidence captures document every operational milestone executed across the isolated lab infrastructure:")
    
    ev_table = doc.add_table(rows=18, cols=4)
    ev_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(ev_table, color="CBD5E1")
    
    headers = ["Figure #", "Evidence Filename", "Module / Task", "Technical Milestone Recorded"]
    for c_idx, h in enumerate(headers):
        cell = ev_table.cell(0, c_idx)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    evidence_rows = [
        ("Figure 1.1", "01_dvwa_security_low.png", "Setup", "DVWA security level configured to Low with PHPIDS disabled."),
        ("Figure 1.2", "02_recon_nmap_web_ports.png", "Recon", "Targeted Nmap scan of ports 80, 8080, 8081, 443, 8443, 4443 on 10.50.20.30."),
        ("Figure 1.3", "03_recon_whatweb_fingerprint.jpg", "Recon", "WhatWeb technology fingerprint disclosing Apache 2.2.8 and PHP 5.2.4."),
        ("Figure 1.4", "04_recon_gobuster_directories.jpg", "Recon", "Gobuster directory brute-force with extension list identifying /hackable/uploads/."),
        ("Figure 2.1", "05_upload_low_baseline_image.png", "Upload Low", "Benign PNG upload confirming storage path (../../hackable/uploads/)."),
        ("Figure 2.2", "06_upload_low_shell_creation.png", "Upload Low", "Construction and terminal verification of command execution script shell.php."),
        ("Figure 2.3", "07_upload_low_shell_success.png", "Upload Low", "DVWA server response confirming unvalidated upload of shell.php."),
        ("Figure 2.4", "08_upload_low_rce_execution.jpg", "Upload Low", "Command execution verification via curl: id, whoami, hostname, and ip a."),
        ("Figure 3.1", "09_upload_medium_security.png", "Upload Medium", "DVWA security level configuration updated to Medium."),
        ("Figure 3.2", "10_upload_medium_rejection.png", "Upload Medium", "Server rejection message ('Your image was not uploaded') on direct script upload."),
        ("Figure 3.3", "11_upload_medium_burp_intercept.png", "Upload Medium", "Burp Suite intercepting request and modifying Content-Type to image/jpeg."),
        ("Figure 3.4", "12_upload_medium_shell_success.png", "Upload Medium", "DVWA server accepting modified request and confirming upload of shell.php."),
        ("Figure 3.5", "13_upload_medium_rce_execution.png", "Upload Medium", "Remote command execution verified via curl returning uid=33(www-data)."),
        ("Figure 4.1", "14_dvwa_security_high.png", "Upload High", "DVWA security level configuration updated to High."),
        ("Figure 4.2", "15_upload_high_rejection.png", "Upload High", "Server rejecting .php extension regardless of client-supplied MIME tampering."),
        ("Figure 4.3", "16_upload_high_polyglot_creation.png", "Upload High", "Dual-format JPEG polyglot generation on Kali using convert, printf, file, identify."),
        ("Figure 4.4", "17_upload_high_polyglot_success.png", "Upload High", "High-level filter bypassed: small.jpg accepted by getimagesize() check.")
    ]
    
    for r_idx, row in enumerate(evidence_rows, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row):
            cell = ev_table.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=100, right=100)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)
            else:
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
                
    doc.add_page_break()
    
    # Task 1: Ten-Step Recon Workflow
    add_header_paragraph(doc, "Task 1: Ten-Step Reconnaissance Workflow (Weight: 35%)", level=1)
    add_body_p(doc, "A reconnaissance workflow standardizes the transition from an abstract corporate domain to an actionable list of endpoints and vulnerability candidates. Operating without defined stopping conditions leads to infinite crawling loops or premature scanning blocks. The framework below establishes exact inputs, tooling, outputs, and termination thresholds.")
    
    t1_table = doc.add_table(rows=11, cols=5)
    t1_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t1_table, color="CBD5E1")
    
    t1_headers = ["#", "Stage", "Question Answered", "Primary Tools", "Stopping Condition"]
    for c_idx, h in enumerate(t1_headers):
        cell = t1_table.cell(0, c_idx)
        set_cell_background(cell, "1E293B")
        set_cell_margins(cell, top=80, bottom=80, left=80, right=80)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.bold = True
        r.font.name = "Arial"
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        
    t1_steps = [
        ("01", "Domain Info", "Who owns the organization, when was it created, and what are authoritative NS?", "whois, who.is, PKNIC", "Authoritative registrar record retrieved; dates, contact emails, and name servers logged."),
        ("02", "DNS Infra", "Where does email and hosting infrastructure physically and logically resolve?", "dig (A, MX, NS, TXT)", "All primary records queried; mail providers identified; SPF/DMARC TXT records logged."),
        ("03", "Subdomains", "What auxiliary digital assets exist under the target organizational domain?", "subfinder, assetfinder, amass", "Zero new hostnames discovered after querying 3 passive sources and CT logs."),
        ("04", "Live Hosts", "Which candidate hostnames actively respond to HTTP/HTTPS connections?", "httpx-toolkit, curl -I", "Entire candidate list probed; non-responsive hosts pruned; titles/status codes cataloged."),
        ("05", "Port Scans", "What network services and daemon ports listen behind firewalls?", "nmap, naabu", "Top 1,000 TCP ports scanned; web ports (80, 443, 8080, 8443) probed for service banners."),
        ("06", "Tech Profile", "What web servers, application runtimes, and frameworks power the site?", "whatweb -v, wappalyzer-cli", "Server headers, cookies, runtime signatures, and DOM fingerprints cataloged."),
        ("07", "WAF Check", "Is traffic actively filtered, inspected, or normalized by an edge proxy?", "wafw00f, nmap http-waf", "Target tested with non-standard strings; WAF vendor identified or direct origin confirmed."),
        ("08", "Dir Brute", "What unlinked directories, configuration files, and backups are exposed?", "gobuster dir, dirb", "Wordlist fully traversed; high-risk extensions (.php, .txt, .bak, .old) evaluated."),
        ("09", "URL Crawl", "What active endpoints, input parameters, and REST routes exist?", "katana -d 2, gau", "Crawl reaches depth 2/3 or historical archives exhausted; URL inventory deduplicated."),
        ("10", "Misconfigs", "What unpatched versions, open directory listings, and TLS flaws exist?", "nikto, nuclei, sslscan", "Automated engines complete vulnerability scans; zero server rate-limit blocks encountered.")
    ]
    
    for r_idx, row in enumerate(t1_steps, start=1):
        bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        for c_idx, val in enumerate(row):
            cell = t1_table.cell(r_idx, c_idx)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8)
            if c_idx == 0:
                r.bold = True
                r.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)
            else:
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)
                
    add_header_paragraph(doc, "Tool Substitution Justification", level=2)
    add_body_p(doc, "During the bootcamp demonstration, dirb was introduced as the default directory brute-forcing tool. In our operational methodology, we selected gobuster dir as a superior alternative based on three concrete technical advantages:", bold_prefix="Selected Tool: ")
    add_body_p(doc, "1. Concurrency and Throughput: dirb executes sequential C-based requests, causing a standard dictionary scan of 4,600+ entries to take 3 to 5 minutes. gobuster dir utilizes Go coroutines (goroutines) to perform multi-threaded asynchronous requests (10 to 50 threads), completing the same dictionary traversal in under 12 seconds.", bold_prefix="• ")
    add_body_p(doc, "2. Multi-Extension Dynamic Appending: In web application assessments, developer backups represent severe risks (e.g. config.php.bak). gobuster natively appends multiple target extensions simultaneously via -x php,txt,bak,old, discovering exposed configuration backups in a single unified pass.", bold_prefix="• ")
    add_body_p(doc, "3. Resilient Status Filtering: gobuster supports granular response status filtering (-b 404,403) and custom pattern matching, eliminating false positives caused by custom HTTP 200 handlers and wildcard redirects.", bold_prefix="• ")

    add_image_evidence(doc, "02_recon_nmap_web_ports.png", "Figure 1.2: Port discovery scanning common web listeners on 10.50.20.30 (Port 80 open).")
    add_image_evidence(doc, "03_recon_whatweb_fingerprint.jpg", "Figure 1.3: WhatWeb fingerprint identifying Apache 2.2.8 and PHP 5.2.4 on Ubuntu Linux.")
    add_image_evidence(doc, "04_recon_gobuster_directories.jpg", "Figure 1.4: Gobuster directory brute-force discovering /hackable/uploads/ and sensitive files.")

    doc.add_page_break()

    # Task 2: File Upload Walkthrough
    add_header_paragraph(doc, "Task 2: Full File Upload Walkthrough (Weight: 40%)", level=1)
    add_body_p(doc, "The File Upload module within Damn Vulnerable Web Application (DVWA v1.0.7) illustrates how naive validation implementations fail under real-world scrutiny. The progression across Low, Medium, High, and Impossible reveals the exact defensive value of each control and the cost of each bypass.")

    # Low Level
    add_header_paragraph(doc, "1. Level Low: Zero Server-Side Validation", level=2)
    add_body_p(doc, "At Level Low, the application performs no validation whatsoever on the uploaded file. The uploaded file is moved directly from temporary storage into the web-accessible directory ../../hackable/uploads/ using its original client-supplied filename.", bold_prefix="Defensive Posture: ")
    add_body_p(doc, "A baseline benign image was first uploaded to confirm that file storage was operational and to disclose the exact server path. A minimal command execution script (shell.php) was then created locally and uploaded without restriction. Upon accessing the URL over HTTP, arbitrary system commands were executed, confirming RCE as www-data (uid=33).", bold_prefix="Exploitation Workflow: ")

    add_image_evidence(doc, "05_upload_low_baseline_image.png", "Figure 2.1: Benign PNG upload confirming storage path (../../hackable/uploads/).")
    add_image_evidence(doc, "06_upload_low_shell_creation.png", "Figure 2.2: Local creation and verification of shell.php on Kali Linux.")
    add_image_evidence(doc, "07_upload_low_shell_success.png", "Figure 2.3: Low level confirmation: shell.php successfully stored in web root.")
    add_image_evidence(doc, "08_upload_low_rce_execution.jpg", "Figure 2.4: Command execution proof via curl confirming uid=33(www-data) and host identity.")

    # Medium Level
    add_header_paragraph(doc, "2. Level Medium: Client-Controlled MIME Type Validation", level=2)
    add_body_p(doc, "At Level Medium, the developer attempts to enforce validation by inspecting $_FILES['uploaded']['type'] and checking that it matches image/jpeg or image/png, along with a file size limit of 100,000 bytes.", bold_prefix="Defensive Posture: ")
    add_body_p(doc, "The critical flaw is that $_FILES['uploaded']['type'] is not verified on the server; it is extracted directly from the Content-Type header sent by the client's browser. An attacker using an intercepting proxy (Burp Suite) can capture the multipart POST request and modify Content-Type: application/x-php to Content-Type: image/jpeg. The server evaluates the falsified header, passes the check, and writes the script to disk.", bold_prefix="Bypass Mechanics: ")

    add_image_evidence(doc, "09_upload_medium_security.png", "Figure 3.1: DVWA security configuration updated to Medium.")
    add_image_evidence(doc, "10_upload_medium_rejection.png", "Figure 3.2: Server rejecting upload when client sends Content-Type: application/x-php.")
    add_image_evidence(doc, "11_upload_medium_burp_intercept.png", "Figure 3.3: Burp Suite intercepting request and rewriting Content-Type to image/jpeg.")
    add_image_evidence(doc, "12_upload_medium_shell_success.png", "Figure 3.4: Server accepting modified request and confirming upload of shell.php.")
    add_image_evidence(doc, "13_upload_medium_rce_execution.png", "Figure 3.5: Remote command execution verified via curl on Medium security.")

    doc.add_page_break()

    # High Level
    add_header_paragraph(doc, "3. Level High: Extension Whitelist & Content Inspection", level=2)
    add_body_p(doc, "Level High implements a much stricter check: the file extension must strictly end with .jpg, .jpeg, or .png, and the server executes PHP's getimagesize() function on the temporary file. Attempting to upload shell.php with a spoofed MIME header fails because the extension is rejected and getimagesize() returns false on raw script text.", bold_prefix="Defensive Posture: ")
    add_body_p(doc, "A polyglot file satisfies two distinct format specifications simultaneously. Using ImageMagick's convert, a genuine 50x50 pixel JPEG image (small.jpg) was generated. PHP command execution instructions were then appended to the file. Because the file retains authentic JPEG magic bytes, header segments, and dimensional data, getimagesize() evaluates it as a valid image and the upload succeeds.", bold_prefix="Bypass Mechanics: ")

    add_image_evidence(doc, "14_dvwa_security_high.png", "Figure 4.1: DVWA security configuration updated to High.")
    add_image_evidence(doc, "15_upload_high_rejection.png", "Figure 4.2: High security rejecting script upload despite MIME manipulation.")
    add_image_evidence(doc, "16_upload_high_polyglot_creation.png", "Figure 4.3: Terminal output showing creation and validation of dual-format JPEG polyglot.")
    add_image_evidence(doc, "17_upload_high_polyglot_success.png", "Figure 4.4: High-level filter bypassed: small.jpg accepted by getimagesize() check.")

    # Impossible Level
    add_header_paragraph(doc, "4. Level Impossible: Architectural Defense-in-Depth", level=2)
    add_body_p(doc, "The Impossible level eliminates all file upload bypasses by implementing four independent, layered architectural controls:", bold_prefix="Defensive Architecture: ")
    
    add_body_p(doc, "1. Anti-CSRF Token Validation (checkToken): Verifies a session-bound cryptographic token, preventing cross-site request forgery and automated upload submissions.", bold_prefix="• Control 1: ")
    add_body_p(doc, "2. Cryptographic Filename Randomization: The user-supplied filename is discarded. The file is saved as md5(uniqid() . $uploaded_name) . '.' . $uploaded_ext, eliminating path traversal risks and making direct file access unpredictable.", bold_prefix="• Control 2: ")
    add_body_p(doc, "3. Image GD Re-Encoding (imagecreatefromjpeg / imagejpeg): This is the decisive defense against polyglots. The server reads the raw pixel data into memory and re-renders an entirely new image file to disk. All appended scripts, comments, and non-image metadata are permanently stripped and destroyed.", bold_prefix="• Control 3: ")
    add_body_p(doc, "4. Directory Execution Denial: Configuring the web server (.htaccess with php_flag engine off or Options -ExecCGI) ensures that the upload folder is incapable of executing scripts, rendering any uploaded file inert.", bold_prefix="• Control 4: ")

    add_code_block(doc, """// DVWA Impossible Level Upload Defense (impossible.php snippet)
if( ( strtolower( $uploaded_ext ) == 'jpg' || strtolower( $uploaded_ext ) == 'jpeg' || strtolower( $uploaded_ext ) == 'png' ) &&
    ( $uploaded_size < 100000 ) &&
    ( $uploaded_type == 'image/jpeg' || $uploaded_type == 'image/png' ) &&
    getimagesize( $uploaded_tmp ) ) {

    // Strip metadata and re-encode image from raw pixels
    if( $uploaded_type == 'image/jpeg' ) {
        $img = imagecreatefromjpeg( $uploaded_tmp );
        imagejpeg( $img, $temp_file, 100);
    } else {
        $img = imagecreatefrompng( $uploaded_tmp );
        imagepng( $img, $temp_file, 9);
    }
    imagedestroy( $img );
    rename( $temp_file, ( $target_path . $target_file ) );
}""")

    doc.add_page_break()

    # Task 3: Executive Remediation Brief (Strictly 1 page)
    add_header_paragraph(doc, "Task 3: Executive Remediation Brief (Weight: 25%)", level=1)
    
    # Memo Box
    tbl_memo = doc.add_table(rows=4, cols=2)
    tbl_memo.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(tbl_memo, color="0284C7")
    memo_headers = [
        ("TO:", "Executive Leadership & IT Steering Committee"),
        ("FROM:", "Enterprise Information Security Assessment Team"),
        ("DATE:", "November 12, 2026"),
        ("SUBJECT:", "Strategic Risk Assessment & Remediation Roadmap: File Storage Architecture")
    ]
    for r_idx, (k, v) in enumerate(memo_headers):
        c0 = tbl_memo.cell(r_idx, 0)
        c1 = tbl_memo.cell(r_idx, 1)
        set_cell_background(c0, "F0F9FF")
        set_cell_background(c1, "F0F9FF")
        set_cell_margins(c0, top=40, bottom=40, left=80, right=80)
        set_cell_margins(c1, top=40, bottom=40, left=80, right=80)
        p0 = c0.paragraphs[0]
        p0.paragraph_format.space_after = Pt(0)
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.name = "Arial"
        r0.font.size = Pt(8.5)
        r0.font.color.rgb = RGBColor(0x03, 0x69, 0xA1)
        p1 = c1.paragraphs[0]
        p1.paragraph_format.space_after = Pt(0)
        r1 = p1.add_run(v)
        r1.font.name = "Calibri"
        r1.font.size = Pt(8.5)
        r1.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)
        
    doc.add_paragraph().paragraph_format.space_after = Pt(6)
    
    add_header_paragraph(doc, "Executive Risk Analysis & Business Exposure", level=2)
    add_body_p(doc, "During our recent technical security assessment, our team evaluated the mechanisms responsible for receiving external customer files within our core web applications. We identified a critical architectural weakness in how incoming files are stored and managed on corporate infrastructure.")
    add_body_p(doc, "Under current configurations, our servers accept files submitted by internet users and store them directly inside public website directories. Crucially, organizational web servers are configured to treat files in these directories as executable application code rather than inert data. This creates four major areas of commercial and operational exposure:")
    add_body_p(doc, "1. Total Loss of Data Confidentiality: Unauthorized external actors can read proprietary application databases, customer records, employee credentials, and backend configuration files.", bold_prefix="• ")
    add_body_p(doc, "2. Complete Host Compromise: External parties can execute administrative commands on organizational servers, establishing an unauthorized foothold inside our internal network.", bold_prefix="• ")
    add_body_p(doc, "3. Critical Business Disruption: External actors can alter website contents, delete core databases, or deploy encrypting software that halts corporate operations.", bold_prefix="• ")
    add_body_p(doc, "4. Regulatory Penalties: An exposure of customer databases triggers mandatory data breach disclosures under privacy legislation, carrying substantial financial fines and lasting brand harm.", bold_prefix="• ")

    add_header_paragraph(doc, "Root Cause in Plain Language", level=2)
    add_body_p(doc, "The risk does not arise simply from allowing users to upload documents or profile pictures. The danger arises from a fundamental failure to separate storage from execution:")
    add_body_p(doc, "1. Excessive Trust in External Labels: Our software currently trusts declarations provided by the user's internet browser (such as file names and claimed format types) without independently verifying what the file actually contains.", bold_prefix="• ")
    add_body_p(doc, "2. Execution Permissions on Storage Folders: When an external file is placed in a public folder, the server's default configuration attempts to run any code it recognizes inside that file. The server should never run software out of a folder dedicated to storing images or documents.", bold_prefix="• ")

    add_header_paragraph(doc, "Four-Pillar Strategic Remediation Roadmap", level=2)
    add_body_p(doc, "To permanently eliminate this vulnerability across all organizational systems, engineering teams must implement four mandatory controls:")
    add_body_p(doc, "1. Server-Side Image Re-generation: Applications must never store raw files received from external users. Graphics must be processed through backend rendering software that reads raw pixels and writes a brand new, clean image file. This process automatically strips all unauthorized instructions, comments, and hidden data.", bold_prefix="Pillar 1 — ")
    add_body_p(doc, "2. Cryptographic Name Replacement: Discard original user-provided filenames entirely. The system must assign a randomized, computer-generated alphanumeric identifier with an approved extension, preventing attackers from predicting file locations or manipulating directory paths.", bold_prefix="Pillar 2 — ")
    add_body_p(doc, "3. Storage Outside Public Web Roots: Store uploaded documents in private storage locations—such as dedicated cloud object storage buckets or isolated internal directories—that cannot be accessed directly via internet web browsers.", bold_prefix="Pillar 3 — ")
    add_body_p(doc, "4. Absolute Execution Denial: Web server software must be explicitly configured so that program execution handlers are permanently deactivated across all file storage repositories. The server must be fundamentally incapable of running stored files as software.", bold_prefix="Pillar 4 — ")

    add_callout(doc, "Executive Recommendation", "Remediating this critical weakness does not require expensive commercial licenses. It requires enforcing disciplined engineering policies that isolate data storage from program execution. We recommend mandating these four pillars across all development teams immediately.", hex_bg="F0FDF4", hex_border="22C55E")

    doc.save(OUTPUT_DOCX)
    print(f"Successfully generated DOCX report at: {OUTPUT_DOCX}")

if __name__ == "__main__":
    build_docx()
