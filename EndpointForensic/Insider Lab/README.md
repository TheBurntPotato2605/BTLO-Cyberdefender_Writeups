# 🛡️ Security Writeup – Insider Lab

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Endpoint Forensic
* **Difficulty:** Easy
* **Date:** 18/04/2026

---

## 📖 Scenario

After Karen started working for 'TAAUSAI,' she began doing illegal activities inside the company. 'TAAUSAI' hired you as a soc analyst to kick off an investigation on this case.

You acquired a disk image and found that Karen uses Linux OS on her machine. Analyze the disk image of Karen's computer and answer the provided questions.

---

## 🎯 Objectives

Analyze Linux disk image artifacts, including logs and Bash history, using FTK Imager to investigate insider threat activities and reconstruct user actions.

---

## 🧰 Tools 

* Tools: FTK Imager


---


## 🔍 Analysis

* Explore the evidence tree, some regular files indicate that Kali Linux is used on this machine.

  <img width="948" height="291" alt="image" src="https://github.com/user-attachments/assets/ec0ac3fd-f8bd-4e1f-b240-97f70e269cf0" />

* Export the access.log file of Apache and we have its MD5 hash value

  <img width="661" height="293" alt="image" src="https://github.com/user-attachments/assets/e632f14d-afaa-4e2d-8d84-a65ce2984280" />

  <img width="605" height="105" alt="image" src="https://github.com/user-attachments/assets/145db5ab-5905-4fe6-975f-051f5d60d24b" />

* It is suspected that a credential dumping tool was downloaded. We have to check for Downloads folder to examnine which tool is installed. mimikatz is used to extract plaintexts passwords, hash, PIN code and kerberos tickets from memory. It can also perform pass-the-hash, pass-the-ticket or build Golden tickets.

  <img width="943" height="282" alt="image" src="https://github.com/user-attachments/assets/5dcf9c19-eb52-4e0f-b89f-15c30abdd638" />

* When users create files and directories, their commands are often logged. In the bash_history hidden file, we can see that a SuperSecretFile.txt was created

  <img width="963" height="490" alt="image" src="https://github.com/user-attachments/assets/af927b75-fdaf-4b7d-98d1-11dd2b9bfea1" />

* In the bash_history file, didyouthinkwedmakeiteasy.jpg file is used with binwalk during its execution.
  
  <img width="643" height="109" alt="image" src="https://github.com/user-attachments/assets/243fa77c-256f-40a7-8588-88433aa8394a" />

* Users often store checklists and notes on their desktop so we will have a look at Desktop folder. And there is a file named "Checklist" in the Desktop folder
  
  <img width="954" height="288" alt="image" src="https://github.com/user-attachments/assets/43357f95-668a-4b21-9cb6-6b556b049f1d" />
  
  <img width="651" height="118" alt="image" src="https://github.com/user-attachments/assets/e2e7fc99-9584-4a97-a7f4-781dea3dc0cb" />


* The logs in apache2 all have a size of 0 bytes, indicating that Apache was never run on this system.

  <img width="951" height="373" alt="image" src="https://github.com/user-attachments/assets/6c784426-3a1f-484c-a9dc-4a59f3beea60" />

* In the root folder, we found a .JPEG file with a quite suspicious name and it looks like an attack conducted by this machine

  <img width="932" height="636" alt="image" src="https://github.com/user-attachments/assets/d115c4e6-42b8-4b8b-a98d-94b455a85ab5" />

* It is believed that Karen was taunting a fellow computer expert through a bash script within the Documents directory. In the Documents folder, there is a folder named "myfirsthack" which maybe an evidence for our investigation. The script below seems to be used to taunt someone name Young

  <img width="961" height="470" alt="image" src="https://github.com/user-attachments/assets/f6a5b8a4-e32b-4f07-b40d-437a2cda86f3" />

* To find out who switched to root, we check the system's authentication logs. The auth.log file contains records of all su commands in Linux. In the given timestamp, the user postgress executed the su command to gain root access multiple times.

  <img width="744" height="753" alt="image" src="https://github.com/user-attachments/assets/6707fe21-ce6f-453e-84b8-8a06eae0055a" />

* From the most recent commands, it is revealed that the current working directory is /root/Documents/myfirsthack/
  
  <img width="668" height="577" alt="image" src="https://github.com/user-attachments/assets/63021644-7759-4e70-872b-2663b50b4387" />

---





## 💡 Lessons Learned

* Even simple Linux artifacts such as .bash_history, Desktop notes, and authentication logs can provide strong evidence of intent and user behavior.
* Empty log files can still be meaningful when confirming that a service was not actively used.
* Privilege escalation traces in auth.log are critical for identifying which account gained elevated access.
* User-created folders, scripts, and working directories often reveal both technical actions and attacker mindset.

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: Which Linux distribution is being used on this machine?      | Kali    |
| Q2: What is the MD5 hash of the Apache access.log file?      | d41d8cd98f00b204e9800998ecf8427e    |
| Q3: It is suspected that a credential dumping tool was downloaded. What is the name of the downloaded file?      | mimikatz_trunk.zip    |
| Q4: A super-secret file was created. What is the absolute path to this file?      | /root/Desktop/SuperSecretFile.txt    |
| Q5: What program used the file didyouthinkwedmakeiteasy.jpg during its execution?      | binwalk    |
| Q6: What is the third goal from the checklist Karen created?      | profit    |
| Q7: How many times was Apache run?      | 0    |
| Q8: This machine was used to launch an attack on another. Which file contains the evidence for this?      | irZLAohL.jpeg    |
| Q9: It is believed that Karen was taunting a fellow computer expert through a bash script within the Documents directory. Who was the expert that Karen was taunting?     | young    |
| Q10: A user executed the su command to gain root access multiple times at 11:26. Who was the user?      | postgres    |
| Q11: Based on the bash history, what is the current working directory?      | /root/Documents/myfirsthack/    |

---

