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



---

### Key Artifact Identification

* Indicator 1: 
* Indicator 2: 

👉 Significance:

* [Why these matter]

---



## 🗺️ Attack Flow / Timeline


---

## 🧬 Threat Context (Optional but Strong)

* **Tactic:** Execution, Defense Evasion, Command and Control
* **Technique:** 

---

## 🛡️ Detection Opportunities

* Monitor for:

  * Unusual patterns or anomalies
  * Suspicious access or behavior
* Create alerts for:

  * Known indicators
  * Abnormal activity patterns

---


## 💡 Lessons Learned

* Key takeaway from the investigation
* What could have prevented or detected this earlier

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

