# [ATT&CK](https://blueteamlabs.online/home/challenge/attck-0e4914db5d)

You are hired as a Blue Team member for a company. You are assigned to perform threat intelligence for the company. See how you can operationalize the MITRE ATT&CK framework to solve these scenario-based problems.

**Scenario**

You are hired as a Blue Team member for a company. You are assigned to perform threat intelligence for the company. See how you can operationalize the MITRE ATT&CK framework to solve these scenario-based problems.

**1**.  Your company heavily relies on cloud services like Azure AD, and Office 365 publicly. What technique should you focus on mitigating, to prevent an attacker performing Discovery activities if they have obtained valid credentials? (Hint: Not using an API to interact with the cloud environment!) 

In this technique, after using stolen credentials, hacker may take advantage of this to explore our system

<img width="940" height="135" alt="image" src="https://github.com/user-attachments/assets/a31a8a61-c653-4c48-b845-c9e0cfb7c8c7" />

**Answer: T1538**


**2**.  You were analyzing a log and found uncommon data flow on port 4050. What APT group might this be? 

This group used a non-standard port to make external communication

<img width="940" height="120" alt="image" src="https://github.com/user-attachments/assets/cb0e38e4-91d0-4b3d-9a30-7ff326b4e2e1" />

**Answer: G0099**


**3**.  The framework has a list of 9 techniques that falls under the tactic to try to get into your network. What is the tactic ID? 

<img width="940" height="65" alt="image" src="https://github.com/user-attachments/assets/55453a15-7adf-40b5-af0e-6619db05d560" />

**Answer: TA0001**


 **4**.   A software prohibits users from accessing their account by deleting, locking the user account, changing password etc. What such software has been documented by the framework? 

This techniques’s description is the most suitable to the behavior of the software we are finding

<img width="940" height="138" alt="image" src="https://github.com/user-attachments/assets/7e2ac76a-80ab-48a7-a691-a741a41f6051" />

Here we have 3 softwares that are described exactly like the question

<img width="940" height="163" alt="image" src="https://github.com/user-attachments/assets/822b9d68-6734-4e67-b997-07ba456f3157" />

**Answer: S0372**


**5**.   Using ‘Pass the Hash’ technique to enter and control remote systems on a network is common. How would you detect it in your company?

Pass the Hash abuse password’s hash to log in instead of using valid password

This is a technique of Lateral movement because after that they can login other device in the same domain without knowing the passwords 

<img width="940" height="138" alt="image" src="https://github.com/user-attachments/assets/c643801c-b286-438e-8df1-caeacaecb9f0" />

I use Google Dork for this question with keywords of "Pass the Hash", "Monitor...disprecancies", "T1550.002" and I have found [this page](https://mitre.ptsecurity.com/en-US/T1550.002) contains the answer as MITRE ATT&CK does not provide a clear answer

<img width="940" height="273" alt="image" src="https://github.com/user-attachments/assets/611e22e1-b36f-4a63-a418-fb9da4d73eb1" />

**Answer: Monitor newly created logons and credentials used in events and review for discrepancies**
