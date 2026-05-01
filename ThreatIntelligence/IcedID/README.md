# 🛡️ Security Writeup – IcedID

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Threat Intelligence
* **Difficulty:** Easy
* **Date:** 02/05/2026

---

## 📖 Scenario

A cyber threat group was identified for initiating widespread phishing campaigns to distribute further malicious payloads. The most frequently encountered payloads were IcedID. You have been given a hash of an IcedID sample to analyze and monitor the activities of this advanced persistent threat (APT) group.

---

## 🎯 Objectives

Investigate IcedID malware using VirusTotal and threat intelligence platforms to identify IOCs, associated threat actors, and execution mechanisms.

---

## 🧰 Tools 
* Tools: VirusTotal, MITRE ATT&CK

---



## 🔍 Analysis

* Begin by analyzing the hash on VirusTotal. Check the “Details” tab on VirusTotal, where file metadata, including the original filename, is often listed.
* These are the names of which the file has been submitted

  <img width="580" height="194" alt="image" src="https://github.com/user-attachments/assets/38a59cb0-322f-4b36-ad7c-1afd75f82a1c" />

* Explore the file’s relationships. In VirusTotal’s “Relations” tab, examine requests to and from this file, especially looking for files with repetitive requests. Here, we can see that 3003.gif was contacted multiple times.

  <img width="758" height="290" alt="image" src="https://github.com/user-attachments/assets/8628a806-2dfc-489f-a21c-aab498755fcc" />

* Review all network connections associated with the GIF file. There are 5 different domains the gift file connected to for additional downloads.

  <img width="505" height="331" alt="image" src="https://github.com/user-attachments/assets/359a8f7c-0b24-4299-af4d-c5a0ff30b012" />

*  A DNS registrar named NameCheap was predominantly used by the threat actor to host their harmful content, enabling the malware's functionality. It is used by one of the 5 domains above

    <img width="863" height="468" alt="image" src="https://github.com/user-attachments/assets/435d2cc5-76d7-47d7-baae-64a038dddb96" />

* Looking up IcedID on MITRE ATT&CK framework, it is used by groups with ID TA551

  <img width="1702" height="536" alt="image" src="https://github.com/user-attachments/assets/6f2e3e98-71eb-4d3b-817c-d0ef7736a1ea" />

  <img width="1431" height="665" alt="image" src="https://github.com/user-attachments/assets/cd9e3620-d637-44fc-9b92-7b2b91293501" />

* In the activity summary of malware, in the execution phase, the malware employ UrlDownloadToFile function to fetch extra payloads onto the system.

  

  <img width="1136" height="732" alt="Screenshot 2026-05-02 012158" src="https://github.com/user-attachments/assets/dfbe54b6-0d2e-4719-bed7-0de8f08919bc" />
   


---


## 🧾 Key Findings

* A malicious Excel file named document-1982481273.xlsm containing macro code .

* Dropped payload: The macro downloaded a file disguised as 3003.gif, which is actually a 64-bit IcedID DLL.

* C2 infrastructure: The malware contacted 5 different domains to download additional payloads. One of the domains used NameCheap as the DNS registrar.

* Associated threat actor: The sample is linked to the threat group GOLD CABIN (also known as TA551).

* Execution technique: During the execution phase, IcedID uses the Windows API function UrlDownloadToFile to fetch extra payloads onto the compromised system.

---



## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the name of the file associated with the given hash?      | document-1982481273.xlsm    |
| Q2: Can you identify the filename of the GIF file that was deployed?      | 3003.gif    |
| Q3: How many domains does the malware look to download the additional payload file in Q2?      | 5    |
| Q4: From the domains mentioned in Q3, a DNS registrar was predominantly used by the threat actor to host their harmful content, enabling the malware's functionality. Can you specify the Registrar INC?      | NameCheap    |
| Q5: Could you specify the threat actor linked to the sample provided?      | GOLD CABIN    |
| Q6: In the Execution phase, what function does the malware employ to fetch extra payloads onto the system?      | UrlDownloadToFile  |

---

