# Technical AdOps Interview Playbook

When Affirm (or Stedi) schedules that first interview, you need to seamlessly transition from "Manager" to "Technical Sniper." This playbook gives you the exact scripts and technical answers to pass remote IC interviews.

## 1. The "Specialist" Pivot (Handling the Manager Question)
**The Objection:** *"I see you were a Service Director for 3 years, but recently moved into a Technical Support Specialist role. Why the shift, and what are you looking for next?"*

**Your Script (The "Deliberate Transition" Narrative):**
> "I spent three years as a Service Director, which gave me invaluable perspective on how technical operations connect to business outcomes and P&L. However, I realized my highest impact and personal motivation came from the 'Technical Deep Work' rather than people management.
> 
> **I made a deliberate decision in late 2025 to pivot back into a hands-on Individual Contributor role as a Technical Support Specialist.** I took this step specifically to master the implementation layer—GTM orchestration, API troubleshooting, and raw JS/HTML debugging. 
> 
> I've loved the move, but I'm now looking to take this technical specialization and apply it at an Enterprise SaaS scale with a remote-first organization like [Zapier/Affirm]. I want to be a technical anchor in an environment where precision and automation are the core product, not just a service-line."

*(Note: If they ask why you're leaving BlueTone so soon after the shift, you can mentions that while you love the technical work, the 'remote' promise of the role hasn't met the high standards of a true remote-first company, and you're looking for a culture that is remote-native.)*

## 2. Technical Screening: The "Pixel Troubleshooting" Answer
**The Question:** *"Walk me through how you troubleshoot a client pixel that isn't firing conversions or is double-reporting."*

**Your Script (The "DevTools First" Approach):**
> 1. **Replicate the Environment:** *"First I open the client's site dynamically, ensuring I’m bypassing caching or AdBlockers, and fire up Chrome DevTools right away."*
> 2. **Network Tab Analysis:** *"I immediately go to the Network tab and filter for the specific pixel request (like `bat.bing` or Facebook's `tr`). I trigger the conversion event and check if a network payload actually fires with a 200 OK status."*
> 3. **Payload Inspection:** *"If it fires, I check the payload. Is the `revenue` variable passing null? Has someone hardcoded a string instead of a float?"*
> 4. **GTM Tag Assistant / Container Check:** *"If the Network tab is empty, I open Google Tag Assistant to look at the DataLayer. Usually, I'll find that their developers recently updated the frontend stack (like a React push) and either nuked the DataLayer push entirely, or changed the class of the button that our GTM trigger was bound to."*

## 3. Technical Screening: The "Prioritization" Answer
**The Question:** *"You will have 50 different implementation tickets open at once. How do you prioritize?"*

**Your Script (The SLA/Compliance Approach):**
> *"I prioritize strictly based on Revenue Impact and SLA windows. A malformed pixel on a high-spend campaign that is bleeding attribution data gets tier-1 immediate triage. A new client onboarding ticket gets scheduled into my deep-work block. Because I don't need to escalate to engineering for basic HTML/JS debugging, my resolution time on high-priority tickets is incredibly fast."*

## 4. The "I Can Code" Flex
If they ask what tools you know or if you know HTML/JS:
> *"I'm natively comfortable in raw HTML and JavaScript. I built my entire personal portfolio natively without a CMS to verify that. I don't need to be a full-stack software engineer writing React components all day, but I know exactly how to read a DOM structure, write a script injection in GTM to scrape a value, and read an API response payload to figure out why an integration failed."*

## 5. The "Global Anchor" Flex (Timezone Availability)
**The Question:** *"We are a distributed team. How do you handle working with people in different timezones?"*

**Your Script:**
> "I actually view timezone diversity as a competitive advantage. I spent **four years working consistent overnights**, so I am natively comfortable and highly productive in non-standard hours. As my family and I transition to a nomadic lifestyle, I am not tied to any single geographic schedule. I am 100% willing to align with your team's primary core hours—whether that's US Pacific, European Central, or a 'Follow the Sun' support rotation. I thrive in asynchronous environments, but I am always available for the synchronous 'Global Anchor' blocks your team needs."

## 5. Vetting for Nomad-Friendliness (The "Freedom" Check)
*The Goal:* Ensure you don't get trapped in a "Local Remote" job.

**Questions to ask the Interviewer:**
1. **The Residency Question:** *"Do you have any 'tax residency' requirements for employees, or can we work as true digital nomads as long as our residency is handled via an EOR like Remote.com or Deel?"*
2. **The Asynchronous Question:** *"How much of your communication is synchronous (Zoom) vs. Asynchronous (Post/Slack)? For a nomad team, how do you handle hand-offs across different time zones?"*
3. **The 'States' Question:** *"If I travel or move internationally, does that trigger any internal payroll or HR blockers on your end?"*

## 7. Senior-Tier Technical Scenario: The "Enterprise Scaling" Answer
**The Question:** *"Describe a time you solved a technical issue that had a massive scale or impact."*

**Your Script (The "Systemic Fix" Approach):**
> *"At my digital agency, we had a recurring issue where high-volume e-commerce clients were seeing attribution drops during peak traffic (like Black Friday). Instead of manually fixing each pixel, I conducted a **root-cause analysis** using DevTools and server logs and discovered a script-collision in our standard deployment template.
> 
> I re-architected the tagging logic to fire asynchronously, protecting the site's Time-to-Interactive (TTI) while ensuring 100% data fidelity. I then authored the internal runbook that my team used to migrate 50+ enterprise sites to this new standard. I don't just solve the ticket; I solve the underlying architectural weakness that caused the ticket."*

## 8. Strategic Context: The Senior Salary Anchor
*For Your Ears Only (Internal Strategy):*
Since we have removed the SNAP constraint, your new target range is **$120,000 – $145,000 (Base + Bonus/Equity).** 
- **Anchoring:** If asked for your expectations, say: *"Based on the technical scope of this Senior Implementation role and the Enterprise-scale responsibility, I am looking for a total compensation package in the $135k range, but I'm open to discussing the full benefits and equity component."*
- **Leverage:** Your current $47.8k salary is a relic of your local geography. In the global SaaS market, your "fair market value" is 2.5x higher. Do not let your current paycheck dictate your future value.

## 9. Scientific Evidence of Soft Skills (The Workplace Insights Edge)
**The Question:** *"How do you handle high-pressure conflict or difficult client troubleshooting?"*

**Your Script (The "Validated Profile" Approach):**
> "I actually recently underwent a formal Workplace Insights assessment to better understand my professional DNA. The results validated what I’ve seen in the field: I am categorized as **'Extremely Patient'** and **'Highly Cooperative.'** 
> 
> What that means in practice is that when a client is frustrated by a technical blocker, I don't mirror their stress. I’m naturally unruffled by pressure, which allows me to stay focused on the technical root cause while maintaining social harmony. I value 'Common Ground' as much as I value a '200 OK' status code. For a distributed team like [Company Name], this means I can handle asynchronous conflict with empathy and calm, ensuring that technical friction doesn't turn into team friction."

**The "Goal-Oriented" Pivot:**
> "The same assessment highlighted that I am exceptionally **'Goal-Oriented'** with strong follow-through. I don't just 'work the queue'; I own the resolution. If a ticket requires deep-diving into a legacy JS conflict over a 3 AM shift, I have the intrinsic drive to see that goal through to completion without needing external micromanagement."
