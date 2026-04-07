# 🛡️ Security Writeup – Meta

## 📌 Overview

* **Platform:** BTLO
* **Category:** Digital Forensic
* **Difficulty:** Easy
* **Date:** 07/04/2026

---

## 📖 Scenario

The attached images were posted by a criminal on the run, with the caption "I'm roaming free. You will never catch me". We believe you can assist us in proving him wrong.

---


## 🧰 Tools & Techniques

* Tools: Exiftool, Google Images
* Techniques:
    * EXIF metadata extraction
    * Timeline analysis
    * Open Source Intelligence (OSINT)
    * Image geolocation


---


## 🔍 Analysis

* The camera model is a digital fingerprint of the device that took the photo. It helps investigators prove authenticity, connect evidence, and sometimes even trace the suspect’s hardware. We use Exiftool to check for criminal's camera model and here is the result

<img width="628" height="75" alt="image" src="https://github.com/user-attachments/assets/5afc22be-cfe2-4815-8e65-a2a0df18d789" />

* Checking for the Date time the photo was taken can reveal suspect's timeline matches the evidence and compare time across his photos , reconstruct a sequence of actions.

<img width="629" height="75" alt="image" src="https://github.com/user-attachments/assets/741857e6-b635-4f1b-a363-2ad913faa8ec" />

* We check comment tag because maybe the criminal leave hidden notes, identifiers, or even clues in it.

<img width="627" height="77" alt="image" src="https://github.com/user-attachments/assets/ce3e2205-0233-4f36-a0a0-c832cebfbf8e" />

* After using Google Image to search for his 2 images, we identify that these pictures was taken in Kathmandu, Nepal and maybe that is the location of the criminal

<img width="1153" height="700" alt="image" src="https://github.com/user-attachments/assets/60a65953-17f5-4f09-a27b-bc90e1bd2639" />


<img width="1105" height="687" alt="image" src="https://github.com/user-attachments/assets/ca9e095b-686a-4af5-84c2-d8da6b990a99" />

---



## 🧾 Key Findings


* Camera model identified as Canon EOS 550D
* Image taken time: 2021:11:02 13:20:23
* Embedded comment contains a comment from the criminal
* Location identified as Kathmandu, Nepal

---



## 💡 Lessons Learned

* EXIF metadata can reveal critical forensic evidence such as device information, timestamps, and hidden data.
* OSINT techniques such as reverse image search are powerful for geolocation.
* Always consider formatting requirements in CTF challenges, as correct answers may depend on exact string formatting.

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the camera model       | Canon xxx    |
| Q2: When was the picture taken       | 2021-xxx    |
| Q3: What does the comment on the first image says?       | rely xxx    |
| Q4: Where could the criminal be?       | near Himalaya?    |


---

