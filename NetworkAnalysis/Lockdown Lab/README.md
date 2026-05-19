# 🛡️ Security Writeup – Lockdown Lab

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Network Forensics
* **Difficulty:** Easy
* **Date:** 19/05/2026

---

## 📖 Scenario

TechNova Systems’ SOC has detected suspicious outbound traffic from a public-facing IIS server in its cloud platform—activity suggestive of a web-shell drop and covert connections to an unknown host.

As the forensic examiner, you have three critical artefacts in hand: a PCAP capturing the initial traffic, a full memory image of the server, and a malware sample recovered from disk. Reconstruct the intrusion and all of the attacker’s activities so TechNova can contain the breach and strengthen its defenses.

---

## 🎯 Objectives

Reconstruct a multi-stage intrusion by analyzing network traffic, memory, and malware artifacts using Wireshark, Volatility, and VirusTotal, mapping findings to MITRE ATT&CK.

---

## 🧰 Tools & Techniques

* Tools: Wireshark, Volatility, VirusTotal

---



## 🔍 Analysis

* Let's have an overview of the given PCAP file. After flooding the IIS host with rapid-fire probes, the attacker reveals their origin. As shown below, the number of packets sent from IP addess 10.0.2.4 to 10.0.2.15 are the most among the traffic.

  <img width="1352" height="342" alt="image" src="https://github.com/user-attachments/assets/68f1b8e1-7a0e-4e82-ab1b-30e4a7d7b6d9" />
  <img width="1520" height="586" alt="image" src="https://github.com/user-attachments/assets/dbd6ecae-09c0-4b7b-9d62-5816b77c937b" />

* Within a short timeframe, attacker sent multiple SYN requests to victim IP response with RST ACK. This indicates that he is trying to port scan to discover system.

  <img width="1876" height="391" alt="image" src="https://github.com/user-attachments/assets/84f352b7-7927-44c3-bdcc-8be9787ab172" />

* Zeroing in on a single open service to gain a foothold, the attacker carries out targeted enumeration.  MITRE ATT&CK technique ID T1046 covers this activity

  <img width="1465" height="492" alt="image" src="https://github.com/user-attachments/assets/e2522391-f5c2-42eb-96f6-42469607eba8" />

* While reviewing the SMB traffic, you observe two consecutive Tree Connect requests that expose the first shares the intruder probes on the IIS host. That’s a strong indicator of  enumerating SMB shares — a reconnaissance step that often precedes lateral movement or data access.

  <img width="1872" height="251" alt="image" src="https://github.com/user-attachments/assets/02decf56-9b26-4a81-aaee-511632b3155a" />

  <img width="1709" height="601" alt="image" src="https://github.com/user-attachments/assets/f5ca3095-4049-42ff-88c8-afcd386624ac" />

* Inside the share, the attacker plants a web-accessible payload that will grant remote code execution. The filename shell.aspx strongly suggests the attacker is uploading a malicious ASP.NET web shell to the IIS host. Once placed in a web‑accessible directory, the attacker can execute commands through the shell, giving them interactive control of the server.

  <img width="1882" height="287" alt="image" src="https://github.com/user-attachments/assets/cb32e725-547e-4d43-9815-858ea1684dd7" />

* The newly planted shell calls back to the attacker over an uncommon but firewall-friendly port. We need to review HTTP GET request to shell.aspx (3573), this is the moment webshell is activated

  <img width="1077" height="91" alt="image" src="https://github.com/user-attachments/assets/75ee78a8-9cb3-4e07-bed4-521b5320ce91" />

* Right after that packet, we see a TCP connection from from our server to the attacker's machine(3574) - this is a reverse shell. Next, the destination port is kept repeatedly which indicates that this is listening port of the hacker. 

  <img width="1662" height="396" alt="image" src="https://github.com/user-attachments/assets/53142d7c-a9f4-4032-9e9a-f735812b9da2" />

* Your memory snapshot captures the system’s kernel in situ, providing vital context for the breach. To view the kernel base, we use windows.info of volatility

  <img width="640" height="444" alt="image" src="https://github.com/user-attachments/assets/b7ff96e1-d733-4742-b0b3-8690be6007f4" />

* A trusted service launches an unfamiliar executable residing outside the usual IIS stack, signalling a persistence implant. updatenow.exe is not a normal Windows startup service under the Startup

  <img width="628" height="325" alt="image" src="https://github.com/user-attachments/assets/2e65906e-b885-4f5f-a7df-d855b7822198" />

