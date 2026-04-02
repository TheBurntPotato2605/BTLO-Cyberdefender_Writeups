# 🛡️ Security Writeup – Barcode World

Do you know the history of barcode?

## 📌 Overview

* **Platform:** BTLO
* **Category:** CTF
* **Difficulty:** Medium
* **Date:** 03/04/2026

The CTF challenge provide us with 9347 .png files from 1.png to 9347.png. They look like some kind of barcode we used to scan for information. Because the number of pictures are too much, we have to use script to automate the task for us. It seems like that each barcode will contain a piece of information that after being joined will give us the flag of the challenge

<img width="1658" height="481" alt="image" src="https://github.com/user-attachments/assets/605121af-7097-4abe-934e-090f5ee3f1ce" />

* First, write a python script named decode.py to extract raw data from images. It will get all images in the folder, sort them in order of 1,2,3,...., decode each barcode using pyzbar library and then save result to a file. After that, we build a combined string as the decoded may look useless when stand alone

<img width="276" height="391" alt="image" src="https://github.com/user-attachments/assets/0429cc09-b7d6-4af4-8969-45c2cf932995" />

* Our result file will look like this:

<img width="244" height="500" alt="image" src="https://github.com/user-attachments/assets/a36a53cc-907f-4c62-b95e-6ee0fe5a7154" />
<img width="128" height="417" alt="image" src="https://github.com/user-attachments/assets/a1da6466-fcd1-40fb-9588-9c48c5be8d76" />

* They remind me of the ASCII character and they are divided by blank space (65 = A, 32 = space). So i try write one more script to interpret the data i achieved before, the digits must be grouped and converted.

<img width="636" height="499" alt="image" src="https://github.com/user-attachments/assets/1c0cd15d-9f39-471a-b379-1345d08131fe" />


* This new script can read from the previous result file, detect the blank seperator, build number from each digit, split them and then convert to character. Lastly, the output decoded character will be saved to a new file.

<img width="616" height="389" alt="image" src="https://github.com/user-attachments/assets/2fbd9265-3e93-44da-8db2-a65ef099e570" />

<img width="630" height="376" alt="image" src="https://github.com/user-attachments/assets/6deba7d4-98a5-44d9-b1fd-c6e68bfe0383" />

* Finally, you can explore the flag from this decoded paragraph. It is SBT{B4r....}

