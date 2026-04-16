# 🛡️ Security Writeup – Shiba Insider

## 📌 Overview

* **Platform:** BTLO
* **Category:** CTF
* **Difficulty:** Easy
* **Date:** 16/04/2026

---

## 📖 Scenario

Can you uncover the insider?

---

## 🎯 Objectives

Discover the insider

---

## 🧰 Tools & Techniques

* Tools: Wireshark, Steghide, Exiftool, CyberChef

---


## 🔍 Analysis

* Open the insider.pcap file using Wireshark, we can see a TCP session between 192.168.176.1 and 192.169.176.145. This is user asking the server for hide.txt with a query parameter message "how do i open file" and the server response with plain text "use your own password"

  <img width="1798" height="168" alt="image" src="https://github.com/user-attachments/assets/ff8cffde-da6e-47da-958a-0db1ef1ed419" />

* As we know, in an HTTP request, the Authorization header usually contains authentication credentials used to prove the client’s identity or access rights. Here, we have Basic authentication. This contains a Base64-encoded username and password so we will discover their credential using CyberChef

  <img width="809" height="477" alt="image" src="https://github.com/user-attachments/assets/0566c2fe-a7e5-4b46-9efd-e4d013a0776b" />

* As the result, we achieve user name: "fakeblue" with password: "redforever"

  <img width="1532" height="687" alt="image" src="https://github.com/user-attachments/assets/20688ce4-0b7f-498f-adc9-dff8c2b2b4a4" />

* Based on the password we decoded, open the file.zip and we have a README.txt file with a picture file ssdog1.jpeg

  <img width="358" height="192" alt="image" src="https://github.com/user-attachments/assets/7dae32d5-1e8b-411e-94a3-c082df56f9bd" />
  
* From the information from README.txt, it seems that no more password will be required

  <img width="634" height="88" alt="image" src="https://github.com/user-attachments/assets/f6a05994-ca8a-400a-8b2f-fc8d897c301a" />

* Now, we use Exiftool to gather more information about the suspicious Shiba picture

  <img width="617" height="444" alt="image" src="https://github.com/user-attachments/assets/eaf20cf9-aa9d-4d7f-8eac-8dd72d71583d" />

* The result points out that this picture is just a cover file for hidden data. It used steganography technique to hide data so we use Steghide to uncover that.

  <img width="614" height="165" alt="image" src="https://github.com/user-attachments/assets/8a74acf7-9296-48b7-a05c-5e87a2b48649" />

* The steghide info used to discover information about a stego or cover file. The hidden file here is a text file idInsider.txt

  <img width="614" height="165" alt="image" src="https://github.com/user-attachments/assets/641916f4-d561-48f0-afec-0f6ea93253e0" />

* Earlier, we are hinted from the README.txt that no more password is needed so here I extract the ssdog1.jpeg file using no password. And here we achieve a text file with and ID that maybe from some kind of platform or social media.
  
  <img width="630" height="149" alt="image" src="https://github.com/user-attachments/assets/209b67e7-e595-4a18-acbf-f3a45917b75b" />

* Remember when we login BTLO and go to profile page, we have a string that look like user ID so i try paste that ID to the URL: https(:)//blueteamlabs.online/home/user/0726ba878ea47de571777a.

  <img width="1914" height="846" alt="image" src="https://github.com/user-attachments/assets/48a25833-ef4a-42ab-be3e-9fcc6320522e" />


* It indicates a profile with user name of bluetiger


---




## 💡 Lessons Learned

* Basic Authentication only uses Base64 encoding, not encryption, so credentials can often be recovered easily from captured traffic.
* Metadata analysis with tools like **Exiftool** can reveal clues that point to hidden or manipulated content.
* Steganography is a simple but effective way to conceal data, so tools like **Steghide** are valuable during forensic analysis.
* CTF and real-world investigations both benefit from following the full evidence chain rather than treating artifacts in isolation.

---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the response message obtained from the PCAP file?       | use your X X    |
| Q2: What is the password of the ZIP file?        | redXXXXXXX    |
| Q3: Will more passwords be required?       | XX    |
| Q4: What is the name of a widely-used tool that can be used to obtain file information?       | ExifXXXX    |
| Q5: What is the name and value of the interesting information obtained from the image file metadata?      | Technique.X    |
| Q6: Based on the answer from the previous question, what tool needs to be used to retrieve the information hidden in the file?      | Steg    |
| Q7: Enter the ID retrieved.      | 0XXXXXXa    |
| Q8: What is the profile name of the attacker?      | blueXXXXX    |

---