* The reverse shell’s outbound traffic is handled by a built-in Windows process that also spawns the implanted executable. w3wp.exe is the IIS worker process, responsible for handling web requests. updatenow.exe launched by w3wp.exe is not normal startup behavior — it’s evidence of a malicious payload executed via the IIS worker process, confirming active exploitation of the host.

  <img width="626" height="35" alt="image" src="https://github.com/user-attachments/assets/22410385-a596-4a90-b9ec-a6a2479993e9" />

  <img width="633" height="38" alt="image" src="https://github.com/user-attachments/assets/e01791f0-119e-49cb-9f7f-2a69ff1a8a4d" />

* Extracting the executable file, calculate its hash value for more information in Threat Intelligence platform VirusTotal.

  <img width="1759" height="777" alt="image" src="https://github.com/user-attachments/assets/508d9234-9ead-4f16-a505-66104c3a4bc5" />

  
* Static inspection reveals the binary has been packed to hinder analysis. UPX packer was used to obfuscate it

  <img width="1576" height="397" alt="image" src="https://github.com/user-attachments/assets/27748a37-4dfa-468b-a69f-3fcb7ecc543e" />


* Threat-intel analysis shows the malware beaconing to its command-and-control host.

  <img width="590" height="236" alt="image" src="https://github.com/user-attachments/assets/ff436868-8657-402d-aead-4f5e765350a9" />

* Open-source intel associates that hash with a well-known commodity RAT. Malware family the sample belongs to is AgentTesla

  <img width="1871" height="638" alt="image" src="https://github.com/user-attachments/assets/66ba4d7c-4426-424c-87ac-8bd084c2636d" />




---

## 🧾 Key Findings

- **Attacker IP:** `10.0.2.4` – the source of all malicious traffic.
- **Reconnaissance:** Port scan detected using `SYN` packets; technique mapped to **MITRE T1046**.
- **SMB Share Enumeration:** Attacker probed two shares: `\\10.0.2.15\Documents` and `\\10.0.2.15\IPC$`.
- **Webshell Upload:** Malicious ASP.NET file `shell.aspx` placed inside the `Documents` share.
- **Reverse Shell:** Triggered by a `GET` request to `shell.aspx`; callback on attacker’s listening port **4443**.
- **Memory Artifacts:**
  - Kernel base address: `0xf80079213000` (varies per memory dump).
  - Persistence implant: `updatenow.exe` located in the Startup folder.
  - Parent process: `w3wp.exe` (IIS worker) spawned `updatenow.exe`.
- **Malware Analysis:**
  - Packer: **UPX** .
  - C2 domain: cp8nl[.]hyperhost.ua
  - Malware family: **AgentTesla** (info-stealing RAT).

---



## 🧬 Threat Context 

| Tactic | Technique | ID |
|--------|-----------|-----|
| Reconnaissance | Network Service Discovery (port scan, SMB share enumeration) | T1046 |
| Initial Access | Exploit public-facing application (webshell upload) | T1190 |
| Execution | Command and Scripting Interpreter: ASP.NET | T1059 |
| Persistence | Boot or Logon Autostart Execution: Startup Folder | T1547 |
| Defense Evasion | Obfuscated Files or Info: UPX packing | T1027 |

---





## ❓ Answers

| Question | Answer |
|----------|--------|
| Q1: Which IP address generated this reconnaissance traffic? | `10.0.2.4` |
| Q2: Which MITRE ATT&CK technique ID covers this activity? | `T1046` |
| Q3: Which two full UNC paths are accessed? | `\\10.0.2.15\Documents`, `\\10.0.2.15\IPC$` |
| Q4: What is the filename of the malicious file they uploaded, and what byte length is specified in the corresponding SMB2 Write Request? | `shell.aspx`, `1015024` |
| Q5: Which listening port did the attacker use for the reverse shell? | `4443` |
| Q6: What is the kernel base address in the dump? | `0xf80079213000` |
| Q7: What is the final full on-disk path of that executable, and which MITRE ATT&CK persistence technique ID corresponds to this behaviour? | `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\updatenow.exe, T1547` |
| Q8: What is the name of this process, and what PID does it run under? | `w3wp.exe`, `4332` |
| Q9: Which packer was used to obfuscate it? | `UPX` |
| Q10: Which fully qualified domain name (FQDN) does it contact? | `cp8nl.hyperhost.ua` |
| Q11: To which malware family does the sample belong? | `AgentTesla` |

---
