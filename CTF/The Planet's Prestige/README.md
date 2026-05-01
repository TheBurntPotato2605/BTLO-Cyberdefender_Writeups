# 🛡️ Security Writeup – The Planet's Prestige

## 📌 Overview

* **Platform:** BTLO
* **Category:** CTF
* **Difficulty:** Easy
* **Date:** 01/05/2026

---

## 📖 Scenario

CoCanDa, a planet known as 'The Heaven of the Universe' has been having a bad year. A series of riots have taken place across the planet due to the frequent abduction of citizens, known as CoCanDians, by a mysterious force. CoCanDa’s Planetary President arranged a war-room with the best brains and military leaders to work on a solution. After the meeting concluded the President was informed his daughter had disappeared. CoCanDa agents spread across multiple planets were working day and night to locate her. Two days later and there’s no update on the situation, no demand for ransom, not even a single clue regarding the whereabouts of the missing people. On the third day a CoCanDa representative, an Army Major on Earth, received an email.

---



## 🧰 Tools & Techniques

* Tools: Thunderbird, Exiftool


---



## 🔍 Analysis

* Viewing the source of the email, we have the Received section with emkei.cz - This is the mail server domain that actually sent the message. Emkei.cz is a known web‑based fake mailer service often used for spoofing.

  <img width="629" height="75" alt="image" src="https://github.com/user-attachments/assets/081cd378-b351-4e9d-bf4a-3cd544414fcb" />

* From: "Bill" <billjobs@microapple[.]com>  This is the claimed sender address. The domain is microapple.com looks like a custom or spoofed domain.
* Reply-To: negeja3921@pashter[.]com  This is where replies would actually go. Attackers often use a different Reply-To to redirect responses away from the sender.

  <img width="510" height="170" alt="image" src="https://github.com/user-attachments/assets/d77b7434-9fac-48a5-8051-c0e4a3b5977b" />

* The malicious actor send an .pdf attachment with the email. But using Exiftool, it reveals that this is actually a .ZIP file

  <img width="1459" height="589" alt="image" src="https://github.com/user-attachments/assets/e9b83620-6e3d-43c7-8950-9c5cf81ef7fd" />

* Unzip the PuzzleToCoCanDa file, we receive another 3 files inside it. 

  <img width="376" height="63" alt="image" src="https://github.com/user-attachments/assets/980e91f6-47f5-4937-86c0-57f9f7fc6c5d" />

  <img width="1919" height="706" alt="image" src="https://github.com/user-attachments/assets/15e3abb1-d302-46fb-a7b2-246be3069bef" />


* The metadata of GoodJobMajor tells us the real identity of the malicious actor

  <img width="495" height="301" alt="image" src="https://github.com/user-attachments/assets/ffb4be98-fe3c-42b0-b0d4-3ae7e6556f37" />

* Inside the Money.xlsx excel file, we have 2 sheets. The second sheet looks like it has nothing in it but in the email, the sender hint to not trust your eyes

  <img width="788" height="453" alt="image" src="https://github.com/user-attachments/assets/ea6782d7-fc4b-4a2b-a798-a0efa3916042" />

* So the information here maybe hidden from the receiver. In the 4C, we obtain a string that looks like it is Base64-encoded. Using Cyberchef, we obtain the location of the attacker mentioned before

  <img width="1016" height="419" alt="image" src="https://github.com/user-attachments/assets/a523110c-ad3e-420f-b361-435411126347" />

* As we have said before, the real reply target of the attacker is pashter.com from Reply-To section. It could be the probable C&C domain to control the attacker’s autonomous bots
  

  

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the email service used by the malicious actor?      | emkei.cz    |
| Q2: What is the Reply-To email address?      | negeja3921@pashter.com    |
| Q3: What is the filetype of the received attachment which helped to continue the investigation?       | .zip    |
| Q4: What is the name of the malicious actor?      | Pestero Negeja    |
| Q5: What is the location of the attacker in this Universe?      | The Martian Colony, Beside Interplanetary Spaceport.    |
| Q6: What could be the probable C&C domain to control the attacker’s autonomous bots?      | pashter.com    |

---

