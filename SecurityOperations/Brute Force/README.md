# 🛡️ Security Writeup – Brute Force

## 📌 Overview

* **Platform:** BTLO
* **Category:** Security Operations
* **Difficulty:** Medium
* **Date:** 01/06/2025

---

## 📖 Scenario

One of our system administrators identified a large number of Audit Failure events in the Windows Security Event log.

There are a number of different ways to approach the analysis of these logs! Consider the suggested tools, but there are many others out there! 

---

## 🎯 Objectives

Analyze logs from an attempted RDP bruteforce attack

---

## 🧰 Tools 

* Text Editor, DB browser


---



## 🔍 Analysis

* Here, i use DB browser for SQLite to help we investigate the .csv log file
  <img width="1919" height="863" alt="image" src="https://github.com/user-attachments/assets/350aedd6-f206-451b-9d8b-9a60ba84e9be" />
* Windows' Event ID for failed logon is 4625, execute the SQL command below to count for number of failed logon.
  <img width="745" height="340" alt="Screenshot 2026-06-01 180358" src="https://github.com/user-attachments/assets/78373d9d-53d3-4af8-85fc-fd563d893285" />

* Look deeper at the Event 4625, we know that the administrator local account is being targeted with logon type = 3 (Network Logon) which indicates that attacker tried to connect to our machine
  <img width="1045" height="438" alt="image" src="https://github.com/user-attachments/assets/861d5e63-3fa9-41ca-9cf6-9294c88ceabb" />
* The failure reasons related to the Audit Failure logs is multiple Unknown username or bad password, it means that the hacker attempted to conduct bruteforce attack to the admin account
* The IP address conducted this attack is 113[.]161[.]192[.]227 from Lam Dong, Viet Nam and is reported from vendors of attacks on honeypot servers, bruteforce attack on MSSQL server,...
  <img width="449" height="241" alt="image" src="https://github.com/user-attachments/assets/64943745-4002-42aa-a803-1d0d1cbe0e93" />
  <img width="1322" height="708" alt="image" src="https://github.com/user-attachments/assets/e2f95f6d-46db-45c4-ba1b-977dae69642f" />
  <img width="1329" height="617" alt="image" src="https://github.com/user-attachments/assets/00402bb2-b56c-4926-8978-f2c0a6162d88" />
* To find the port range of the attacker to make these login requests, we run the below command to find and sort the source port. So he used the port range from 49162 to 65534
  <img width="632" height="62" alt="image" src="https://github.com/user-attachments/assets/240c5eba-6065-48b0-bc35-8e649ea01571" />
  <img width="626" height="206" alt="image" src="https://github.com/user-attachments/assets/55453201-212e-437d-92e9-231b75e41a1e" />
  <img width="638" height="267" alt="image" src="https://github.com/user-attachments/assets/5ec0aa54-5c71-405c-822c-85133d7ca952" />





---

## 🧾 Key Findings



- **Total Failed Logons (Event ID 4625):** 3103
- **Targeted Account:** `Administrator` (local).
- **Logon Type:** `3` (Network logon – typical for RDP over network).
- **Failure Reason:** `Unknown user name or bad password` – consistent with password guessing.
- **Attacker Source IP:** `113.161.192.227` (geolocated in Lam Dong, Viet Nam).
- **Source Port Range:** `49162` – `65534` (ephemeral ports), indicating many concurrent or sequential connection attempts.




---


