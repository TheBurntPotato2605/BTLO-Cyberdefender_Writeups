# 🛡️ Security Writeup – Malicious Powershell Analysis

## 📌 Overview

* **Platform:** BTLO
* **Category:** Security Operations
* **Difficulty:** Medium
* **Date:** 30/06/2026

---

## 📖 Scenario

Recently the networks of a large company named GothamLegend were compromised after an employee opened a phishing email containing malware. The damage caused was critical and resulted in business-wide disruption. GothamLegend had to reach out to a third-party incident response team to assist with the investigation. You are a member of the IR team - all you have is an encoded Powershell script. 

---

## 🎯 Objectives

Decode the Powershell script and identify what malware is responsible for this attack

---

## 🧰 Tools & Techniques

* Tools: Cyberchef

---



## 🔍 Analysis

* Firstly, take a look at given Powershell script. We can easily see that the text only consists a mess of uppercase letters, lowercase letters and numbers with no standard code punctuation. Moreover, the letter "A" is repeated after some characters, this maybe the blank space is converted into Base64. These evidence maybe the signs that this text is Base64-encoded 

 <img width="1134" height="741" alt="image" src="https://github.com/user-attachments/assets/29e87c3d-2054-4a12-8003-f6bff675d9aa" />

* Using Cyberchef to decode we have the following text file

  <img width="905" height="729" alt="image" src="https://github.com/user-attachments/assets/c8caef2e-753a-477e-8c91-5b4d0baeaf56" />

  <img width="656" height="453" alt="image" src="https://github.com/user-attachments/assets/8628aeef-41e0-4532-b228-178c5a453ae4" />

* Once decoded, I see a lot of strange formatting as shown above. The owner of this script might use the back tick character (') as it is escape character in Powershell. If it is placed in the middle of a command, it will be ignored and still run while antivirus scanner may fail to identify it. After using nano to find and delete all the backtick characters, we have the new problem:

  <img width="637" height="379" alt="image" src="https://github.com/user-attachments/assets/7462ce5d-93b2-4b05-a560-e56c6f6f4d9c" />

* Now we can see that there are hundreds of strings brake and stick together using plus sign. This make us think this is a mess but the + is just a string concatenation so I use nano to clean all of them again

  <img width="633" height="347" alt="image" src="https://github.com/user-attachments/assets/f651d1b5-b49c-4084-93ad-c89eb87d592f" />

* After that, the massive -f format operator block is still holding the malicious URL and command. We resolve them using Python's .format tool. A python script is used to solve the file to a readable format and explain in the comment.

  <img width="734" height="453" alt="image" src="https://github.com/user-attachments/assets/1a57a5ea-a7cb-46ad-9174-1c92e68479b9" />

  <img width="743" height="484" alt="image" src="https://github.com/user-attachments/assets/afa6bd39-0909-48f1-979d-63751a58f365" />

* Based on the analysis of the obfuscated code, the name of malware is emotet due to URLhaus

  <img width="1223" height="79" alt="image" src="https://github.com/user-attachments/assets/f7df6e24-8b49-4d2b-b436-21cd54092ba0" />

---


## 🧾 Key Findings

* Evasion: Uses backticks and -f formatting to bypass static detection; suppresses errors with $ErrorActionPreference.

* Persistence Setup: Creates the hidden directory %HOME%\Db_bh30\Yf5be5g\ to stage the payload.

* C2 Infrastructure: Hardcoded list of 7 compromised domains (e.g., admintk.com, mikegeerinck.com, wm.mcdevelop.net).

* Network Security: Enforces TLS 1.2 for outbound communication.

* Payload Delivery: Downloads A69S.dll using WebClient, verifies file size ≥ 35,698 bytes, then executes via rundll32.exe to load the DLL.

* Attribution: The domains, execution chain, and structure match Emotet .





---



## ❓ Answers

  <img width="1208" height="675" alt="image" src="https://github.com/user-attachments/assets/4ff817cb-9379-4568-b5be-f95f14579b68" />


---
