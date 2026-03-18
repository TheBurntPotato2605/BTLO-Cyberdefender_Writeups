# WebStrike Lab

Analyze network traffic using Wireshark to investigate a web server compromise, identify web shell deployment, reverse shell communication, and data exfiltration.

**Scenario**

A suspicious file was identified on a company web server, raising alarms within the intranet. The Development team flagged the anomaly, suspecting potential malicious activity. To address the issue, the network team captured critical network traffic and prepared a PCAP file for review.  
Your task is to analyze the provided PCAP file to uncover how the file appeared and determine the extent of any unauthorized activity.

**Hands-on Lab Writeup**

From the description of the lab, we know that our web server was compromised with:

-   Web shell deployment 🡪 Filter for HTTP traffic, POST request with strange parameter, unfamiliar IP addr, upload file with extension like .php, .jsp
-   Reverse shell communications 🡪 Follow TCP stream, check for commands from server like whoami, dir,…
-   Data exfiltration 🡪 Inspect zipped files or high volume download/upload

**1**, Identifying the geographical origin of the attack facilitates the implementation of geo-blocking measures and the analysis of threat intelligence. From which city did the attack originate?

💡 **Note:** The lab machines do not have internet access. To look up the IP address and complete this step, use an IP geolocation service on your local computer outside the lab environment.

<img width="940" height="445" alt="image" src="https://github.com/user-attachments/assets/b7c1c2c4-eeaf-4a03-901f-6b89aa4f1d8a" />

<img width="940" height="444" alt="image" src="https://github.com/user-attachments/assets/f09c76d9-d62f-4b75-9424-4abf5c6959b8" />

**Answer: Tianjin**

**2**, Knowing the attacker's User-Agent assists in creating robust filtering rules. What's the attacker's Full User-Agent?

<img width="940" height="440" alt="image" src="https://github.com/user-attachments/assets/ea8fabb2-6589-4137-a273-9c4dea99ce9a" />

**Answer: Mozilla/5.0 (X11; Linux x86\_64; rv:109.0) Gecko/20100101 Firefox/115.0**

**3**, We need to determine if any vulnerabilities were exploited. What is the name of the malicious web shell that was successfully uploaded?

<img width="940" height="229" alt="image" src="https://github.com/user-attachments/assets/6c4880a1-9850-42d8-9421-a5af25a4d492" />

We have 2 POST requests but only the second one with length of 1302 was successfully uploaded

<img width="940" height="439" alt="image" src="https://github.com/user-attachments/assets/29075ac9-e3c4-4022-8641-d21b14e38af8" />

**Answer: image.jpg.php**

**4**, Identifying the directory where uploaded files are stored is crucial for locating the vulnerable page and removing any malicious files. Which directory is used by the website to store the uploaded files?

<img width="940" height="441" alt="image" src="https://github.com/user-attachments/assets/c1d93c46-ef93-4d10-82f4-0072b1537c41" />

**Answer: /reviews/uploads/**

**5**, Which port, opened on the attacker's machine, was targeted by the malicious web shell for establishing unauthorized outbound communication?

Because port 80 is HTTP’s so we filtered it to view unauthorized outbound connection. And with the destination IP of attacker is 117.11.88.124 so after filtered we know that port 8080 is opened on the attacker’s machine.


<img width="940" height="416" alt="image" src="https://github.com/user-attachments/assets/ba85e638-eb41-4849-bdcc-b5d1a891a345" />

**Answer: 8080**

**6**, Recognizing the significance of compromised data helps prioritize incident response actions. Which file was the attacker attempting to exfiltrate?

View the TCP stream from the attacker’s IP and we have some commands:

<img width="940" height="439" alt="image" src="https://github.com/user-attachments/assets/d65bf036-4800-4ea0-9722-d6fb504ee576" />

**Answer: passwd**
