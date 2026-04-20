import json
import requests
import datetime
import os

# Configuration
CONFIG_FILE = 'target_companies.json'
OUTPUT_HTML = 'job_dashboard.html'
OUTPUT_CSV = 'job_leads.csv'

# Search Keywords for "Jeremy's Nomad Freedom Track"
# Focus: High Mastery, Low Stress, Fully Remote
KEYWORDS = ['Technical Support', 'Implementation Specialist', 'Customer Success', 'Support Engineer', 'Happiness Engineer', 'Technical Analyst', 'Specialist']
NEGATIVE_KEYWORDS = ['Senior', 'Lead', 'Manager', 'Architect', 'DevOps', 'Sales Representative', 'Account Executive', 'Director', 'Head of']
REMOTE_KEYWORDS = ['Worldwide', 'Global', 'Anywhere', 'Anywhere in the World']

def fetch_greenhouse(slug):
    url = f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('jobs', [])
    except Exception as e:
        print(f"Error fetching Greenhouse ({slug}): {e}")
    return []

def fetch_ashby(slug):
    # Ashby public API for job boards
    url = f"https://api.ashbyhq.com/posting-api/job-board/{slug}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('jobs', [])
    except Exception as e:
        print(f"Error fetching Ashby ({slug}): {e}")
    return []

def score_job(job_title, location_name):
    title_lower = job_title.lower()
    loc_lower = location_name.lower()
    
    # 1. Immediate Discard for Negative Keywords (Stress Traps)
    if any(k.lower() in title_lower for k in NEGATIVE_KEYWORDS):
        return 0
    
    score = 0
    
    # 2. Freedom Track Match
    if any(k.lower() in title_lower for k in KEYWORDS):
        score += 70
    elif 'support' in title_lower or 'specialist' in title_lower:
        score += 50
    elif 'engineer' in title_lower:
        score += 30 # Lower priority for 'Engineer' titles to keep stress low
    
    # 3. Nomad Elite Match
    if any(k.lower() in loc_lower for k in REMOTE_KEYWORDS):
        score += 30
    elif 'remote' in loc_lower:
        if any(state.lower() in loc_lower for state in ['only', 'unites states', '/ us', 'us only']):
             score += 5
        else:
             score += 15
             
    return score

def main():
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: {CONFIG_FILE} not found.")
        return

    with open(CONFIG_FILE, 'r') as f:
        companies = json.load(f)

    all_leads = []
    
    print("Starting GTM Job Engine Recon...")

    for company in companies:
        name = company['name']
        ats = company['ats']
        slug = company['slug']
        
        print(f"Scouting {name} ({ats})...")
        
        raw_jobs = []
        if ats == 'greenhouse':
            raw_jobs = fetch_greenhouse(slug)
            for rj in raw_jobs:
                title = rj.get('title')
                loc = rj.get('location', {}).get('name', 'Unknown')
                link = rj.get('absolute_url')
                score = score_job(title, loc)
                if score >= 50:
                    all_leads.append({
                        'company': name,
                        'title': title,
                        'location': loc,
                        'url': link,
                        'score': score
                    })
        
        elif ats == 'ashby':
            raw_jobs = fetch_ashby(slug)
            for rj in raw_jobs:
                title = rj.get('title')
                loc = rj.get('location', 'Remote') # Ashby often nests, but public board usually has string
                link = rj.get('jobUrl')
                score = score_job(title, loc)
                if score >= 50:
                    all_leads.append({
                        'company': name,
                        'title': title,
                        'location': loc,
                        'url': link,
                        'score': score
                    })
        
        elif ats == 'manual':
            all_leads.append({
                'company': name,
                'title': 'Check Careers Page / Email',
                'location': 'Manual Check Needed',
                'url': f"https://{slug}",
                'score': 100
            })

    # Sort by score descending
    all_leads.sort(key=lambda x: x['score'], reverse=True)

    # Generate HTML
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html_content = f"""
    <html>
    <head>
        <title>GTM Job Engine - Daily Recon</title>
        <style>
            body {{ font-family: sans-serif; background: #f4f7f6; padding: 40px; color: #333; }}
            .container {{ max-width: 900px; margin: auto; background: white; padding: 20px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
            .lead-card {{ border-bottom: 1px solid #eee; padding: 15px 0; display: flex; justify-content: space-between; align-items: center; }}
            .lead-info h3 {{ margin: 0; color: #3498db; }}
            .lead-info p {{ margin: 5px 0 0; font-size: 0.9em; color: #666; }}
            .score {{ background: #e74c3c; color: white; padding: 5px 10px; border-radius: 4px; font-weight: bold; font-size: 0.8em; }}
            .score.high {{ background: #27ae60; }}
            .apply-btn {{ text-decoration: none; background: #3498db; color: white; padding: 8px 15px; border-radius: 4px; font-size: 0.9em; }}
            .footer {{ margin-top: 20px; font-size: 0.8em; color: #999; text-align: center; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>GTM Recon Report</h1>
            <p>Last Updated: {timestamp}</p>
    """
    
    for lead in all_leads:
        score_class = "high" if lead['score'] >= 80 else ""
        html_content += f"""
            <div class="lead-card">
                <div class="lead-info">
                    <h3>{lead['company']} - {lead['title']}</h3>
                    <p>📍 {lead['location']}</p>
                </div>
                <div style="display: flex; align-items: center; gap: 15px;">
                    <span class="score {score_class}">Score: {lead['score']}</span>
                    <a href="{lead['url']}" class="apply-btn" target="_blank">Recon Role</a>
                </div>
            </div>
        """
        
    html_content += """
            <div class="footer">Generated by Jeremy's GTM Job Engine v1.0</div>
        </div>
    </body>
    </html>
    """

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)

    # Generate CSV
    import csv
    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['company', 'title', 'location', 'url', 'score'])
        writer.writeheader()
        writer.writerows(all_leads)

    print(f"Recon Complete! {len(all_leads)} leads found. Check {OUTPUT_HTML}")

if __name__ == "__main__":
    main()
