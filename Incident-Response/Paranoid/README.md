# 🛡️ Security Writeup – Paranoid

## 📌 Overview

* **Platform:** BTLO
* **Category:** Incedent Response
* **Difficulty:** Medium
* **Date:** 13/05/2026

---

## 📖 Scenario

I'm not paranoid, you are

---



## 🧰 Tools 

* Tools: aureport, CVE


---


## 🔍 Analysis

* First, we will have an overview of given log file audit.log. The command below will show a summary of the log file. As we can see here there are 87 failed logins and only 1 success login.

  <img width="668" height="497" alt="image" src="https://github.com/user-attachments/assets/1cd144f1-dd59-4cad-9b57-32506caaee7a" />

* Next, we have to identify which account was compromised. From the authentication report, it showed that only account btlo login to machine. The attacker from the host 192.168.4.155 tried to ssh to the machine multiple times and he successed at the 89th attempt. This is a sign of a brute force attack target our victim.

  <img width="640" height="438" alt="image" src="https://github.com/user-attachments/assets/fd8aa32e-31fd-41e0-88f2-152e409a647b" />

  <img width="615" height="311" alt="image" src="https://github.com/user-attachments/assets/e6107239-bbfc-4d45-842a-c457f3f03976" />

* Furthermore, we need to discover what the hacker did with system. We can tell aureport to shows commands typed on terminals - TTYs. Right after compromising an account, he use ls and whoami commands to discover the directory and user he accessed. Next, he downloaded linpeas - a script that search for possible paths to escalate privileges on Linux/Unix*/MacOS hosts, to perform system enumeration.

  <img width="801" height="455" alt="image" src="https://github.com/user-attachments/assets/39f65167-5d45-46e9-8829-6fd72dacda61" />

* Moreover, he then get a malicious binary called evil and execute it. After that, he run whoami command again to check for new user he changed to and now he can access shadow file ( a critical component of Linux systems, storing encrypted user password information and related account details) which require root privilege. It indicated that running evil is his technique to escalate privilege.

  <img width="582" height="45" alt="image" src="https://github.com/user-attachments/assets/5399541d-7730-49fc-8b27-b6f21f66173c" />



---

## Key Findings

| Item | Value |
|------|-------|
| Compromised account | `btlo` |
| Attack type | brute force |
| Attacker IP | `192.168.4.155` |
| Enumeration tool | `linpeas` |
| Root binary & PID | `evil, 829992` |
| CVE | `CVE-2021-3156` |
| Vuln type | heap‑based buffer overflow |
| Exfiltrated file | `shadow` |

---

## 💡 Lessons Learned

- **Block brute force** – Use  SSH keys, rate limiting,....
- **Know your `aureport` options**
- `aureport` gives separate tables . You must  correlate timestamps or event IDs to build a timeline. There’s no single “attack chain” view.

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What account was compromised?       | btlo    |
| Q2: What attack type was used to gain initial access?       | brute force    |
| Q3: What is the attacker's IP address?       | 192.168.4.155    |
| Q4: What tool was used to perform system enumeration?       | linpeas    |
| Q5: What is the name of the binary and pid used to gain root?       | evil, 829992    |
| Q6: What CVE was exploited to gain root access? (Do your research!)       | CVE-2021-3156    |
| Q7: What type of vulnerability is this?       | heap-based buffer overflow    |
| Q8: What file was exfiltrated once root was gained?       | shadow    |

---

