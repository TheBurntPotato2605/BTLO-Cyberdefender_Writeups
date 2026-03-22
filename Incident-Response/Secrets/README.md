# 🛡️ Security Writeup – Secrets

## 📌 Overview

* **Platform:** BTLO
* **Category:** Incident Repsponse
* **Difficulty:** Easy
* **Date:** 22/03/2026

---

## 📖 Scenario

You’re a senior cyber security engineer and during your shift, we have intercepted/noticed a high privilege actions from unknown source that could be identified as malicious. We have got you the ticket that made these actions.
You are the one who created the secret for these tickets. Please fix this and submit the low privilege ticket so we can make sure that you deserve this position.
Here is the ticket:

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiQlRMe180X0V5ZXN9IiwiaWF0Ijo5MDAwMDAwMCwibmFtZSI6IkdyZWF0RXhwIiwiYWRtaW4iOnRydWV9.jbkZHll_W17BOALT95JQ17glHBj9nY-oWhT1uiahtv8

---

## 🎯 Objectives

Find the secret, fix and submit the low privilege ticket

---

## 🧰 Tools 

* Tools: Cyberchef, Hashcat

---


## 🔍 Analysis

 * From the scenario, we know that a suspicious ticket (authentication token) was intercepted so we can assume that this ticket use some kind of encrypt to hide its secret.
 * Upload this string to Cyberchef and use Magic to identify the kind of encode this ticket used

   <img width="1919" height="903" alt="image" src="https://github.com/user-attachments/assets/c9b2b2e4-a982-4cef-b123-c215e865cd57" />

   So this is JWT-encoded

* JWT is made up of three parts: a header, a payload, and a signature, all encoded in Base64URL and separated by dots. This structure ensures secure transmission of claims between parties.

  <img width="1576" height="470" alt="image" src="https://github.com/user-attachments/assets/5cbb3801-b1c3-4f71-aba9-7219ed912811" />

  Now, our objective is to find out the secret 

* As all parts of JWT is encoded in Base64URL, we use Base64 decode for more information of the ticket

  <img width="1576" height="481" alt="image" src="https://github.com/user-attachments/assets/8bd9ee97-f399-4f4b-b17a-8ba3b5a8750d" />

  As we can see, the header is {"typ":"JWT","alg":"HS256"} and the payload is {"flag":"BTL{_4_Eyes}","iat":90000000,"name":"GreatExp","admin":true}. The algorithm used here is HS256 come with a flag with the value of BTL{4_Eyes}, the timestamp here also looks suspicious 90000000 (about 50 years ago) and the admin true indicates high privilege actions.

* From the header, we see that token is encoded with JWT and HS256. So that if we want to find out the secret part of token, we will use hashcat to brute force it with character mask attack.

  <img width="1254" height="918" alt="image" src="https://github.com/user-attachments/assets/0b0c628b-7577-471e-a5f9-063a833ab0fd" />

Luckily, after tried with 4-character mask attack because of the hint from flag: 4_Eyes we have the secret is bT!0

---

## 🧾 Key Findings

* Dictionary attack may ineffective but weak secret key may easuly become a vulnerability
* Privilege abuse of high privilege role like admin

---

## 💡 Lessons Learned

* Strong secrets are necessary to protect your application
* JWT is encoded not encrypted so store sensitive data in the payload is risky

---

## ❓ Answers

| Question | Answer |
|----------|--------|
| Q1: Can you identify the name of the token? | JWT |
| Q2: What is the structure of this token? | Header.Payload.Signature |
| Q3: What is the hint you found from this token? | 4_Eyes |
| Q4: What is the Secret? | bT!0 |
| Q5: Can you generate a new verified signature ticket with a low privilege? | eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiQlRMe180X0V5ZXN9IiwiaWF0Ijo5MDAwMDAwMCwibmFtZSI6IkdyZWF0RXhwIiwiYWRtaW4iOmZhbHNlfQ.nMXNFvttCvtDcpswOQA8u_LpURwv6ZrCJ-ftIXegtX4 |

---
