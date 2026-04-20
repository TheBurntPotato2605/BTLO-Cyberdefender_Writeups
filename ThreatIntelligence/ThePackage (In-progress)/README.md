# 🛡️ Security Writeup – ThePackage

## 📌 Overview

* **Platform:** BTLO
* **Category:** Threat Intelligence
* **Difficulty:** Easy
* **Date:** 20/04/2026

---

## 📖 Scenario

Authorities are looking for a hacker who is planning to sell a powerful device and the delivery is going to be in a undisclosed but crowded location.

---

## 🎯 Objectives

Find out what product is and obtain more information about this hacker.

---

## 🧰 Tools & Techniques

* Tools: Google
* Techniques: Google Dorking

---

<img width="940" height="311" alt="image" src="https://github.com/user-attachments/assets/32f88656-a43e-4d52-bfa9-7003091566e9" />

 
## 🔍 Analysis

* From the information we are provided from the challenge, we search for the hacking products that the criminal tries to sell.

  <img width="784" height="415" alt="image" src="https://github.com/user-attachments/assets/d7f5f2f2-886f-46e1-83ad-a610d1b35956" />

* We are informed that the profile name of the suspect is jllerenac and is known for being a good hacker and also a good developer. Here, we found his github with 13 repos may expose something useful for investigation. After examining, we still don't acquire any new information.
* Right under his github profile from the browser result, I found another github profile. Reviewing every repos in this account, there is nothing we can use
* But this account has one follower, examine every repos of the follower i found a repo named OSINT (Open-Source Intelligence) which is the practice of collecting, analyzing, and verifying publicly available information to produce actionable intelligence for decision-making across multiple sectors.
  
  <img width="1252" height="664" alt="image" src="https://github.com/user-attachments/assets/a8950045-8b5a-4b39-9b3b-d75c803adc82" />

* We also find that jllerenac - our target committed to this repo too.

  <img width="1564" height="545" alt="image" src="https://github.com/user-attachments/assets/13dd48f8-1e80-494b-9560-707e290ce2f7" />

* Here, we found the coordinates of the meeting and now we have to decode it to know the location
* Using the usual reading of  clues:

second prime number = 3

π to 2 decimals = 3.14

“multiple of the first 5 digits” = 1×2×3×4×5 = 120

sixth Fibonacci value, zero-inclusive = 5

The order that gives a sensible latitude is:

(((−0.841600711036728−3.14)+5)÷3)×120=40.735971558530885

So the full coordinates are:

40.735971558530885, -73.99116596577247

* Use google to find the location and we have:

  <img width="655" height="529" alt="image" src="https://github.com/user-attachments/assets/fe664694-e17a-49c7-b1af-4825a8e686a3" />

---

## 🧾 Key Findings

* Pivoting through related accounts led to an OSINT repository reveal the delivery location.
* The file suspect contributed to in the repo contained encoded meeting coordinates.
* The coordinates point to a crowded public location in NYC


---

## 💡 Lessons Learned

* GitHub profiles, followers, and shared repos can reveal useful OSINT leads.
* Pivoting between related accounts is often necessary in investigations.
* Small clues in public files can expose operational details such as locations.

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the name of the WiFi hacking device?      | Wifi X    |
| Q2: What is the name of the website containing the information of delivery location? (Format: WebsiteName)       | X    |
| Q3: What is the name of the file containing the information of location? (Format: filename.extension)      | X.txt    |
| Q4: Enter the coordinates of the meeting (Format: value, -value)      | 40.X, -73.X   |
| Q5: Where is the delivery going to be? (Format: Location Name)      | X Square    |

---
