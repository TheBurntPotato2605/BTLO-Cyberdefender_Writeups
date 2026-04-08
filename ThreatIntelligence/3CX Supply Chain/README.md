# 🛡️ Security Writeup – 3CX Supply Chain

Reconstruct the 3CX supply chain attack by analyzing compromised MSI and DLL artifacts to identify TTPs and attribute the incident to a threat actor.

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Threat Intelligence
* **Difficulty:** Easy
* **Date:** 08/04/2026

---

## 📖 Scenario

A large multinational corporation heavily relies on the 3CX software for phone communication, making it a critical component of their business operations. After a recent update to the 3CX Desktop App, antivirus alerts flag sporadic instances of the software being wiped from some workstations while others remain unaffected. Dismissing this as a false positive, the IT team overlooks the alerts, only to notice degraded performance and strange network traffic to unknown servers. Employees report issues with the 3CX app, and the IT security team identifies unusual communication patterns linked to recent software updates.

---

## 🎯 Objectives

As the threat intelligence analyst, it's your responsibility to examine this possible supply chain attack. Your objectives are to uncover how the attackers compromised the 3CX app, identify the potential threat actor involved, and assess the overall extent of the incident. 

---

## 🧰 Tools 

* Tools: VirusTotal, ANY.RUN, Fortinet, Qualys report, 3CX



---

## 🔍 Analysis

* Understanding the scope of the attack and identifying which versions exhibit malicious behavior is crucial for making informed decisions if these compromised versions are present in the organization. From the 3CX's blog on 30/03/2023, Pierre Jorrdan - AppSec & Interpop Manager informed that their Electron Windows App version number 18.12.407 & 18.12.416 include security issue.

<img width="1211" height="661" alt="image" src="https://github.com/user-attachments/assets/07d99f39-fc96-46fc-b707-240f3a895951" />

* Determining the age of the malware can help assess the extent of the compromise and track the evolution of malware families and variants. Using the malicious .msi file's hash value, we have information about its history on VirusTotal

<img width="547" height="180" alt="image" src="https://github.com/user-attachments/assets/d306a219-df3f-4214-9b52-e307dd90f0bd" />

* Executable files (.exe) are frequently used as primary or secondary malware payloads, while dynamic link libraries (.dll) often load malicious code or enhance malware functionality. Analyzing files deposited by the Microsoft Software Installer (.msi) is crucial for identifying malicious files and investigating their full potential. The Fortinet's report about 3CX Desktop App compromised indicates there are 2 malicious sideload DLLs

<img width="1616" height="333" alt="image" src="https://github.com/user-attachments/assets/f38475b8-bc0e-48c6-8059-859e382bd68b" />

* Recognizing the persistence techniques used in this incident is essential for current mitigation strategies and future defense improvements. From both report of Qualys and VirusTotal about the incodent, we can see that the hacker use MITRE Technique ID T1574.003 - DLL Side-Loading to load the malicious DLLs

<img width="1497" height="222" alt="image" src="https://github.com/user-attachments/assets/d0dba6bc-7861-41d4-9e4c-0a5579925118" />

<img width="646" height="476" alt="image" src="https://github.com/user-attachments/assets/0dcadf98-e141-459b-b88b-05fbecbb37f5" />

* Recognizing the malware type (threat category) is essential to your investigation, as it can offer valuable insight into the possible malicious actions you'll be examining. Security vendor' analysis said that threat category in this case is Trojan, 3CXDesktop App had been Trojanized due to code-level compromise

<img width="1911" height="808" alt="image" src="https://github.com/user-attachments/assets/3682670e-d920-4714-820e-7e9adfee2a17" />

* As a threat intelligence analyst conducting dynamic analysis, it's vital to understand how malware can evade detection in virtualized environments or analysis systems. This knowledge will help you effectively mitigate or address these evasive tactics.

<img width="525" height="315" alt="image" src="https://github.com/user-attachments/assets/7a2391c3-45f3-4d4e-b6df-86d06eface90" />

* When conducting malware analysis and reverse engineering, understanding anti-analysis techniques is vital to avoid wasting time. In the previous section, we know that the two malicious DLLs used virtualization/sandbox evasion technique ID T1497. To be more specific, they use these sub-technique:

