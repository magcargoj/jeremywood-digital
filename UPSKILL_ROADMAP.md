# Technical Upskill Roadmap & Domain Strategy

Since you are targeting IC3/IC4 Implementation Specialist and Automation Strategist roles, you need to confidently speak the language of a Solutions Architect without needing to write backend code from scratch. This 90-day roadmap focuses strictly on the exact skills companies like Zapier, Affirm, and HubSpot test for.

---

## 90-Day Technical Upskill Roadmap

### Month 1: API & Webhook Mastery
*The goal is to understand how the internet talks to itself. You shouldn't just know what an API is; you need to be able to test one manually.*
1.  **Postman:** Download Postman (it's free). Learn how to send a basic `GET` and `POST` request. 
2.  **REST vs. SOAP:** Understand the difference. 99% of modern SaaS uses REST APIs.
3.  **JSON Payloads:** Learn how to read raw JSON. Understand key-value pairs, arrays, and strings. You need to be able to look at a block of code and say, *"The API call failed because the currency value was passed as a string ('100') instead of an integer (100)."*
4.  **Webhooks:** Understand the difference between an API (polling/asking for data) and a Webhook (event-driven/pushing data). 

### Month 2: Advanced JavaScript & DevTools Debugging
*The goal is to master the browser. As an Implementation Specialist, the browser is your diagnostic surgical table.*
1.  **Chrome DevTools (Network Tab):** Learn how to filter the Network tab by `Fetch/XHR`. If a Meta Pixel fires, you need to know how to click the payload and read the specific event data being passed to the server.
2.  **The Window Object:** Learn how to type `window.dataLayer` into the Chrome Console and press Enter to read the raw array of events sitting on the page.
3.  **Local Storage vs. Cookies:** Understand how the browser stores session IDs and auth tokens.
4.  **Basic JS Functions:** Be able to write a 5-line JavaScript function that grabs a piece of text from a website (`document.querySelector`) and pushes it into the dataLayer. 

### Month 3: Automation Orchestration & Platform Certifications
*The goal is to prove you can connect systems visually.*
1.  **Zapier University:** Go get the "Zapier Certified Expert" badge. It's free, and having it on your LinkedIn makes you a hyper-target for every SaaS company out there.
2.  **HubSpot Academy:** Get the "HubSpot Integration Certification". 
3.  **Data Mapping:** Practice taking complex business problems and drawing out the logical flow (e.g., Lead Submits Form -> Webhook Catch -> JSON Parse -> CRM Update -> Slack Notification). 

---

## Portfolio Domain Name Strategy

If `jeremywood.dev` is unavailable or you want something punchier, here is the strategy for selecting an optimal domain name for an AdOps / Implementation Portfolio:

### 1. The "Tech Native" TLDs
Using a modern Top-Level Domain (TLD) immediately signals that you are technical. Avoid `.com` if it forces you to use a clunky name like `jeremywoodtech.com`.
*   `jeremywood.dev` (Ideal, highest technical authority)
*   `jeremywood.io` (Very startup/SaaS aligned)
*   `jeremywood.tech`
*   `jwood.co`

### 2. The "Action-Oriented" Domains
If you want to brand yourself as a strategic problem-solver rather than just a name:
*   `woodops.dev` (Wood + AdOps)
*   `implementjeremy.io`
*   `jeremyorchestrates.com`

### 3. The "Hungarian Pivot" (High Risk, High Reward)
If you apply heavily to Prezi or GoTo, buying a `.hu` domain is the ultimate "I am moving to Central Europe" flex.
*   `jeremywood.hu`

**Recommendation:** Stick to `jeremywood.dev` or `jeremywood.io`. They look pristine on a resume and scream "Enterprise Tech." Check Porkbun or Namecheap to lock one down today.
