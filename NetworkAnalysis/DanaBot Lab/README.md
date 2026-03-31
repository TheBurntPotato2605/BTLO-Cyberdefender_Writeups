# 🛡️ Security Writeup – DanaBot Lab

Analyze network traffic using Wireshark to identify DanaBot initial access, deobfuscate malicious JavaScript, and extract IOCs like IPs, file hashes, and execution processes.

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Network Analysis
* **Difficulty:** Easy
* **Date:** 31/03/2026

---

## 📖 Scenario

The SOC team has detected suspicious activity in the network traffic, revealing that a machine has been compromised. Sensitive company information has been stolen. 

---

## 🎯 Objectives

Your task is to use Network Capture (PCAP) files and Threat Intelligence to investigate the incident and determine how the breach occurred.

---

## 🧰 Tools & Techniques

* Tools: Wireshark, VirusTotal, ANY., RUN, Network Miner

---


## 🔍 Analysis

<img width="1608" height="892" alt="image" src="https://github.com/user-attachments/assets/438e1d30-00a1-4873-9702-95dfe8f5e9e4" />

* View the conversations from the pcap file, we see that the IP 10.2.14.101 makes a lot of connection. It s likey to be our victim host so we have to find which IP is connected to it

* Next, we filter out HTTP protocol as it s always used as C2 or to drop malicious files/payloads

<img width="1618" height="236" alt="image" src="https://github.com/user-attachments/assets/b3517f4b-cf98-4248-8f3c-6c9888bacd6a" />

<img width="1913" height="865" alt="image" src="https://github.com/user-attachments/assets/956c819c-ec34-4e60-b0bd-39c1350383a4" />

* Here we identify a suspicious connection to 62.173.142.148, the hacker respond with a packet obfuscated JavaScript file

<img width="1527" height="521" alt="image" src="https://github.com/user-attachments/assets/b7889323-0ba5-46c1-b2cc-2bfafb419cc6" />

* The IP address is reported for being abused on AbuseIPDB while the file is also identified as malicious by ANY.RUN and VirusTotal

<img width="1577" height="788" alt="image" src="https://github.com/user-attachments/assets/e5d946a6-4c78-44b1-99c2-603b9f6877ab" />

<img width="1750" height="771" alt="image" src="https://github.com/user-attachments/assets/3ff20e7e-37af-413c-9b0a-6acd36077f3c" />

* Investigating further with ANY.RUN, it indicates that wscript.exe is the process used to executed malicious .js file. As wscript.exe is the native Windows component used to execute .js  scripts, all script-related malicious behaviors are attributed to it, it is the process that launched and executed the obfuscated JS payload.

<img width="1509" height="766" alt="image" src="https://github.com/user-attachments/assets/a8116fd4-f629-4e2a-9084-8abf3c9e0631" />

* Extracting the obfuscated Javascript file, it indicates that the second malicious file used by the hacker is a .dll file

<img width="1522" height="396" alt="image" src="https://github.com/user-attachments/assets/c92bd105-d2de-4ecb-b703-42a08572b4c0" />


---

### Key Artifact Identification

* Indicator 1: Obfuscated Javascript file allegato_708.js
* Indicator 2: 62.173.142.148




---

## 🧾 Key Findings

* The compromise originated from the victim host 10.2.14.101, which communicated with the malicious external IP 62.173.142.148 over HTTP.

* The attacker delivered an obfuscated JavaScript file named allegato_708.js. This script was executed through wscript.exe, a legitimate Windows scripting component often abused by threat actors for malware execution.

* Analysis of the script revealed evidence of a second-stage payload in the form of a DLL, indicating that the JavaScript acted as the initial loader.

---

## 🧬 Threat Context 

* **Tactic:** Execution, Command and Control
* **Technique:** T1059.007, T1071.001, T1027

---

## 🛡️ Detection Opportunities

* Alert on HTTP responses delivering .js files from untrusted external IP addresses
* Detect execution of wscript.exe spawning suspicious network activity
* Monitor for obfuscated JavaScript written to disk or executed from user-accessible directories
* Flag systems that retrieve script files and shortly afterward load DLL-based payloads
* Correlate external IP reputation feeds with outbound connections to suspicious infrastructure such as 62.173.142.148


---

## 🔐 Prevention & Mitigation

* Block or restrict Windows Script Host where not required
* Enforce web filtering for malicious or low-reputation IP addresses
* Prevent execution of scripts from temporary and user download directories
* Use email and web gateway controls to inspect and block suspicious script attachments
* Enable endpoint protection rules for script-based malware and suspicious child-process behavior

---

## 💡 Lessons Learned

* Obfuscated JavaScript delivered over HTTP is a strong sign of malware staging
* Legitimate Windows binaries like wscript.exe are frequently abused for execution
* Threat-intelligence enrichment helps validate suspicious infrastructure and malware artifacts

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: Which IP address was used by the attacker during the initial access?       | 62.173.142.148    |
| Q2: What is the name of the malicious file used for initial access?       | allegato_708.js    |
| Q3: What is the SHA-256 hash of the malicious file used for initial access?      | 847b4ad90b1daba2d9117a8e05776f3f902dda593fb1252289538acf476c4268    |
| Q4: Which process was used to execute the malicious file?      | wscript.exe    |
| Q5: What is the file extension of the second malicious file utilized by the attacker?       | .dll    |
| Q6: What is the MD5 hash of the second malicious file?       |  E758E07113016ACA55D9EDA2B0FFEEBE    |

---
