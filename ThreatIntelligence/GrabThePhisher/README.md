# 🛡️ Security Writeup – GrabThePhisher

## 📌 Overview

* **Platform:** Cyberdefenders
* **Category:** Threat Intelligence
* **Difficulty:** Easy
* **Date:** 05/04/2026

---

## 📖 Scenario

A decentralized finance (DeFi) platform recently reported multiple user complaints about unauthorized fund withdrawals. A forensic review uncovered a phishing site impersonating the legitimate PancakeSwap exchange, luring victims into entering their wallet seed phrases. The phishing kit was hosted on a compromised server and exfiltrated credentials via a Telegram bot.

---

## 🎯 Objectives

Your task is to conduct threat intelligence analysis on the phishing infrastructure, identify indicators of compromise (IoCs), and track the attacker’s online presence, including aliases and Telegram identifiers, to understand their tactics, techniques, and procedures (TTPs).

---




## 🔍 Analysis

* Navigate through the given folder, we have an HTML file named index.html that shows different kinds of crypto wallets. 

<img width="1003" height="710" alt="image" src="https://github.com/user-attachments/assets/984f260e-1495-4479-88ac-ff36d04df4c1" />

<img width="642" height="615" alt="image" src="https://github.com/user-attachments/assets/fff34f9c-8cf6-4fe8-a035-3f927f85befd" />

* However, there is only one source folder of the metamask wallet so it seems that this is the phishing kit we are finding.

<img width="619" height="654" alt="image" src="https://github.com/user-attachments/assets/69a816f5-0c7b-4a61-95b3-4d30bb6f1968" />

* After checking content of the folder, we can see an HTML file: index.html - the frontend of the malicious site, a source php file: metamask.php and a font folder. When viewing the HTML file, it shows that this site tricks user to post their crypto wallet's seed phrase to the server and send it to the hacker. This is definitely a phishing site as metamask never ask user to enter their seed phrase on a strange website. The metamask.php has code for the phishing kit, it takes the information and hacker can access user's wallet. The script collects user input via $_POST["data"], packages it into a message along with additional victim information (IP, location), and exfiltrates it to the attacker via a Telegram bot API.

<img width="1021" height="631" alt="image" src="https://github.com/user-attachments/assets/6e1b1e00-4e68-4993-9da7-0ff9285b4b0f" />

<img width="1019" height="713" alt="image" src="https://github.com/user-attachments/assets/5f4f2733-da6f-4640-8f2d-db84650cf5e4" />

* Investigate further, the attacker try to retrieve the victim's machine information through API call from sypex geo. This service can search for location through IP address. These lines of code will identify the country and city of the victim using their IP and save them to variables: $geo and $city. These information may be used to analyze user's behaviour, optimize phishing campaign and increase reliability based on their geography location.
  
    $request = file_get_contents("http: //api.sypexgeo.net/json/".$_SERVER['REMOTE_ADDR']);
  
    $array = json_decode($request);
  
    $geo = $array->country->name_en;
  
    $city = $array->city->name_en;
  
    $date = date("m.d.Y"); //aaja

* After sending stolen data to the attacker’s Telegram bot, the script also writes a copy locally into log.txt. The log file becomes a repository of all victims’ credentials, IP addresses, and user agents.

<img width="795" height="338" alt="image" src="https://github.com/user-attachments/assets/e89f1077-0115-4d71-831d-a9d5d7f64e52" />

* Here, we review the log.txt file inside the log folder and it shows 3 lines seem to be the seed phrase of crypto wallet. It means that there has 3 victims send their seed phrase to the attacker.

<img width="856" height="304" alt="image" src="https://github.com/user-attachments/assets/71b1a01d-4889-4926-a77e-38672064b7ac" />

* That function is designed to exfiltrate stolen data via Telegram.
  
    $id → the Telegram chat ID of the attacker.

    $token → the Telegram bot token, which authenticates the bot.

    $filename → constructs a Telegram API URL that sends the $message (containing victim’s wallet seed phrase, IP, user     agent,...) to the attacker’s chat.

    file_get_contents($filename); → executes the HTTP request, so the data is delivered to Telegram.

    @file_put_contents(..., $text, FILE_APPEND); → also writes the stolen data into a local file log.txt on the server for backup.

<img width="745" height="138" alt="image" src="https://github.com/user-attachments/assets/f8069dad-bc30-4d0c-b98f-e792edb6789f" />

* This seems like the shout-out of the author to the others hackers and the j1j1b1s@m3r0 look like alias or nickname of the creator. This may help threat intelligence team to attribute phishing kit to specific individual.

<img width="457" height="186" alt="image" src="https://github.com/user-attachments/assets/57408a8d-08b8-4e37-8fdf-eb5290c3de18" />

---

### Key Artifact Identification

* Indicator 1: Telegram Bot Token → 5457463144:AAG8t4k7e2ew3tTi0IBShcWbSia0Irvxm10
* Indicator 2: Telegram Chat ID → 5442785564
* Indicator 3: metamask.php



---

## 🧾 Key Findings

* The phishing kit impersonates a legitimate DeFi platform (PancakeSwap) to trick users into entering their wallet seed phrases.
* The backend script (metamask.php) captures sensitive data submitted via POST requests.
* Victim data is enriched with geolocation information using the SypexGeo API.
* Stolen credentials are exfiltrated via a Telegram bot, acting as a C2 communication channel.
* A local log file (log.txt) stores victim seed phrases, IP addresses, and user agents for backup.
* At least three victims have already submitted their seed phrases.
* The phishing kit includes a potential developer alias: "j1j1b1s@m3r0", which may assist in attribution.

---


## 🧬 Threat Context 

* **Tactic:** Credential Access  

* **Technique:** T1566, T1056, T1567.002 


## 💡 Lessons Learned

## 💡 Lessons Learned

* Users should never enter seed phrases on third-party or untrusted websites.
* Phishing kits often use simple backend scripts  combined with messaging platforms like Telegram for data exfiltration.
* Monitoring outbound connections to services like Telegram can help detect data exfiltration.
* Geolocation APIs are frequently abused by attackers to profile victims and tailor attacks.

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: Which wallet is used for asking the seed phrase?       | metamask    |
| Q2: What is the file name that has the code for the phishing kit?      | metamask.php    |
| Q3: In which language was the kit written?      | php    |
| Q4: What service does the kit use to retrieve the victim's machine information?      | sypex geo    |
| Q5: How many seed phrases were already collected?      | 3    |
| Q6: Could you please provide the seed phrase associated with the most recent phishing incident?      | father also recycle embody balance concert mechanic believe owner pair muffin hockey    |
| Q7: Which medium was used for credential dumping?      | telegram    |
| Q8: What is the token for accessing the channel?      | 5457463144:AAG8t4k7e2ew3tTi0IBShcWbSia0Irvxm10    |
| Q9: What is the Chat ID for the phisher's channel?      | 5442785564    |
| Q10: What are the allies of the phish kit developer?      | j1j1b1s@m3r0    |

---

