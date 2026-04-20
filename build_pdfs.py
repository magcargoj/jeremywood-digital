import os
import subprocess
import glob
import markdown

# Configuration
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE_DIR = os.getcwd()

# Professional CSS for Markdown to PDF conversion
MD_CSS = """
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
}
h1, h2, h3 { color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 5px; }
h1 { font-size: 2.2em; }
h2 { font-size: 1.8em; margin-top: 30px; }
h3 { font-size: 1.4em; }
p, li { font-size: 1.1em; }
code { background: #f4f4f4; padding: 2px 5px; border-radius: 3px; font-family: monospace; }
blockquote { border-left: 5px solid #3498db; padding-left: 15px; color: #555; font-style: italic; }
@media print {
    body { margin: 0; padding: 0; }
}
"""

def html_to_pdf(html_file, pdf_file):
    print(f"Converting {os.path.basename(html_file)} -> {os.path.basename(pdf_file)}...")
    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_file}",
        f"file:///{html_file.replace(os.sep, '/')}"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"  Error converting {html_file}: {e.stderr}")
        return False

def md_to_pdf(md_file, pdf_file):
    print(f"Converting {os.path.basename(md_file)} -> {os.path.basename(pdf_file)}...")
    with open(md_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    html_content = markdown.markdown(text)
    full_html = f"<html><head><style>{MD_CSS}</style></head><body>{html_content}</body></html>"
    
    temp_html = md_file + ".temp.html"
    with open(temp_html, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    success = html_to_pdf(temp_html, pdf_file)
    os.remove(temp_html)
    return success

def main():
    if not os.path.exists(CHROME_PATH):
        print(f"Error: Chrome not found at {CHROME_PATH}")
        return

    # 1. Handle HTML files
    html_files = glob.glob(os.path.join(BASE_DIR, "RESUME_*.html")) + \
                 glob.glob(os.path.join(BASE_DIR, "COVER_LETTER_*.html")) + \
                 glob.glob(os.path.join(BASE_DIR, "jeremy_wood_*.html")) + \
                 glob.glob(os.path.join(BASE_DIR, "cover_letter_*.html"))

    for html_file in html_files:
        pdf_file = html_file.replace(".html", ".pdf")
        html_to_pdf(html_file, pdf_file)

    # 2. Handle Markdown files (Specific ones for applications/outreach)
    md_patterns = ["*APPLICATION_DRAFT.md", "COVER_LETTER_*.md", "cover_letter_*.md", "OUTREACH_*.md", "RESUME_*.md"]
    md_files = []
    for pattern in md_patterns:
        md_files.extend(glob.glob(os.path.join(BASE_DIR, pattern)))

    for md_file in md_files:
        pdf_file = md_file.replace(".md", ".pdf")
        md_to_pdf(md_file, pdf_file)

    print("\nPDF Generation Complete.")

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()
