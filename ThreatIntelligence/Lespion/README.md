# 🛡️ Security Writeup – Lespion

Investigate an insider threat by analyzing GitHub repositories for exposed credentials, using OSINT tools to correlate online accounts, and performing image analysis to identify locations.

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Threat Intel
* **Difficulty:** Easy
* **Date:** 01/04/2026

---

## 📖 Scenario

You have been tasked by a client whose network was compromised and brought offline to investigate the incident and determine the attacker's identity.

Incident responders and digital forensic investigators are currently on the scene and have conducted a preliminary investigation. Their findings show that the attack originated from a single user account, probably, an insider. 

---

## 🎯 Objectives

Investigate the incident, find the insider, and uncover the attack actions.

---

## 🧰 Tools & Techniques

* Tools: Google Maps, Google Image search, Sherlock

---



## 🔍 Analysis

* Viewing the latest repo in his github profile, an API key is shown in Login Page.js

<img width="1851" height="578" alt="image" src="https://github.com/user-attachments/assets/38ed947d-4943-4391-a5c7-9482b5b8e7e5" />

* In the same file, a password base64-encoded is posted directly to github. Using Cyberchef to decode this into a plaintext password

<img width="912" height="299" alt="Screenshot 2026-04-01 003731" src="https://github.com/user-attachments/assets/c993525c-ac5b-438c-acb1-ce256c02ffe7" />


<img width="1525" height="470" alt="image" src="https://github.com/user-attachments/assets/f187a335-8b75-486e-ac75-cc8771b1db39" />


* As we are looking for cryptocurrency mining tool being used by the insider threat, take a look at all of his repos. 

<img width="1127" height="580" alt="image" src="https://github.com/user-attachments/assets/ab149473-9f49-4a70-b592-aae38cca2561" />

* One of his repo is XMRig, which is XMRig High performance, open source, cross platform RandomX, CryptoNight, AstroBWT and Argon2 CPU/GPU miner, with official support for Windows.

* From his name and information about a gaming website account, we use google: EMarseille99 gaming website account and easily found his Steam account

<img width="959" height="184" alt="image" src="https://github.com/user-attachments/assets/e2786528-9ba6-431b-b551-37142648c301" />

* The insider's Instagram account can easily be found by searching for:  EMarseille99 Instagram

<img width="1529" height="455" alt="image" src="https://github.com/user-attachments/assets/941ac69c-87ef-47a9-80d4-e08739fa0250" />

* One of the post on Instagram reveal holiday's location. Using Edge's visual search to find information for the picture and the result is Marina bay in Singapore

<img width="1530" height="830" alt="image" src="https://github.com/user-attachments/assets/94dbd520-4527-4d37-9adb-39d806276e9c" />

<img width="1146" height="750" alt="image" src="https://github.com/user-attachments/assets/b7de2174-56c8-4ed5-b888-aae004032fd0" />

* The insider has 2 posts about the family's place.

<img width="1271" height="542" alt="image" src="https://github.com/user-attachments/assets/05bb92fb-408c-4473-9a8c-a2a4c16430b9" />

<img width="1522" height="652" alt="image" src="https://github.com/user-attachments/assets/0ccb7f01-9607-4005-8e3a-fc8234aa70f9" />

* Both results from visual search indicate that his family live in Dubai, one has UAE flag and one has a buliding seems like Burj Khalifa

<img width="1421" height="630" alt="image" src="https://github.com/user-attachments/assets/5bca1766-2194-407f-a4a2-e1ad42bfc649" />

<img width="904" height="737" alt="image" src="https://github.com/user-attachments/assets/5e308950-031b-4496-9753-bd5d6ecb5aa6" />

* Insert the image of office.jpg for Google Image Search shows that this place is in Birmingham

<img width="1561" height="718" alt="image" src="https://github.com/user-attachments/assets/17fcff45-8d9d-433e-ba3b-475cabc95f5f" />

* The view of this place is identified by Google as from Notra Dame University in Indiana, USA

<img width="1538" height="744" alt="image" src="https://github.com/user-attachments/assets/5e453340-db4a-4a02-920f-9bf2fae7c436" />

---

## 💡 Lessons Learned

Key lessons include:

* Public code repositories can expose highly sensitive secrets, including API keys and hardcoded passwords.
* The password should be keep as secret and hide somewhere that outsider can not reach.
* Reviewing all repositories associated with a suspect can reveal tooling, motives, or post-compromise actions such as cryptomining.
* Username reuse across platforms significantly increases attribution risk and enables rapid OSINT pivoting.
* Social media images can disclose travel history, family location, and other contextual intelligence through visual landmarks.
* Reverse image search remains highly effective for identifying unknown places from photos and surveillance imagery.
* Organizations should enforce secret scanning, credential hygiene, and continuous monitoring of employee public activity where legally and ethically appropriate.

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: File -> Github.txt: What API key did the insider add to his GitHub repositories?       |  aJFRaLHjMXvYZgLPwiJkroYLGRkNBW    |
| Q2: File -> Github.txt: What plaintext password did the insider add to his GitHub repositories?       | PicassoBaguette99    |
| Q3: File -> Github.txt: What cryptocurrency mining tool did the insider use?       | XMRig    |
| Q4: On which gaming website did the insider have an account?       | Steam    |
| Q5: What is the link to the insider Instagram profile?       | (https://www.instagram.com/EMarseille99/)    |
| Q6: Which country did the insider visit on her holiday?       | Singapore    |
| Q7: Which city does the insider family live in?       | Dubai    |
| Q8: File -> office.jpg: You have been provided with a picture of the building in which the company has an office. Which city is the company located in?       | Birmingham    |
| Q9: File -> Webcam.png: With the intel, you have provided, our ground surveillance unit is now overlooking the person of interest suspected address. They saw them leaving their apartment and followed them to the airport. Their plane took off and landed in another country. Our intelligence team spotted the target with this IP camera. Which state is this camera in?       | Indiana    |

---
