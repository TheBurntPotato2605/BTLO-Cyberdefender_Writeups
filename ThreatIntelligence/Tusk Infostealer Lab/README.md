# 🛡️ Security Writeup – Tusk Infostealer Lab


## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Threat Intelligence
* **Difficulty:** Easy
* **Date:** 21/04/2026

---

## 📖 Scenario

A blockchain development company detected unusual activity when an employee was redirected to an unfamiliar website while accessing a DAO management platform. Soon after, multiple cryptocurrency wallets linked to the organization were drained. Investigators suspect a malicious tool was used to steal credentials and exfiltrate funds.

---

## 🎯 Objectives

Analyze threat intelligence and malware configuration to identify TTPs, extract IOCs, and track cryptocurrency flow of the Tusk Infostealer campaign.

---

## 🧰 Tools & Techniques

* Tools: SECURELIST by Kaspersky

---



## 🔍 Lab Walkthrough

* The size of the malicious file is 921.36kB as mentioned in the report.

  <img width="1502" height="601" alt="image" src="https://github.com/user-attachments/assets/b25688d3-40de-4e34-82a7-038b56696fab" />

* As the threat actor uses the word “Mammoth” in log messages of initial downloaders — at least in the three active sub-campaigns we analyzed. “Mammoth” is slang used by Russian-speaking threat actors to refer to victims. Mammoths used to be hunted by ancient people and their tusks were harvested and sold.

  <img width="985" height="308" alt="image" src="https://github.com/user-attachments/assets/4cfcbacb-c32b-4a3a-9eb0-abc5bb4a52a6" />

* It is said in the report that the malicious website is tidyme[.]io.

  <img width="938" height="237" alt="image" src="https://github.com/user-attachments/assets/621cc7e1-1665-48a5-833b-ab6acba53202" />

* This campaign has several malware samples for macOS and Windows, both hosted on Dropbox.

  <img width="986" height="581" alt="image" src="https://github.com/user-attachments/assets/d3eab6d1-8b9c-4e4d-b380-64ae96e46a18" />

* The tidyme.exe sample contains a configuration file called config.json which contains base64-encoded URLs and a password for archived data decompression, which is used to download the second-stage payloads.

  <img width="987" height="475" alt="image" src="https://github.com/user-attachments/assets/57dd18ab-c56a-45d2-b287-b916f326a959" />

* The function downloadAndExtractArchive retrieves the field archive from the configuration file, which is an encoded Dropbox link, decodes it and stores the file from Dropbox to the path %TEMP%/archive-<RANDOM_STRING>.

  <img width="935" height="403" alt="image" src="https://github.com/user-attachments/assets/368a758c-dab8-4c22-9b4d-ccaef400855e" />

* In this campaign, the threat actor was simulating an AI translator project named YOUS. The original website is yous.ai, while the malicious website is voico[.]io

  <img width="964" height="360" alt="image" src="https://github.com/user-attachments/assets/141af6bb-4b2b-41ff-bceb-1fc7c157c508" />

*  In our analysis we observed that all the active sub-campaigns host the initial downloader on Dropbox. This downloader is responsible for delivering additional malware samples to the victim’s machine, which are mostly infostealers (Danabot and StealC) and clippers. 

  <img width="734" height="233" alt="image" src="https://github.com/user-attachments/assets/c2f8e228-87d5-4563-bc3c-047797927f37" />

  <img width="1000" height="758" alt="image" src="https://github.com/user-attachments/assets/0004b69f-efd2-49e0-b9f2-06abd39c8293" />

  <img width="1007" height="726" alt="image" src="https://github.com/user-attachments/assets/e4e3ee89-d2c2-409f-a917-16a9ce6b9fc3" />

* In addition to distributing malware, this campaign involves victims connecting their cryptocurrency wallets directly through the campaign’s website. This campaign also utilizes infostealers to steal software-based cryptocurrency wallets which could be used to gain access to the victim’s funds

  <img width="754" height="339" alt="image" src="https://github.com/user-attachments/assets/c414043f-64c5-4da4-9fab-e6078a8e1013" />


---

### Key Artifact Identification

