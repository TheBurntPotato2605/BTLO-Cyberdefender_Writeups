# 🛡️ Security Writeup – Network Analysis - Ransomware

## 📌 Overview

* **Platform:** BTLO
* **Category:** Network Analysis
* **Difficulty:** Medium
* **Date:** 05/05/2026

---

## 📖 Scenario

ABC Industries worked day and night for a month to prepare a tender document for a prestigious project that would secure the company’s financial future. The company was hit by ransomware, believed to be conducted by a competitor, and the final version of the tender document was encrypted. Right now they are in need of an expert who can decrypt this critical document. All we have is the network traffic, the ransom note, and the encrypted ender document. Do your thing Defender!​

---

## 🎯 Objectives

Decrypt the critical document

---

## 🧰 Tools & Techniques

* Tools: Wireshark, VirusTotal, TeslaDecoder


---



## 🔍 Analysis

* Take a look at Capture File Properties section of Wireshark, the operating system of the host from which the network traffic was captured is 32-bit Windows 7 Service Pack 1, build 7601. So the victim is a Windows machine.

  <img width="1157" height="606" alt="image" src="https://github.com/user-attachments/assets/d3c88e8f-7ed4-4677-8542-ff1bb5fc1fd7" />

* To have a more accurate overview, I examine the Conversations sections. And as we can see below, the IP address of 10.0.2.4 is the most active host with most packets and data exchange. This helps us identify where to focus in our investigation 

  <img width="1577" height="263" alt="image" src="https://github.com/user-attachments/assets/cb4993a9-aaca-4c03-b53f-232c72a66c03" />
  <img width="1669" height="589" alt="image" src="https://github.com/user-attachments/assets/66ac976c-59f8-49c1-b94a-9e47bf4a273c" />
  <img width="1680" height="259" alt="image" src="https://github.com/user-attachments/assets/78ebd62e-9d90-486a-a0d3-4fec45885d00" />

* We are informed that the company was attacked by ransomware so the ransomware executable file will be downloaded by the malicious actor to encrypt files. In the Wireshark, we filter for the IP address above and HTTP method GET. The hacker downloaded the .exe file from 10.0.2.15

  <img width="1403" height="493" alt="image" src="https://github.com/user-attachments/assets/29999a8c-61ce-4bec-97a2-235640aeef7f" />

* To obtain more information about the ransomware, I export the executable file and check for the MD5 hash value.

  <img width="739" height="157" alt="image" src="https://github.com/user-attachments/assets/9d7d56c7-a72a-4ea3-852d-05c4e694a288" />
  &nbsp;
  <img width="405" height="66" alt="image" src="https://github.com/user-attachments/assets/fd0bcd15-c67e-4bda-81b5-72bc6895602b" />

* Paste this hash value to VirusTotal, it indicates that this ransomware is teslacrypt

  <img width="1747" height="515" alt="Screenshot 2026-05-06 003239" src="https://github.com/user-attachments/assets/30118253-4f20-49bf-88cc-9b9c210b571f" />

* According to the ransom note,  the encryption algorithm used by the ransomware is RSA-4096

  <img width="1064" height="224" alt="image" src="https://github.com/user-attachments/assets/c96084c2-b621-4993-8953-589417b05948" />

* Back to network traffic, use this filter to find the domain beginning with ‘d’ that is related to ransomware traffic

  <img width="1170" height="143" alt="image" src="https://github.com/user-attachments/assets/5a3179d7-054a-4f46-8fb7-327f98026f99" />

* If we want to decrypt the critical document here we have to obtain both public key and private key. The problem here is the private key is kept by the malicious actor on their secret server and we are only provided with public key so it's impossible for us to decrypt it without the private key.

  <img width="472" height="247" alt="image" src="https://github.com/user-attachments/assets/fc0406ed-8712-4072-a096-7923f0823131" />

* Luckily, ESET researchers able to got the masterkey and defeat teslacrypt ransomware. Here, the hackers public the masterkey allow cybersecurity expert to come up with decryptors for this ransomware 

  <img width="797" height="643" alt="image" src="https://github.com/user-attachments/assets/118dbc73-2981-4435-8524-5b1fcdcd7929" />

* Downloading TeslaDecoder and start decrypting our critical document

  <img width="978" height="452" alt="image" src="https://github.com/user-attachments/assets/632ec020-64e1-44f2-987d-fa49db2d3c93" />

* Insert the folder contain the encrypted file along with the masterkey they have public, wait a minute and the decrypted file will replace the encrypted file.

  <img width="706" height="426" alt="image" src="https://github.com/user-attachments/assets/78f4561f-4047-46fa-9c74-9812c532dca5" />

  <img width="696" height="420" alt="image" src="https://github.com/user-attachments/assets/831fc049-575c-424b-8a74-ebfec513bbb3" />

* Finally, we have content of the critical document and also the flag of the challenge

  <img width="620" height="188" alt="image" src="https://github.com/user-attachments/assets/533589b0-a46f-49fd-8e3e-a740bff5861f" />

  <img width="601" height="480" alt="image" src="https://github.com/user-attachments/assets/bd7539f7-5289-4371-8e3e-da16783589d0" />


  

---

## 🧾 Key Findings


* Victim OS: 32-bit Windows 7 SP1 (build 7601) – outdated and vulnerable

* Infection vector: safecrypt.exe downloaded via HTTP from 10.0.2.15[:]8000

* Ransomware: TeslaCrypt (MD5: 4a1d88603b1007825a9c6b36d1e5de44)

* Encryption: RSA-4096, no private key in traffic

* Malicious domain: dunyamuzelerimuzesi.com 

* Decryption method: Used TeslaDecoder and public masterkey

* Flag recovered: BTLO-T3nd3r-Fl@g






---

## 💡 Lessons Learned

* Identify ransomware early – Hash lookups (VirusTotal) enable use of existing decryption tools.

* Public decryptors can save the day when masterkeys are available.

* Outdated OS = high risk – Windows 7 SP1 increased exposure; patching and segmentation reduce impact.


---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the operating system of the host from which the network traffic was captured? (Look at Capture File Properties, copy the details exactly)      | 32-bit Windows 7 Service Pack 1, build 7601    |
| Q2: What is the full URL from which the ransomware executable was downloaded?      | (http[:]//10.0.2.15[:]8000/safecrypt.exe)    |
| Q3: Name the ransomware executable file?     | safecrypt.exe    |
| Q4: What is the MD5 hash of the ransomware?      | 4a1d88603b1007825a9c6b36d1e5de44    |
| Q5: What is the name of the ransomware?      | teslacrypt    |
| Q6: What is the encryption algorithm used by the ransomware, according to the ransom note?       | RSA-4096    |
| Q7: What is the domain beginning with ‘d’ that is related to ransomware traffic?       | dunyamuzelerimuzesi.com    |
| Q8: Decrypt the Tender document and submit the flag       | BTLO-T3nd3r-Fl@g    |

---


