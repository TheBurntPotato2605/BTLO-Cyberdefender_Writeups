# Yellow RAT Lab
Analyze malware artifacts using threat intelligence platforms like VirusTotal to identify IOCs, C2 servers, and understand adversary tactics.

**Scenario**

During a regular IT security check at GlobalTech Industries, abnormal network traffic was detected from multiple workstations. Upon initial investigation, it was discovered that certain employees' search queries were being redirected to unfamiliar websites. This discovery raised concerns and prompted a more thorough investigation. Your task is to investigate this incident and gather as much information as possible.

<img width="940" height="399" alt="image" src="https://github.com/user-attachments/assets/abd3b501-7a0b-4e67-8ba0-fc0643385a34" />

<img width="940" height="381" alt="image" src="https://github.com/user-attachments/assets/8fc0935a-a729-4cea-9d32-51083af851f9" />

**Q1**

Understanding the adversary helps defend against attacks. What is the name of the malware family that causes abnormal network traffic?
After entering the hash value we have this report of Red Canary about Yellow Cockatoo Rat

<img width="940" height="188" alt="image" src="https://github.com/user-attachments/assets/bacd880a-7751-47e6-8674-1205ac067eb8" />
 
**Answer: Yellow Cockatoo RAT**

**Q2**

As part of our incident response, knowing common filenames the malware uses can help scan other workstations for potential infection. What is the common filename associated with the malware discovered on our workstations?

In the signature info section, we can see the filename that is malware’s signature which means that this file is associated with the malware

<img width="940" height="375" alt="image" src="https://github.com/user-attachments/assets/9ff8ee82-6129-48f5-a4f0-fbc76394256b" />

**Answer: 111bc461-1ca8-43c6-97ed-911e0e69fdf8.dll** 

**Q3**

Determining the compilation timestamp of malware can reveal insights into its development and deployment timeline. What is the compilation timestamp of the malware that infected our network?

<img width="940" height="372" alt="image" src="https://github.com/user-attachments/assets/96ca291b-8182-4ecd-8345-f782083b2680" />

**Answer: 2020-09-24 18:26**

**Q4**

Understanding when the broader cybersecurity community first identified the malware could help determine how long the malware might have been in the environment before detection. When was the malware first submitted to VirusTotal?

<img width="708" height="259" alt="image" src="https://github.com/user-attachments/assets/54655166-2fa5-49d6-8ece-971a29f0dc89" />

**Answer: 2020-10-15 02:47**

**Q5**

To completely eradicate the threat from Industries' systems, we need to identify all components dropped by the malware. What is the name of the .dat file that the malware dropped in the AppData folder?

The malware dropped solarmarker.dat in the AppData folder to remain persistence, load the command-line scripts to execute malicious DLL in victim’s machine

<img width="940" height="456" alt="image" src="https://github.com/user-attachments/assets/78d11399-2286-4b00-bb65-72f0625bb0a1" />

**Answer: solarmarker.dat**

**Q6**

It is crucial to identify the C2 servers with which the malware communicates to block its communication and prevent further data exfiltration. What is the C2 server that the malware is communicating with?

<img width="940" height="311" alt="image" src="https://github.com/user-attachments/assets/44fe4ee3-29df-4cba-9096-b4c36963d06e" />

**Answer: https://gogohid.com**


