# 🛡️ Security Writeup – Red Stealer Lab

Analyze a suspicious executable using VirusTotal and MalwareBazaar to extract IOCs, identify C2 infrastructure, MITRE ATT&CK techniques, and privilege escalation mechanisms.

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Threat Intelligence
* **Difficulty:** Easy 
* **Date:** 02/04/2026

---

## 📖 Scenario

You are part of the Threat Intelligence team in the SOC (Security Operations Center). An executable file has been discovered on a colleague's computer, and it's suspected to be linked to a Command and Control (C2) server, indicating a potential malware infection.

---

## 🎯 Objectives

Your task is to investigate this executable by analyzing its hash. The goal is to gather and analyze data beneficial to other SOC members, including the Incident Response team, to respond to this suspicious behavior efficiently.


---

## 🧰 Tools 

* Tools: VirusTotal, MalwareBazaar, Threat Fox

---

## 🔍 Analysis

* Categorizing malware enables a quicker and clearer understanding of its unique behaviors and attack vectors. From the security vendor's analysis, it is indicated that this is a Trojan malware
  
<img width="1749" height="761" alt="image" src="https://github.com/user-attachments/assets/57de9a51-52f9-4eec-a3d1-04e7d4b20f35" />

* Clearly identifying the name of the malware file improves communication among the SOC team. As we can see here, it is WEXTRACT

<img width="1749" height="236" alt="image" src="https://github.com/user-attachments/assets/34a82f9c-14fa-4d93-a047-51c549728bdb" />

* Knowing the exact timestamp of when the malware was first observed can help prioritize response actions. Newly detected malware may require urgent containment and eradication compared to older, well-documented threats.

<img width="630" height="219" alt="image" src="https://github.com/user-attachments/assets/b7aba279-de87-4b2d-b5ae-9abae8eec82b" />

* Understanding the techniques used by malware helps in strategic security planning.

<img width="1840" height="786" alt="image" src="https://github.com/user-attachments/assets/0fc0b18d-13e0-45e4-813d-6a4b244639d9" />

<img width="1851" height="790" alt="image" src="https://github.com/user-attachments/assets/d3769d11-5bbd-4c8a-93de-94fb8c71aeef" />

* The malware resolve via DNS queries using popular social media domain name facebook.com

<img width="426" height="291" alt="image" src="https://github.com/user-attachments/assets/189f2358-efcf-40f8-afd2-f18c627bf4c5" />

* Once the malicious IP addresses are identified, network security devices such as firewalls can be configured to block traffic to and from these addresses.

<img width="432" height="347" alt="image" src="https://github.com/user-attachments/assets/79d64275-8701-42a4-b712-8e5cd69d752e" />

<img width="607" height="388" alt="image" src="https://github.com/user-attachments/assets/760bc6d7-e26b-4390-9079-d81ccfb58f5f" />

* YARA rules are designed to identify specific malware patterns and behaviors. Using MalwareBazaar,  the name of the YARA rule created by "Varp0s" that detects the identified malware is detect_RedLine_Stealer

<img width="1655" height="304" alt="image" src="https://github.com/user-attachments/assets/2386dff5-446a-44e7-84ab-3cd32d334b8d" />

* Understanding which malware families are targeting the organization helps in strategic security planning for the future and prioritizing resources based on the threat. Using Threat Fox, we know that this malware alias associated with the malicious IP is RECORDSTEALER

<img width="772" height="286" alt="image" src="https://github.com/user-attachments/assets/0abb0ac5-ad88-43bf-af8e-d4a5305e817a" />

* By identifying the malware's imported DLLs, we can configure security tools to monitor for the loading or unusual usage of these specific DLLs. Here, The malware imports ADVAPI32.DLL, which provides APIs commonly used for token and privilege manipulation. This DLL provides functions like AdjustTokenPrivileges and OpenProcessToken, which are essential for manipulating access tokens and escalating privileges.

<img width="263" height="380" alt="image" src="https://github.com/user-attachments/assets/ec853ed4-0339-4eda-ac8e-5d36f6653d41" />

---

### Key Artifact Identification

* Indicator 1: 77.91.124.55:19071



---

## 🧾 Key Findings

* The sample is a Trojan / stealer-type executable associated with RedLine / RecordStealer-style activity.
* The malware file name associated with the sample is wextract.exe.
* The malware communicates with 77.91.124.55 over TCP port 19071, which is a high-confidence C2 indicator.
* MalwareBazaar-linked reporting ties the sample to the YARA rule detect_Redline_Stealer, authored by Varp0s.
* ThreatFox associates the malicious IP with the alias RECORDSTEALER.
* Sandbox reporting indicates behaviors aligned with persistence, discovery, collection, defense evasion, and C2/exfiltration.

---


## 🧬 Threat Context 

* **Tactic:** Execution, Persistence, Privilege Escalation, Defense Evasion, Discovery, Collection, Impact
* **Technique:** T1204, T1547, T1068, T1055, T1005, T1027, T1218, T1082, T1016, T1033, T1555, T1119, T1071, T1105, T1041


---



## 💡 Lessons Learned

* Hash-based investigation can quickly expose C2 infrastructure, detection content, and threat aliases across multiple intel platforms.
* Cross-validating VirusTotal with MalwareBazaar, ThreatFox, and sandbox reports improves confidence and helps separate confirmed IOCs from incidental execution artifacts.
* The most actionable SOC outputs from this case are:
  
    block 77.91.124.55:19071

    hunt for executions of wextract.exe

    look for credential-store access and registry autostart changes

    deploy detections aligned to detect_Redline_Stealer where applicable.


---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What category has Microsoft identified for that malware in VirusTotal?       | Trojan    |
| Q2: What is the file name associated with this malware?      | WEXTRACT    |
| Q3: What is the UTC timestamp of the malware's first submission to VirusTotal?      | 2023-10-06 04:41    |
| Q4: What is the MITRE ATT&CK technique ID for the malware's data collection from the system before exfiltration?      | T1005    |
| Q5: Following execution, which social media-related domain names did the malware resolve via DNS queries?      | facebook.com    |
| Q6: Can you provide the IP address and destination port the malware communicates with?      | 77.91.124.55:19071    |
| Q7: Using MalwareBazaar, what's the name of the YARA rule created by "Varp0s" that detects the identified malware?      | detect_Redline_Stealer    |
| Q8: Can you provide the different malware alias associated with the malicious IP address according to ThreatFox?      | RECORDSTEALER    |
| Q9: Can you provide the DLL utilized by the malware for privilege escalation?      | ADVAPI32.DLL    |

---