| Artifact | Value |
|----------|-------|
| Malicious file size | 921.36 KB |
| Victim slang term | Mammoth |
| Fake DAO website | tidyme[.]io |
| Cloud storage | Dropbox |
| Archive password | newfile2024 |
| Download function | downloadAndExtractArchive |
| Legitimate AI translator | yous[.]ai |
| Fake AI translator | voico[.]io |
| StealC C2 IPs | 46.8.238.240, 23.94.225.177 |
| Ethereum wallet | 0xaf0362e215Ff4e004F30e785e822F7E20b99723A |

---



## 🗺️ Attack Flow / Timeline

### 1. Victim redirected to tidyme[.]io (fake DAO platform).

### 2. tidyme.exe (921.36 KB) downloaded from Dropbox.

### 3. Executable reads config.json, decodes Dropbox URL.

### 4. Calls downloadAndExtractArchive to fetch second‑stage archive.

### 5. Archive decompressed using password newfile2024.

### 6. StealC (C2s: 46.8.238.240, 23.94.225.177) and Danabot deployed.

### 7. Infostealers harvest software‑based cryptocurrency wallets.

### 8. Funds drained to Ethereum address 0xaf0362e215Ff4e004F30e785e822F7E20b99723A.

---

## 🧬 Threat Context 

| Tactic | Technique | ID | Description |
|--------|-----------|----|-------------|
| Initial Access | Spearphishing Link | T1566.002 | Redirect to malicious `tidyme[.]io` |
| Execution | User Execution | T1204 | Victim runs downloaded executable |
| Defense Evasion | Obfuscated Files/Info | T1027 | Base64‑encoded URLs in config.json |
| Command & Control | Ingress Tool Transfer | T1105 | Payloads hosted on Dropbox |
| Credential Access | Credentials from Password Stores | T1555 | StealC steals crypto wallets |
| Exfiltration | Exfiltration Over C2 Channel | T1041 | Stolen data sent to StealC C2s |
| Impact | Financial Theft | – | Cryptocurrency drained to attacker wallet |

---

## 🛡️ Detection Opportunities

* File creation in %TEMP%\archive-* followed by process execution.

* Command line containing downloadAndExtractArchive or newfile2024.

* Network connections to Dropbox download links (monitor for dl.dropboxusercontent.com with suspicious file names).

* YARA rule for config.json with base64 and password newfile2024.

---

## 🔐 Prevention & Mitigation

* Application allowlisting – Block execution of unsigned executables from %TEMP%.

* Network controls – Block known malicious IPs (46.8.238.240, 23.94.225.177) and Dropbox sharing links used in campaigns.

* User awareness – Train employees to verify DAO platform URLs; avoid clicking shortened or unexpected redirects.

* EDR / AV – Ensure signatures for StealC and Danabot are up to date.

* Cryptocurrency security – Use hardware wallets for organisational funds; monitor for unexpected outgoing transactions.

---



## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: In KB, what is the size of the malicious file?       | 921.36    |
| Q2: What word do the threat actors use in log messages to describe their victims, based on the name of an ancient hunted creature?     | Mammoth    |
| Q3: The threat actor set up a malicious website to mimic a platform designed for creating and managing decentralized autonomous organizations (DAOs) on the MultiversX blockchain (peerme.io). What is the name of the malicious website the attacker created to simulate this platform?      | TidyMe[.]io    |
| Q4: Which cloud storage service did the campaign operators use to host malware samples for both macOS and Windows OS versions?      | Dropbox    |
| Q5: The malicious executable contains a configuration file that includes base64-encoded URLs and a password used for archived data decompression, enabling the download of second-stage payloads. What is the password for decompression found in this configuration file?      | newfile2024    |
| Q6: What is the name of the function responsible for retrieving the field archive from the configuration file?      | downloadAndExtractArchive    |
| Q7: In the third sub-campaign carried out by the operators, the attacker mimicked an AI translator project. What is the name of the legitimate translator, and what is the name of the malicious translator created by the attackers?      | yous[.]ai, voico[.]io    |
| Q8: The downloader is tasked with delivering additional malware samples to the victim’s machine, primarily infostealers like StealC and Danabot. What are the IP addresses of the StealC C2 servers used in the campaign?      | 46.8.238.240,23.94.225.177    |
| Q9: What is the address of the Ethereum cryptocurrency wallet used in this campaign?      | 0xaf0362e215Ff4e004F30e785e822F7E20b99723A    |

---

