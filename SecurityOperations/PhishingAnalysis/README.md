# [Phishing Analysis](https://blueteamlabs.online/home/challenge/phishing-analysis-f92ef500ce)

A user has received a phishing email and forwarded it to the SOC. Can you investigate the email and attachment to collect useful artifacts?

**Scenario**

A user has received a phishing email and forwarded it to the SOC. Can you investigate the email and attachment to collect useful artifacts?

**1**.  Who is the primary recipient of this email?

   <img width="940" height="498" alt="image" src="https://github.com/user-attachments/assets/6cd397f3-6993-488a-9352-22bf43300e97" />

**Answers:** [**kinnar1975@yahoo.co.uk**](mailto:kinnar1975@yahoo.co.uk)

**2**.  What is the subject of this email?

   <img width="931" height="161" alt="image" src="https://github.com/user-attachments/assets/24821299-de60-4399-b9dd-0d3fa07c8d6a" />

**Answers: Undeliverable: Website contact form submission**

**3**.  What is the date and time the email was sent

   <img width="858" height="136" alt="image" src="https://github.com/user-attachments/assets/f40dafd1-5c84-4ea7-957e-0c9418ef290e" />

**Answers: 18 March 2021 04:14**

**4**.  What is the Originating IP? 

Viewing the source of the email we can have the Originating IP

<img width="598" height="86" alt="image" src="https://github.com/user-attachments/assets/2c6271a0-ef0c-47d1-af04-d07b17a566cb" />

**Answers: 103.9.171.10**

**5**.  Perform reverse DNS on this IP address, what is the resolved host? (whois.domaintools.com) 

<img width="940" height="359" alt="image" src="https://github.com/user-attachments/assets/d7cfae78-103c-478c-80ed-87db295b14bd" />

**Answers: c5s2-1e-syd.hosting-services.net.au**

**6**.  What is the name of the attached file? 

<img width="940" height="455" alt="image" src="https://github.com/user-attachments/assets/b0f6b4f0-4059-4d7f-b0f9-2f5b6b282552" />

Stuck here for almost a day because the word in the answer has to be written stick together

**Answers: websitecontactformsubmission.eml**

**7**.  What is the URL found inside the attachment? 

<img width="864" height="239" alt="image" src="https://github.com/user-attachments/assets/5051a9be-c47f-4d64-85bc-36150be81179" />

**Answers: https://35000usdperwwekpodf.blogspot.sg?p=3D9swghttps://35000usdperww= ekpodf.blogspot.co.il?o=3D0hnd**

**8**.  What service is this webpage hosted on? 

<img width="940" height="252" alt="image" src="https://github.com/user-attachments/assets/a362e655-5650-4df2-857f-5354c08d44f3" />

As we can see, these webpage hosted on domain blogspot.sg and blogspot.co.il

So the service used by the 2 webpages is blogger

**Answers: blogger**

**9**. Using URL2PNG, what is the heading text on this page? (Doesn't matter if the page has been taken down!)

**Answers: blog has been removed**

<img width="940" height="270" alt="image" src="https://github.com/user-attachments/assets/23ffb64f-56c1-4911-bf39-7dbbee10e964" />

 




