# 🛡️ Security Writeup – PsExec Hunt Lab


## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Network Forensics
* **Difficulty:** Easy 
* **Date:** 21 - 22/03/2026

 Analyze SMB traffic in a PCAP file using Wireshark to identify PsExec lateral movement, compromised systems, user credentials, and administrative shares.
 
---

## 📖 Scenario

An alert from the Intrusion Detection System (IDS) flagged suspicious lateral movement activity involving PsExec. This indicates potential unauthorized access and movement across the network. As a SOC Analyst, your task is to investigate the provided PCAP file to trace the attacker’s activities. Identify their entry point, the machines targeted, the extent of the breach, and any critical indicators that reveal their tactics and objectives within the compromised environment.

* PsExec is used to execute remote command or program without installing agent.
  
  --> Execute command on remote host
  
  --> Run process with SYSTEM privilege

---

## 🎯 Objectives

* Discover PsExec's lateral movement
* Investigate the provided PCAP file to trace the hacker's activities
* Identify the entry point, machines targeted
* The extention of the breach
* Find out the attacker's tactics and objectives within the compromised environment

---

## 🧰 Tools & Techniques

* Tools: Wireshark
* Techniques: Network Analysis

---

## 🧠 Investigation Strategy

From the Scenario and Overview, we have some useful clues:

* PsExec use SMB --> investigate focus on port 445
* Identify suspicious IP, host, command
* Process: PsExec.exe , PSEXESVC.exe (temporary service)
* Windows log: 7045 (Service created), 4624 (Successful logon) - Type 3: Via network, 5140 (network share object accessed)

---

## 🔍 Analysis

### 1. Initial Assessment

* It seems like host from IP 10.0.0.132 tries to establish a connection with DNS server but no respond from server. Client retransmission multiple times with different port. The volume sent is not massive and and only send to DNS server so it does not seem like a SYN flooding attack or scanning for open port

  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/03fec410-5977-4957-9290-958b21b81f8f" />

  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/ff4c43a8-84c5-46c0-83c5-c2a758cea451" />

* Host from IP 10.0.0.131 join three multicast groups and accept traffic from every source (EXCLUDE mode), which is quite suspicious. It means that hacker can widen the attack surface

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/18985fce-7643-4af2-9e01-f272bc426df3" />

* Host with IP 10.0.0.130 negotiate SMB request to dest IP 10.0.0.133, it send NTLM authentication message with user credential: ssales and right after that have hidden admistrative shares (ADMIN$). Suspicious host 10.0.0.130 tries to copy file PSEXESVC.exe through ADMIN$

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/95e56e19-2317-42ab-8215-96c7ac1221ff" />

* Attacker logoff session, maybe an act of cleanup

<img width="1862" height="157" alt="image" src="https://github.com/user-attachments/assets/56c901da-712e-4e32-aef8-c553ad268e6f" />


👉 Insight: Focus on SMB, TCP, SVCCTL traffic, suspicious IP: 10.0.0.130 and 10.0.0.131, infected server: 10.0.0.133, 

---

### 2. Focused Investigation

* The malicious host share file with server which indicate that it is trying to execute remote command because that file is PSEXESVC normally used to 

<img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/2011c88f-b404-484f-80d8-681f5e5ff196" />

 * Attacker try to connect to service control manager, create, start and check status of the service. He is trying to active remote service execution

   <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/53a8264b-91ec-4b3b-b709-6f44adeea2bb" />

* Attacker may try to steal sensitive information like key to move lateral

<img width="1899" height="117" alt="image" src="https://github.com/user-attachments/assets/05cdf456-ec3b-4823-95a0-688b7c62960a" />

 * Hacker named pipe stdin stdout stder to prepare for his remote command execution and maybe to create new service or process so we have to filter and investigate further

   <img width="1909" height="749" alt="image" src="https://github.com/user-attachments/assets/92af40c1-5884-40cd-a592-db35b0c44971" />
   
  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/05ec6995-9b19-4756-91fa-2af7a9306891" />
  
* Extention of the breach, the attacker first pivoted hostname

  <img width="1919" height="906" alt="image" src="https://github.com/user-attachments/assets/03680ba3-b26b-4eed-8856-6d3f547f786e" />

---

### 3. Deep Analysis

