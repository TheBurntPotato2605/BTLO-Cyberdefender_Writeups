# PoisonedCredentials Lab

Analyze network traffic for LLMNR/NBT-NS poisoning attacks using Wireshark to identify the rogue machine, compromised accounts, and affected systems.

**Scenario**

Your organization's security team has detected a surge in suspicious network activity. There are concerns that LLMNR (Link-Local Multicast Name Resolution) and NBT-NS (NetBIOS Name Service) poisoning attacks may be occurring within your network. These attacks are known for exploiting these protocols to intercept network traffic and potentially compromise user credentials. Your task is to investigate the network logs and examine captured network traffic.

**Note:** LLMNR (UDP/5355) / NBT-NS (UDP/137)

LLMNR and NBT-NS are fallback name-resolution protocols used when DNS cannot resolve a hostname. When a device asks the network “Who has this hostname?”, the request is broadcast to everyone on the local network.

In LLMNR/NBT-NS poisoning, an attacker listens for these broadcast requests and sends a fake reply pretending to be the requested host. The victim then tries to authenticate to the attacker’s machine, often sending NTLM credentials, which the attacker can capture or relay.

**Q1**

In the context of the incident described in the scenario, the attacker initiated their actions by taking advantage of benign network traffic from legitimate machines. Can you identify the specific mistyped query made by the machine with the IP address 192.168.232.162?

<img width="940" height="407" alt="image" src="https://github.com/user-attachments/assets/5cba5cf6-2765-4a3e-9686-b02532cff18c" />

**Answers: fileshaare**

**Q2**

We are investigating a network security incident. To conduct a thorough investigation, We need to determine the IP address of the rogue machine. What is the IP address of the machine acting as the rogue entity?

As we can see, 192.168.232.162 send request to 224.0.0.252 but 192.168.232.215 send response so this is rogue entity

<img width="940" height="411" alt="image" src="https://github.com/user-attachments/assets/82d6b484-1640-495a-96a1-b939ba2c9613" />

**Answers: 192.168.232.215**


**Q3**

As part of our investigation, identifying all affected machines is essential. What is the IP address of the second machine that received poisoned responses from the rogue machine?

<img width="940" height="409" alt="image" src="https://github.com/user-attachments/assets/0a7e7fdc-5bd5-492b-812d-131792660538" />

**Answers: 192.168.232.176**


**Q4**

We suspect that user accounts may have been compromised. To assess this, we must determine the username associated with the compromised account. What is the username of the account that the attacker compromised?

ntlmssp.auth.username help locate packets containing NTLM authentication data, revealing the username of the compromised account.

<img width="940" height="409" alt="image" src="https://github.com/user-attachments/assets/c96eee9d-6581-47bb-9573-49f4643c2e7f" />

**Answers: janesmith**


**Q5**

As part of our investigation, we aim to understand the extent of the attacker's activities. What is the hostname of the machine that the attacker accessed via SMB?

After applying the filter ip.dst == 192.168.232.215 and smb2, look for an SMB2 Session Setup Response containing an NTLMSSP challenge. In the packet details, expand the Target Info field to find the DNS Computer Name. This will reveal the hostname of the machine the attacker accessed via SMB. Additionally, you can check the NetBIOS Name field for further confirmation.

<img width="940" height="428" alt="image" src="https://github.com/user-attachments/assets/375c5dc0-4bd5-4f75-bc98-2ee9d7f32a72" />

**Answers: ACCOUNTINGPC**




