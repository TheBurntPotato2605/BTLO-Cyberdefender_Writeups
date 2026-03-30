# 🛡️ Security Writeup – RamnitLab

Analyze a memory dump using Volatility to identify a malicious process, extract network IOCs, file hash, and compilation timestamp, correlating with external threat intelligence.

## 📌 Overview

* **Platform:** Cyberdefender
* **Category:** Endpoint Forensic
* **Difficulty:** Easy
* **Date:** 28/03/2026

---

## 📖 Scenario

Our intrusion detection system has alerted us to suspicious behavior on a workstation, pointing to a likely malware intrusion. A memory dump of this system has been taken for analysis. 

---

## 🎯 Objectives

Your task is to analyze this dump, trace the malware’s actions, and report key findings.

---

## 🧰 Tools & Techniques

* Tools: Volatility3, Virustotal
---


## 🔍 Analysis

* First, we have to identify the suspicious process in this memory dump and investigate further. As reviewing pstree and pslist doesn't reveal anything useful for our investigation, i use netstat and realize some suspicious connection

* <img width="934" height="543" alt="image" src="https://github.com/user-attachments/assets/5431f000-b628-49c8-a7c9-e394001fc141" />

As we know, in TCP three-way handshake, a sender want to establish a connection to a target must send a SYN first. If they agree they will send back a SYN ACK meaning i can see you and finally the sender will send  ACK. After that, they can communicate and the state will be changed to ESTABLISHED. Here, the process ChromeSetup.exe send SYN to IP address of 58.64.204.181 on port 5202. This is quite suspicious as why a setup executable file for a browser has to establish a connection to external IP with a non-popular port like 5202.

* Using IP reputation tool like AbuseIPDB to search for this suspicious IP, the report shows that this IP maybe used for scan and hacking purpose.

  <img width="1520" height="337" alt="image" src="https://github.com/user-attachments/assets/a9a2b514-892d-4470-be6f-300f6fa05b73" />

* Further investigate use the process's hash with Virustotal show that this is flagged as suspicious by 64/72 vendors

  <img width="1914" height="899" alt="image" src="https://github.com/user-attachments/assets/c4adaa01-1268-4818-9d5a-b54d273d1164" />



---

### Key Artifact Identification

* Indicator 1: SYN SENT of ChromeSetup.exe
* Indicator 2: Uncommon port 5202



---

## 🧬 Threat Context 

* **Tactic:** Execution, Defense Evasion, Command and Control
* **Technique:** T1024, T1036, T1071

---


## 💡 Lessons Learned

* Review every plugins if possible when you have no idea of the malicious activity
* Always check for suspicious IP/Port even if it s from the legit process
* The hash of the process sometimes can reveal useful things for our investigation, especially when combine with Virustotal

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the name of the process responsible for the suspicious activity?       |  ChromeSetup.exe   |
| Q2: What is the exact path of the executable for the malicious process?       |  C:\Users\alex\Downloads\ChromeSetup.exe   |
| Q3: Identifying network connections is crucial for understanding the malware's communication strategy. What IP address did the malware attempt to connect to?       |  58.64.204.181   |
| Q4: To determine the specific geographical origin of the attack, Which city is associated with the IP address the malware communicated with?       | Hong Kong    |
| Q5: Hashes serve as unique identifiers for files, assisting in the detection of similar threats across different machines. What is the SHA1 hash of the malware executable?      |  280c9d36039f9432433893dee6126d72b9112ad2  |
| Q6: Examining the malware's development timeline can provide insights into its deployment. What is the compilation timestamp for the malware?       |  2019-12-01 08:36   |
| Q7: Identifying the domains associated with this malware is crucial for blocking future malicious communications and detecting any ongoing interactions with those domains within our network. Can you provide the domain connected to the malware?       | dnsnb8.net    |

---