* Further investigation indicate that maybe the .key file is not a sensitive file. This seems like created by PsExec with name like PSEXEC-randomid.key, different from normal key file like private.key or ssl.key. It is also checked for existence multiples time through GetInfo request, the attacker has that file so why he still has to check for it? 

  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/7f377f20-eb2d-4d38-83ed-a3a3fcfb02bc" />

  <img width="1919" height="1079" alt="image" src="https://github.com/user-attachments/assets/1aeb9cc3-539c-4707-95a9-24cb2e315b31" />

  <img width="1919" height="881" alt="image" src="https://github.com/user-attachments/assets/cabb46e6-12b8-47b8-867e-047180c574f8" />


  <img width="1919" height="832" alt="image" src="https://github.com/user-attachments/assets/0862b3c8-ed26-4225-961e-f35bf97231ae" />

==> It seems like that this .key file is the remote code execution. Everytime attacker check for existence of it, it create request for PSEXESVC.exe, create and start new service, and also stdin stdout stder pipe, lateral movement to another user

* Hacker try lateral movement to another user NTLM authentication /jdoe and IEuser

  <img width="1862" height="343" alt="image" src="https://github.com/user-attachments/assets/491b163f-d541-4f1c-94fd-8378fcbf34e3" />

  <img width="1862" height="295" alt="image" src="https://github.com/user-attachments/assets/51fbd7f0-0f7e-495f-ab61-fdd5cc9fbec7" />






---

### 4. Key Artifact Identification

* File: PSEXESVC.exe, PSEXESVC
* Suspicious file .key: PSEXEC-HR-PC-1C6C5D14.key, PSEXEC-HR-PC-8FF87B23.key, PSEXEC-HR-PC-AF58F077.key, PSEXEC-HR-PC-CF174DD5.key, PSEXEC-HR-PC-1C6C5D14.key
* Remote code execution: PSEXESVC-HR-PC-7980-stdin, PSEXESVC-HR-PC-7980-stdout, PSEXESVC-HR-PC-7980-stder
* Access: ADMIN$, IPC

  ==> These are indicator of PsExec-based remote command execution (lateral movement)

---

## 🧾 Key Findings

* Remote service creation
* File transfer via SMB
* Command execution via named pipes
* Lateral movement
* ADMIN$, IPC$ access

---

## 🗺️ Attack Flow / Timeline

1. Initial access use user's credential or NTLM hash of ssales user
2. Connect to IPC$ control channel
3. Connect to ADMIN$ for file transfer
4. Drop payload PSEXESVC.exe
5. Check for malicious .key file
6. Open, create, start service via IPC$
7. Open command channel via PSEXESVC-HR-PC-random-stdin/stdout/stder to send and receive command
8. Hacker logogg the session

---

## 🧬 Threat Context 

* **Tactic:** RCE, Lateral Movement, Privilege ?, Service execution
* **Technique:** TA0002, TA0008, T1569.002

---

## 🛡️ Detection Opportunities

 1. Network-based detection
 2. Host-based detection (Windows logs)
 3. Behavioral detection
    
---

## 🔐 Prevention & Mitigation

1. Restrict administrative shares
2. Control credential usage
3. Apply least privilege
4. Application control
5. Logging and monitoring
---

## 💡 Lessons Learned

*  Network analysis is an important skill and can reveal an attacker's execution
*  Admin shares are risky
*  Legit tools can be abused by the hacker
*  Individual artifacts are not suspicious if stand alone
*  Personal credential have to be protected carefully
*  Should practice more on network analysis to have a better analyzing skill

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: To effectively trace the attacker's activities within our network, can you identify the IP address of the machine from which the attacker initially gained access?      | 10.0.0.130    |
| Q2: To fully understand the extent of the breach, can you determine the machine's hostname to which the attacker first pivoted?      | SALES-PC    |
| Q3: Knowing the username of the account the attacker used for authentication will give us insights into the extent of the breach. What is the username utilized by the attacker for authentication? | ssales |
| Q4: After figuring out how the attacker moved within our network, we need to know what they did on the target machine. What's the name of the service executable the attacker set up on the target? | PSEXESVC |
| Q5: We need to know how the attacker installed the service on the compromised machine to understand the attacker's lateral movement tactics. This can help identify other affected systems. Which network share was used by PsExec to install the service on the target machine? | ADMIN$ |
| Q6: We must identify the network share used to communicate between the two machines. Which network share did PsExec use for communication? | IPC$ |
| Q7: Now that we have a clearer picture of the attacker's activities on the compromised machine, it's important to identify any further lateral movement. What is the hostname of the second machine the attacker targeted to pivot within our network? | MARKETING-PC |

---



---

