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

* Tools: Wireshark, evtx-dump, any run, VirusTotal

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

* Following privilege escalation, the attacker attempted to download a file.http[:]//87[.]96[.]21[.]84/checking.ps1
  
   <img width="1637" height="762" alt="image" src="https://github.com/user-attachments/assets/2f41f7b6-9108-4284-98f7-0b3ed27d2c98" />

   <img width="1639" height="754" alt="image" src="https://github.com/user-attachments/assets/792baf8d-87d1-4034-b74a-ecf5188ac53f" />

* Understanding which group Security Identifier (SID) the malicious script checks to verify the current user's privileges can provide insights into the attacker's intentions. Checking the file attacker downloaded it show that he targeted SID of S-1-5-32-544

  <img width="644" height="513" alt="image" src="https://github.com/user-attachments/assets/87686128-9697-4704-8ac7-1bf7ffeb30f7" />

* Windows Defender plays a critical role in defending against cyber threats. If an attacker disables it, the system becomes more vulnerable to further attacks. In the same .ps1 file we can see registry keys used by the attacker to disable Windows Defender functionalities: DisableAntiSpyware, DisableRoutinelyTakingAction, DisableRealtimeMonitoring, SubmitSamplesConsent, SpynetReporting

  <img width="655" height="507" alt="image" src="https://github.com/user-attachments/assets/4a61863a-745c-4a68-b876-4b4304669645" />

* The second file the attacker downloaded is del.ps1. By creating a hidden task under Microsoft\WUT\Update, it ensures the malicious script keeps running indefinitely.

  <img width="1632" height="779" alt="image" src="https://github.com/user-attachments/assets/b9ffa409-6c1c-4041-b928-fae5898f68c5" />

  <img width="627" height="221" alt="image" src="https://github.com/user-attachments/assets/17bacbbb-9655-40b2-bb8e-ab35e54e7aa3" />

* Based on analysis of the second malicious file,the attaker try to kill monitoring tools (taskmgr, perfmon, ProcessHacker, etc.), Removing WMI event subscriptions (_FilterToConsumerBinding), Forcefully stopping its own process (stop-process $pid -Force) so this is Defense Evasion TA0005.

  <img width="638" height="346" alt="image" src="https://github.com/user-attachments/assets/abc0f911-4bfa-479c-984a-a3c1c1df96d7" />

* Right under the discovered file, I find a new suspicious ps1 file name Invoke-PowerDump.ps1. This script is a Windows credential-dumping tool (PowerDump-style). In short:

    * Escalates privileges to SYSTEM by stealing/duplicating the LSASS process token (abusing SeDebugPrivilege).
    * Reads the SAM registry hive, which stores local Windows user account password hashes in encrypted form.
    * Derives decryption keys from the system's boot key (stored in the registry) plus per-account values.
    * Decrypts and outputs the LM/NT password hashes for every local user, in a format (username:RID:LMhash:NThash:::) that's directly usable for offline cracking or pass-the-hash attacks.

  <img width="1643" height="780" alt="image" src="https://github.com/user-attachments/assets/400f7c9a-3d65-4b4e-b80c-9c608948a2c4" />

  <img width="642" height="508" alt="image" src="https://github.com/user-attachments/assets/602aa241-d8bc-4567-bf43-fdd8803c4159" />

  <img width="646" height="503" alt="image" src="https://github.com/user-attachments/assets/e0c5be30-0773-4285-a338-ddf1156b5ba9" />

* Understanding which credentials have been compromised is essential for assessing the extent of the data breach. In the ichigo-lite.ps1 file downloaded we can see that hashes.txt is where the attacker contain the dumped credentials

  <img width="1643" height="781" alt="image" src="https://github.com/user-attachments/assets/dcdcd930-72fd-4e5a-95d7-67674cd40f07" />

  <img width="644" height="463" alt="image" src="https://github.com/user-attachments/assets/35a9be68-c4eb-4726-a403-af31f0e0cc49" />

* Knowing the hosts targeted during the attacker's reconnaissance phase, the security team can prioritize their remediation efforts on these specific hosts. The hacker save 4 hosts that are: 87.96.21.71, 87.96.21.75, 87.96.21.80, 87.96.21.81 in the extracted_hosts.txt

  <img width="1647" height="779" alt="image" src="https://github.com/user-attachments/assets/c87bb778-ed1d-4d75-9aff-5aafb77d52ce" />

* After hash dumping, the attacker attempted to deploy ransomware on the compromised host, spreading it to the rest of the network through previous lateral movement activities using SMB. Here we found a file name javaw.exe must be the ransomware sample and I will conduct a behavioral analysis using any.run

  <img width="1627" height="782" alt="image" src="https://github.com/user-attachments/assets/e6029a8c-7044-49e4-b814-cf89e5406dba" />

  <img width="497" height="408" alt="image" src="https://github.com/user-attachments/assets/47bb34f7-ad82-4076-99f9-62143c11bcab" />

* In some cases, decryption tools are available for specific ransomware families. Identifying the family name can lead to a potential decryption solution. Upload the malware sample from the previous section to VirusTotal and the result indicates that this is a ransomware name BlueSky

  <img width="1907" height="692" alt="image" src="https://github.com/user-attachments/assets/96168847-65fc-4107-8d9a-981391d44f36" />



---

## 🧾 Key Findings

- **Attacker IP:** 87.96.21.84 performed network scanning and targeted the SQL Server.
- **Compromised Account:** The attacker successfully authenticated to the MSSQL server using the `sa` account with the password `cyb3rd3f3nd3r$`.
- **Privilege Escalation & Lateral Movement:** The attacker enabled the `xp_cmdshell` feature, allowing arbitrary OS command execution. Using Metasploit, a C2 payload was injected into the `winlogon.exe` process.
- **Persistence & Defense Evasion:**  
  - Downloaded and executed `checking.ps1`, which verified membership in the Administrators group (SID: `S-1-5-32-544`) and disabled Windows Defender by modifying multiple registry values (`DisableAntiSpyware`, `DisableRoutinelyTakingAction`, `DisableRealtimeMonitoring`, `SubmitSamplesConsent`, `SpynetReporting`).  
  - Downloaded `del.ps1`, which killed security tools, removed WMI event subscriptions, and created a hidden scheduled task `\Microsoft\WUT\Update` for persistent execution. This activity maps to the **Defense Evasion (TA0005)** MITRE ATT&CK tactic.
- **Credential Dumping:** The script `Invoke-PowerDump.ps1` was used to dump local SAM hashes. The stolen credentials were saved in `hashes.txt`.
- **Internal Reconnaissance & Propagation:** The attacker enumerated hosts and saved four target IPs (`87.96.21.71`, `87.96.21.75`, `87.96.21.80`, `87.96.21.81`) in `extracted_hosts.txt`, later spreading ransomware via SMB.
- **Ransomware Deployment:** The final payload, `javaw.exe`, was identified through VirusTotal and behavioral analysis as belonging to the **BlueSky** ransomware family.


---



## 💡 Lessons Learned

Honestly, this challenge humbled me more than I expected. I started off confident, but a few moments really made me rethink why i chose this path.

When I first opened the pcap, the scanning activity was obvious and that part felt good. But then I got absolutely stuck on question 5 for hours. I was hunting through packets, completely forgetting to check the event logs for process injection.  It was a clear reminder that network evidence alone tells half the story. I need to make cross reference with host logs an automatic reflex, not an afterthought.

---


