# 🛡️ Security Writeup – BlueSky Ransomware

## 📌 Overview

* **Platform:** CyberDefenders
* **Category:** Network Analysis
* **Difficulty:** Medium
* **Date:** 01/07/2026

---

## 📖 Scenario

A high-profile corporation that manages critical data and services across diverse industries has reported a significant security incident. Recently, their network has been impacted by a suspected ransomware attack. Key files have been encrypted, causing disruptions and raising concerns about potential data compromise. Early signs point to the involvement of a sophisticated threat actor. Your task is to analyze the evidence provided to uncover the attacker’s methods, assess the extent of the breach, and aid in containing the threat to restore the network’s integrity.

---

## 🎯 Objectives

Reconstruct a BlueSky ransomware attack by analyzing network traffic, decoding PowerShell scripts, and examining persistence mechanisms to identify attacker tactics and IOCs.

---

## 🧰 Tools & Techniques

* Tools: 

---



## 🔍 Analysis

* Knowing the source IP of the attack allows security teams to respond to potential threats quickly. To have a clear overview of conversations, we go to Statistics. As we can see here, the IP address of 87.96.21.84 sent multiple packets to various ports of host 87.96.21.81 from port 1 to port 65389. This is a possible scanning activity
  
  <img width="1463" height="632" alt="image" src="https://github.com/user-attachments/assets/8d62a39e-b92d-4c94-886f-a82aca2aa655" />

  <img width="1444" height="553" alt="Screenshot 2026-07-01 211203" src="https://github.com/user-attachments/assets/07c49edf-fa43-4f8a-a5da-834a7afba412" />

* During the investigation, it's essential to determine the account targeted by the attacker. We can see that there is a TDS7 login from the source IP of attacker that might be his attempt to login an user account name sa. And he login that account successfully with password: cyb3rd3f3nd3r$

  <img width="1870" height="786" alt="image" src="https://github.com/user-attachments/assets/5934dbb3-5ee4-4bdb-aa12-0e46aeec91ef" />

* Right after that, he change some setting to facilitate lateral movement within a network

  <img width="1641" height="586" alt="image" src="https://github.com/user-attachments/assets/bee5408f-70a7-4426-bf1d-d862f7294d66" />

  **EXEC sp_configure 'show advanced options', 1;**
    * Enables advanced configuration options in SQL Server.

    * By default, many risky features are hidden. This command makes them visible.

  **RECONFIGURE;**

    * Applies the above change immediately.

  **EXEC sp_configure 'xp_cmdshell', 1;**

    * Turns on the xp_cmdshell feature.

    * xp_cmdshell allows execution of operating system commands directly from SQL Server.

  **RECONFIGURE;**

    * Applies the above change immediately.
 
* After hours of stucking at the question 5, I find something that may be useful. MSFconsole is the main command-line interface for the Metasploit Framework, which is one of the most widely used penetration testing and exploitation platforms in cybersecurity. This event indicates Metasploit C2 and winlogon.exe is the process that is injected with C2 payload.

   <img width="764" height="515" alt="image" src="https://github.com/user-attachments/assets/049b3402-8153-47f5-9676-691f44f5d184" />

* Following privilege escalation, the attacker attempted to download a file.http://87.96.21.84/checking.ps1
  
   <img width="1637" height="762" alt="image" src="https://github.com/user-attachments/assets/2f41f7b6-9108-4284-98f7-0b3ed27d2c98" />

   <img width="1639" height="754" alt="image" src="https://github.com/user-attachments/assets/792baf8d-87d1-4034-b74a-ecf5188ac53f" />

* Understanding which group Security Identifier (SID) the malicious script checks to verify the current user's privileges can provide insights into the attacker's intentions. 





---

## 🧾 Key Findings



---

## 🗺️ Attack Flow 


---

## 🧬 Threat Context 

* **Tactic:** 
* **Technique:** 

---





## 💡 Lessons Learned


---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1       | xxx    |
| Q2       | xxx    |

---
