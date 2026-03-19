# Oski Lab

Analyze a sandbox report using Any.Run to identify Stealc malware behavior, extract configuration details, and map observed tactics to MITRE ATT&CK.

**Scenario**

The accountant at the company received an email titled "Urgent New Order" from a client late in the afternoon. When he attempted to access the attached invoice, he discovered it contained false order information. Subsequently, the SIEM solution generated an alert regarding downloading a potentially malicious file. Upon initial investigation, it was found that the PPT file might be responsible for this download. Could you please conduct a detailed examination of this file?

<img width="940" height="492" alt="image" src="https://github.com/user-attachments/assets/cd5e7e63-b542-4782-9b80-538b8ab4988f" />

<img width="940" height="512" alt="image" src="https://github.com/user-attachments/assets/e31499a1-a05f-4024-aaa1-96661ece90a1" />

<img width="940" height="514" alt="image" src="https://github.com/user-attachments/assets/65c42915-3c1e-4eb1-a885-91b2ddbf6100" />

**Q1**

Determining the creation time of the malware can provide insights into its origin. What was the time of malware creation?

<img width="940" height="427" alt="image" src="https://github.com/user-attachments/assets/d2850cf3-ed51-424b-b1ea-c424fa466bbe" />

**Answers: 2022-09-28 17:40**


**Q2**

Identifying the command and control (C2) server that the malware communicates with can help trace back to the attacker. Which C2 server does the malware in the PPT file communicate with?

The malware will send the request to this server to receive command or transfer data

<img width="940" height="163" alt="image" src="https://github.com/user-attachments/assets/572679c3-2f71-441e-bff4-842c43147388" />

**Answers:** **http://171.22.28.221/5c06c05b7b34e8e6.php**



**Q3**

Identifying the initial actions of the malware post-infection can provide insights into its primary objectives. What is the first library that the malware requests post-infection?

In the behavior tab of Virustotal, the malware wants the database capability right away so its first action is to fetch the DLL

<img width="940" height="646" alt="image" src="https://github.com/user-attachments/assets/364fae35-15a2-41f6-852b-b0aab1b32961" />

**Answers: sqlite3.dll**


**Q4**

By examining the provided [Any.run report](https://any.run/report/a040a0af8697e30506218103074c7d6ea77a84ba3ac1ee5efae20f15530a19bb/d55e2294-5377-4a45-b393-f5a8b20f7d44), what RC4 key is used by the malware to decrypt its base64-encoded string?

<img width="940" height="338" alt="image" src="https://github.com/user-attachments/assets/e12272e9-64e9-4a14-aca0-2209228b3d0d" />

**Answers: 5329514621441247975720749009**

**Q5**

By examining the MITRE ATT&CK techniques displayed in the [Any.run sandbox report](https://app.any.run/tasks/d55e2294-5377-4a45-b393-f5a8b20f7d44), identify the main MITRE technique (not sub-techniques) the malware uses to steal the user’s password.

The attacker steals user’s credentials from Password Stores while Unsecured Credential is mainly about finding and abusing credentials exposed in files,…

<img width="940" height="308" alt="image" src="https://github.com/user-attachments/assets/c21faf74-22c5-4198-a40c-68767ec90711" />

**Answers: T1555**



**Q6**

By examining the child processes displayed in the [Any.run sandbox report](https://app.any.run/tasks/d55e2294-5377-4a45-b393-f5a8b20f7d44), which directory does the malware target for the deletion of all DLL files?

The malware execute del command targeting at DLL files in C:\\ProgramData

<img width="677" height="409" alt="image" src="https://github.com/user-attachments/assets/5c69f21b-d6a9-46b0-bb3e-035637486c23" />

**Answers: C:\\ProgramData**



**Q7**

Understanding the malware's behavior post-data exfiltration can give insights into its evasion techniques. By analyzing the child processes, after successfully exfiltrating the user's data, how many seconds does it take for the malware to self-delete?

The malware set a timeout of 5 seconds before delete itself

<img width="705" height="397" alt="image" src="https://github.com/user-attachments/assets/d13c735f-0d93-4517-91ac-770b4de6496c" />


**Answers: 5**








