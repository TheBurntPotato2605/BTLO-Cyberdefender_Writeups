# 🛡️ Security Writeup – Webshell

## 📌 Overview

* **Platform:** BTLO
* **Category:** Network Analysis
* **Difficulty:** Easy
* **Date:** 01/04/2026

---

## 📖 Scenario

The SOC received an alert in their SIEM for ‘Local to Local Port Scanning’ where an internal private IP began scanning another internal system.

---

## 🎯 Objectives

Can you investigate and determine if this activity is malicious or not? You have been provided a PCAP, investigate using any tools you wish.

---

## 🧰 Tools 

* Tools: Wireshark, VirusTotal

---

## 🧠 Investigation Strategy

### As SOC team send and alert about local to local port scanning, we should create and effective stratefy specify this:
* Identify scan pattern SYN scan for no completed TCP handshake as this is classic sign of reconnaissance
* Verify full connect scan  may confirm open port: UDP, TCP 3 way handshake
* Detect port sweep behaviour: from 1 IP host scan to other ports
* Check successful connection -> if port open -> data may be exchanged -> attacker take advantage
---

## 🔍 Analysis



---

### Key Artifact Identification

* Indicator 1: 
* Indicator 2: 



---

## 🧾 Key Findings


---

## 🗺️ Attack Flow / Timeline


---


## 🛡️ Detection Opportunities


---

## 🔐 Prevention & Mitigation



---

## 💡 Lessons Learned


---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1       | xxx    |
| Q2       | xxx    |

---

