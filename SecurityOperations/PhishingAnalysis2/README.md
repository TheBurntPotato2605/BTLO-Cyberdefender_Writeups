# [Phishing Analysis 2](https://blueteamlabs.online/home/challenge/phishing-analysis-2-a1091574b8)

Put your phishing analysis skils to the test by triaging and collecting information about a recent phishing campaign.

**Scenario**

Put your phishing analysis skils to the test by triaging and collecting information about a recent phishing campaign.

<img width="940" height="911" alt="image" src="https://github.com/user-attachments/assets/2c063011-74e4-4b6d-82e4-823ad1a160fa" />

**1**.  What is the sending email address? 

<img width="547" height="105" alt="image" src="https://github.com/user-attachments/assets/93336e67-e88b-42a3-9168-562b05f6a3c7" />

**Answers: amazon@zyevantoby.cn**

**2**.  What is the recipient email address? 

<img width="667" height="127" alt="image" src="https://github.com/user-attachments/assets/fcf50af1-7fc6-44cc-88ad-97c76ef9a257" />

**Answers: saintington73@outlook.com**

**3**.  What is the subject line of the email? 

<img width="630" height="142" alt="image" src="https://github.com/user-attachments/assets/737ea074-1662-4105-8e00-243421819cee" />

**Answers: Your account has been locked**

**4**.  What company is the attacker trying to imitate

The attacker tried to trick victim to identify it as a legitimate email from Amazon company

<img width="301" height="60" alt="image" src="https://github.com/user-attachments/assets/ff6b0250-2f81-432b-883c-39bc2c640c3a" />

**Answers: Amazon**

**5**.  What is the date and time the email was sent? (As copied from a text editor) 

<img width="638" height="155" alt="image" src="https://github.com/user-attachments/assets/35f828a2-bf0a-407b-b75d-d70aa934b316" />

**Answers: Wed, 14 Jul 2021 01:40:32 +0900**

**6**.  What is the URL of the main call-to-action button? 

<img width="626" height="55" alt="image" src="https://github.com/user-attachments/assets/0eb240e3-1bde-49d4-8030-66f1a8621662" />

In the bottom of the source file, we can see that a line was base64-encoded.

<img width="940" height="149" alt="image" src="https://github.com/user-attachments/assets/b94f1536-bb15-458a-93e7-35acc2ce9fe3" />

After decoding, we have the HTML content of the email. Search for the button's name to extract the information.

After the href= is the answer we are finding

<img width="940" height="806" alt="image" src="https://github.com/user-attachments/assets/3eabb26e-d574-4fa8-ad70-776790402a40" />

**Answers: https://emea01.safelinks.protection.outlook.com/?url=https%3A%2F%2Famaozn.zzyuchengzhika.cn%2F%3Fmailtoken%3Dsaintington73%40outlook.com&data=04%7C01%7C%7C70072381ba6e49d1d12d08d94632811e%7C84df9e7fe9f640afb435aaaaaaaaaaaa%7C1%7C0%7C637618004988892053%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C1000&sdata=oPvTW08ASiViZTLfMECsvwDvguT6ODYKPQZNK3203m0%3D&reserved=0**

**7**.  Look at the URL using URL2PNG. What is the first sentence (heading) displayed on this site? (regardless of whether you think the site is malicious or not) 

URL2PNG takes too much time to respond so I have to use pikwy instead.

<img width="940" height="879" alt="image" src="https://github.com/user-attachments/assets/69ffee8b-8792-446c-9088-257c19fb9fb5" />

**Answers: This webpage could not be loaded**

**8**.  When looking at the main body content in a text editor, what encoding scheme is being used? 

As we discussed in Q6, the content is base64-encoded

<img width="940" height="921" alt="image" src="https://github.com/user-attachments/assets/34220ba5-639d-4406-95c8-b37b7a647261" />

**Answers: base64**

**9**.  What is the URL used to retrieve the company's logo in the email? 

Ctrl F and find for specific keywords: logo, png, src, image

<img width="940" height="60" alt="image" src="https://github.com/user-attachments/assets/0e01a089-a7a3-4711-b7d2-3c6930b44157" />

**Answers: https://images.squarespace-cdn.com/content/52e2b6d3e4b06446e8bf13ed/1500584238342-OX2L298XVSKF8AO6I3SV/amazon-logo?format=750w&amp;content-type=image%2Fpng**

**10**.  For some unknown reason one of the URLs contains a Facebook profile URL. What is the username (not necessarily the display name) of this account, based on the URL?

Search keyword "facebook" in our content after being decoded and we have a Facbook user's link

<img width="940" height="181" alt="image" src="https://github.com/user-attachments/assets/e320618e-def7-49d0-a76e-0fdc26cc9d97" />

**Answers: amir.boyka.7**



