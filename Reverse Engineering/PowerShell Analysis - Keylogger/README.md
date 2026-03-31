# 🛡️ Security Writeup – PowerShell Analysis - Keylogger

## 📌 Overview

* **Platform:** BTLO
* **Category:** Reverse Engineering
* **Difficulty:** Easy
* **Date:** 31/03/2026

---

## 📖 Scenario

A suspicious PowerShell script was found on one of our endpoints. 

---

## 🎯 Objectives

Find out what this suspicious PowerShell script does.

---

## 🧰 Tools & Techniques

* Tools: Text Editor


---

## 🔍 Analysis

* Extract the PowerShell script, calculate the hash value of the file and check if it is malicious using Virustotal

<img width="798" height="563" alt="image" src="https://github.com/user-attachments/assets/c4b0f1fd-29bb-408a-af50-96e7e56ac8bf" />

Keystroke Logging: The script continuously monitors the user's keyboard input and captures all keystrokes, including special characters and modifier keys like Shift, Ctrl, and Alt.

<img width="1909" height="895" alt="image" src="https://github.com/user-attachments/assets/836c9080-a8ad-42a2-b983-bbb5fe633c2f" />

<img width="643" height="240" alt="image" src="https://github.com/user-attachments/assets/736e3714-8602-41b2-828e-664ee2f7195d" />

It defines a function called "Start-KeyLogger" that takes an optional parameter for the output file path. The function uses several API calls from the user32.dll library to monitor and record keystrokes.

<img width="647" height="253" alt="image" src="https://github.com/user-attachments/assets/4f4c4b23-a4c8-465e-9a6b-b46c3fbe6638" />

Output File: The keystrokes are saved to a text file specified by the $Path variable. By default, it's set to $env:temp\keylogger.txt, which is the user's temporary directory.

<img width="505" height="46" alt="image" src="https://github.com/user-attachments/assets/5279ba62-7ca5-47a4-abb8-024a49b0a578" />


* The script creates an endless loop that runs for a specified number of times (controlled by the $TimesToRun variable) and a specified runtime period (controlled by the $RunTimeP variable). Within each iteration of the loop, the script waits for 40 milliseconds and then scans all ASCII codes from 9 to 254.


* For each ASCII code, the script checks if the corresponding key is pressed using the GetAsyncKeyState API call. If the key is pressed, it performs additional operations to translate the scan code to a real code, get the keyboard state, and translate the virtual key to a character. If successful, it appends the character to the specified output file.

* Logging Duration: The logging duration is controlled by two variables: $TimesToRun and $RunTimeP. $TimesToRun specifies how many times the keylogger should run, while $RunTimeP determines the duration of each logging session in minutes.
  
<img width="754" height="497" alt="image" src="https://github.com/user-attachments/assets/34301918-faa4-4d37-9e8d-ae232a2aaa6b" />

After the loop completes, the script sends an email with the keylogger results as an attachment using the Send-MailMessage cmdlet. It then removes the output file.

Finally, the script opens the output file in Notepad before exiting.

<img width="715" height="513" alt="image" src="https://github.com/user-attachments/assets/49b4d5af-8ef8-4b4d-8a39-5a73c91aa825" />




## 💡 Lessons Learned

* Always process reverse engineering in an isolate environment
* Using reputation tool like Virustotal with your investigation to obtain more information
---

## ❓ Answers

| Question | Answer |
| -------- | ------ |
| Q1: What is the SHA256 hash value for the PowerShell script file?       | X0b7a2ad2320ac32c262aeb6fe2c6c0d75449c6e34d0d18a531157c827b9754X    |
| Q2: What email address is used to send and receive emails?       | cxxxxxxxxxxxxx@gmail.com    |
| Q3: What is the password for this email account?      | yxxxxxxxxxxx!    |
| Q4: What port is used for SMTP?      | 5x7    |
| Q5: What DLL is imported to help record keystrokes?      | usxxxx.dll    |
| Q6: What directory is the generated txt file put in?      | txxx    |

---

