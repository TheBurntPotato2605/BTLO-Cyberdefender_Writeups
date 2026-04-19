# 🛡️ Security Writeup – The Crime Lab 

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Endpoint Forensic
* **Difficulty:** Easy
* **Date:** 19/04/2026

---

## 📖 Scenario

We're currently in the midst of a murder investigation, and we've obtained the victim's phone as a key piece of evidence. After conducting interviews with witnesses and those in the victim's inner circle, your objective is to meticulously analyze the information we've gathered and diligently trace the evidence to piece together the sequence of events leading up to the incident.

---

## 🎯 Objectives

Utilize ALEAPP to analyze Android device artifacts, reconstructing a victim's financial details, movements, and communication patterns.

---

## 🧰 Tools 

* Tools: ALEAPP


---


## 🔍 Analysis

* Based on the accounts of the witnesses and individuals close to the victim, it has become clear that the victim was interested in trading. This has led him to invest all of his money and acquire debt. So we will search for the app or platform he used to do trading on his phone. In the installed app there is only "Olymp Trade" is a famous trading app

  <img width="1257" height="276" alt="image" src="https://github.com/user-attachments/assets/183ce142-3fb0-440e-bdc4-ef861badd1bb" />

  <img width="641" height="299" alt="image" src="https://github.com/user-attachments/assets/3ff9debf-cc4f-4b51-a72a-28647f12a334" />

* According to the testimony of the victim's best friend, he said, "While we were together, my friend got several calls he avoided. He said he owed the caller a lot of money but couldn't repay now".
* First, we will go into Call Logs to look for the phone call that he tried to avoid. It indicates that he did not answer the call from the Phone Address +201172137258 multiple times, this number is likely associated with the creditor based on repeated missed calls
  
  <img width="779" height="737" alt="image" src="https://github.com/user-attachments/assets/fafb647c-c422-41dd-8ab0-465fca0d02f9" />

* Dive deeper in to the Contact List, the owner of this phone number is a man named Shady Wahab

  <img width="675" height="122" alt="image" src="https://github.com/user-attachments/assets/18f88b91-26c9-4b7a-aaa0-fd4c4e2c195f" />

* Lastly, in the SMS messages section of the report, we can see a message was sent to the victim to remind him of the debt up to 250,000 EGP

  <img width="1529" height="165" alt="image" src="https://github.com/user-attachments/assets/410eafd8-8d21-4eff-b2c5-d832f54d18eb" />

* Based on the statement from the victim's family, they said that on September 20, 2023, he departed from his residence without informing anyone of his destination. To know where had he been, we should investigate map or tracking application recently used.

  <img width="1031" height="722" alt="image" src="https://github.com/user-attachments/assets/dd4540f1-d69a-44da-83af-7ac815211fe3" />
  
  <img width="366" height="779" alt="image" src="https://github.com/user-attachments/assets/155cbb50-990c-4ca8-9780-3a19bc75cfc2" />

* From victim's phone, on September 20, 2023, GG Map indicate that he was at The Nile Ritz-Carlton, Cairo 

* The detective continued his investigation by questioning the hotel lobby. She informed him that the victim had reserved the room for 10 days and had a flight scheduled thereafter. The investigator believes that the victim may have stored his ticket information on his phone. Since the online ticket is usually sent to client in the format of picture or pdf, we may look for it in email, flight web or image in his phone.

  <img width="1561" height="394" alt="image" src="https://github.com/user-attachments/assets/bdbd58d1-fdc3-41b0-93ab-2bd39e7493dd" />

  <img width="1919" height="613" alt="image" src="https://github.com/user-attachments/assets/1affc86b-18ac-4147-a7c2-74f0b8a96561" />

* It seems that Mohamed Ahmed booked a flight to Las Vegas from Cairo on October 1, 2023

* After examining the victim's Discord conversations, we discovered he had arranged to meet a friend at a specific location. Now we examine the victim's Discord chats to identify his destination

  <img width="817" height="733" alt="image" src="https://github.com/user-attachments/assets/86976180-1d17-4788-a2fc-b7c9e28238f8" />

* A Discord message from the Username rob1ns0n told him to meet at The Mob Museum when arrive to USA.
---


## 🧾 Key Findings

* The victim was actively using Olymp Trade as his primary trading platform.
* Financial evidence suggests the victim had accumulated significant debt.
* Repeated missed calls and SMS records connect the debt to Shady Wahab.
* The owed amount was identified as 250,000 EGP.
* Location artifacts place the victim at The Nile Ritz-Carlton, Cairo on September 20, 2023.
* Additional evidence indicates the victim intended to travel from Cairo to Las Vegas on October 1, 2023.
* Discord messages show the victim had arranged to meet a friend at The Mob Museum upon arriving in the United States.

---



## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: Can you identify the SHA256 of the trading application the victim primarily used on his phone?       | 4f168a772350f283a1c49e78c1548d7c2c6c05106d8b9feb825fdc3466e9df3c    |
| Q2: How much does the victim owe this person?       | 250000    |
| Q3: What is the name of the person to whom the victim owes money?       | Shady Wahab    |
| Q4: Where was the victim located at that moment?       | The Nile Ritz-Carlton    |
| Q5: Look for where the victim intended to travel.       | Las Vegas    |
| Q6: Can you determine where the meeting with a friend on Discord was supposed to occur?       | The Mob Museum    |

---

