# 🛡️ Security Writeup – Log Analysis - Privilege Escalation

## 📌 Overview

* **Platform:** BTLO
* **Category:** CTF
* **Difficulty:** Easy
* **Date:** 26/03/2026

---

## 📖 Scenario

A server with sensitive data was accessed by an attacker and the files were posted on an underground forum. This data was only available to a privileged user, in this case the ‘root’ account. Responders say ‘www-data’ would be the logged in user if the server was remotely accessed, and this user doesn’t have access to the data. The developer stated that the server is hosting a PHP-based website and that proper filtering is in place to prevent php file uploads to gain malicious code execution. The bash history is provided to you but the recorded commands don’t appear to be related to the attack. Can you find what actually happened?

---


## 🔍 Analysis

1, Other than root user, every other users locate under the home directory. Open the given bash history command file to find other users using search in your text editor because hacker may want to explore another user to gain more valuable information or secret.

<img width="654" height="511" alt="image" src="https://github.com/user-attachments/assets/06340d75-ba27-45d1-b786-1a15d5f7dd23" />

We explored that the attacker try to change directory to "daniel" user to check for potential information from his directory

2, Download exploit tool: The attacker use wget to download a malicious script called "linux-exploit-suggester.sh" from github and save it to "les.sh", which is much shorter and more comfortable to execute. Linux Exploit Suggester is a vulnerability assessment tool designed to identify privilege escalation paths, the hacker may try to privllege escalation on victim's system to gain more permission and reach to the higher level user.

<img width="640" height="276" alt="image" src="https://github.com/user-attachments/assets/09e14c3d-dfe7-41fc-85f1-8566284791c4" />

<img width="1271" height="756" alt="image" src="https://github.com/user-attachments/assets/e21d35b6-a59d-4553-bcf1-3d41a11e0cc8" />

3,  After gaining initial access, the attacker explore the process and user for high value target

ps -aux: list all process, software and which user is running them

ps -ef | grep root: filter for processes run with root privilege, potential targets may be exploited here

dpkg -l: list all installed software and version. Can be used to exploit if they are old version or exploitable, hacker often take advantage of these vulnerabilities to infect host's machine

ls -aRl /etc/ | awk '$1 ~ /^.*r.*/': recursively search the /etc/ directory for files that are readable. Because /etc/ often contains sensitive configuration files (like passwords or service configs), the sentsitive information might be save here as readable files.


<img width="631" height="425" alt="image" src="https://github.com/user-attachments/assets/1fb60f64-3592-4fe8-bc1c-81c606809da9" />

4, Network scanning: 

ifconfig -a: Shows network interfaces 

cat /etc/network/interfaces / cat /etc/sysconfig/network: The attacker try to identify network layout

cat /etc/resolv.conf: Shows the DNS servers being used.

iptables -L: Checks the firewall rules to see which ports are blocked or open.

tcpdump: hacker sniff network, recon network traffic

5, 

find / -type f -user root -perm -4000 2>/dev/null: attacker search for Set User ID (SUID). When the SUID bit is set on a file, it runs with the permissions of the owner (usually root), not the person who typed the command.

<img width="643" height="85" alt="image" src="https://github.com/user-attachments/assets/79a2f2b5-993b-455e-8c1c-4605bd006767" />

python -c 'import os; os.execl("/bin/sh", "sh", "-p")': The hacker likely discovered that the Python binary itself had the SUID bit set .

rm /var/www/html/uploads/x.phtml: hacker remove this suspicious file to delete evidence of the entry point, make it harder to investigate.  .phtml extension is used to bypass simple filters that only look for .php files.


## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What user (other than ‘root’) is present on the server?       | daniel    |
| Q2: What script did the attacker try to download to the server?      | linux-exploit-suggester.sh    |
| Q3: What packet analyzer tool did the attacker try to use? | tcpdump |
| Q4: What file extension did the attacker use to bypass the file upload filter implemented by the developer? | .phtml |
| Q5: Based on the commands run by the attacker before removing the php shell, what misconfiguration was exploited in the ‘python’ binary to gain root-level access? 1- Reverse Shell ; 2- File Upload ; 3- File Write ; 4- SUID ; 5- Library load | 4 |

---