<img width="633" height="223" alt="image" src="https://github.com/user-attachments/assets/d797d76a-b901-4620-9dc4-b5193121271a" />
<img width="387" height="559" alt="image" src="https://github.com/user-attachments/assets/83dc06ed-6572-4c54-b95b-0ec46729e28d" />

* Identifying the cryptographic method used in malware is crucial for understanding the techniques employed to bypass defense mechanisms and execute its functions fully. The attacker use RC4 KSA/PRGA to encrypt data and using Base64, ADD XOR SUB for encoding purpose.

<img width="532" height="576" alt="image" src="https://github.com/user-attachments/assets/d402ccc4-5097-4d7d-8a8c-0f0b4c58ed49" />

* As an analyst, you've recognized some TTPs involved in the incident, but identifying the APT group responsible will help you search for their usual TTPs and uncover other potential malicious activities. From the Qualys' report, it is confirmed that the Lazarus group take responsibility for this attack

<img width="1511" height="810" alt="image" src="https://github.com/user-attachments/assets/4a3c6a38-ddf1-482b-a262-929770cc9924" />

---

### Key Artifact Identification

#### 1. Qualys' Report
<img width="651" height="714" alt="image" src="https://github.com/user-attachments/assets/439b5157-cc24-4c8d-8a02-f4424e5556e0" />
<img width="682" height="733" alt="image" src="https://github.com/user-attachments/assets/1bb9b1d3-ba4e-49e4-9545-c4f042e5ba51" />
<img width="318" height="723" alt="image" src="https://github.com/user-attachments/assets/0a106481-95b6-4d64-9f8a-34deb98d54b0" />

<img width="688" height="714" alt="image" src="https://github.com/user-attachments/assets/4bce716e-8f17-48f0-ad3f-5b20c52815ec" />

#### 2. Fortinet's Report
<img width="825" height="588" alt="image" src="https://github.com/user-attachments/assets/8a3e550c-1be8-4068-b94c-7bb543eebe6b" />
<img width="820" height="450" alt="image" src="https://github.com/user-attachments/assets/ea496ddd-d71e-41be-b17e-2a1a691702b2" />

<img width="284" height="632" alt="image" src="https://github.com/user-attachments/assets/13aa6ed8-2df8-456f-997a-b2723ca2abc4" />
<img width="285" height="531" alt="image" src="https://github.com/user-attachments/assets/d219c4d7-ccb9-4421-ad1a-20437ed25ece" />





---

## 🧾 Key Findings

* Legitimate signed application used to deliver malware
* Malicious DLLs executed under trusted process context
* Use of DLL side-loading enabled stealthy persistence and execution
* Advanced evasion and encryption techniques hindered detection and analysis
* Malware included virtualization-aware anti-analysis checks before running fully

---



## 🧬 Threat Context 

<img width="961" height="717" alt="image" src="https://github.com/user-attachments/assets/c151de34-66b0-4c0e-bd53-0de904621a91" />


---


## 🔐 Prevention & Mitigation

* Remove affected 3CX versions
* Hunt for ffmpeg.dll and d3dcompiler_47.dll on endpoints
* Monitor for suspicious 3CX-related outbound traffic
* Detect DLL side-loading activity in trusted applications
* Watch for malware performing VM or sandbox checks before execution
* Validate and test third-party software updates before deployment

---

## 💡 Lessons Learned

* Trusted software can become an attack vector
* Supply chain attacks can bypass traditional trust controls
* Virtualization evasion can hide real malware behavior during analysis


---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: How many versions of 3CX running on Windows have been flagged as malware?      | 2    |
| Q2: What's the UTC creation time of the .msi malware?      | 2023-03-13 06:33    |
| Q3: Which malicious DLLs were dropped by the .msi file?      | ffmpeg.dll,d3dcompiler_47.dll    |
| Q4: What is the MITRE Technique ID employed by the .msi files to load the malicious DLL?      | T1574    |
| Q5: What is the threat category of the two malicious DLLs?      | Trojan    |
| Q6: What is the MITRE ID for the virtualization/sandbox evasion techniques used by the two malicious DLLs?      | T1497    |
| Q7: Which hypervisor is targeted by the anti-analysis techniques in the ffmpeg.dll file?      | VMware    |
| Q8: What encryption algorithm is used by the ffmpeg.dll file?      | RC4    |
| Q9: Which group is responsible for this attack?      | Lazarus    |

---

