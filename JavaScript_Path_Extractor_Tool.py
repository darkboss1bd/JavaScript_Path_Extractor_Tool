import requests
import re
from urllib.parse import urlparse, urljoin
import os

print("""\033[35m

██████╗  █████╗ ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝██╔══██╗██╔════╝ ██╔════╝██╔════╝██╔══██╗
██║  ██║███████║██████╔╝█████╔╝ ██████╔╝██║  ███╗█████╗  █████╗  ██║  ██║
██║  ██║██╔══██║██╔══██╗██╔═██╗ ██╔══██╗██║   ██║██╔══╝  ██╔══╝  ██║  ██║
██████╔╝██║  ██║██║  ██║██║  ██╗██████╔╝╚██████╔╝███████╗███████╗██████╔╝
╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═════╝ 
                                                                          
\033[36m
██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
\033[37m
JavaScript Path Extractor Tool - Extract all relative paths from JS files
┌─────────────────────────────────────────────────────────────────────────┐
│ [\033[32m+\033[37m] Developer: darkboss1bd                                  │
│ [\033[32m+\033[37m] Telegram: https://t.me/darkvaiadmin                    │
│ [\033[32m+\033[37m] Channel: https://t.me/windowspremiumkey                │
│ [\033[32m+\033[37m] Website: https://crackyworld.com/                      │
│ [\033[32m+\033[37m] Version: 2.0 | Professional Hacking Tool               │
└─────────────────────────────────────────────────────────────────────────┘
\033[0m
""")

def extract_relative_links(js_url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(js_url, headers=headers, timeout=10)
        response.raise_for_status()
        js_content = response.text
    except requests.RequestException as e:
        print(f"\033[31mError fetching the JavaScript file: {e}\033[0m")
        return [], None

    # Parse the base URL and derive output filename from domain
    parsed = urlparse(js_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    output_filename = f"{parsed.netloc}_paths.txt"

    # Regex to find strings starting with '/'
    pattern = r'(?:"|\')(/[^"\']+)(?:"|\')'
    matches = re.findall(pattern, js_content)

    # Remove duplicates and build absolute URLs
    seen = set()
    links = []
    for rel in matches:
        if rel not in seen:
            seen.add(rel)
            full_url = urljoin(base_url, rel)
            links.append(full_url)

    return links, output_filename

def display_banner():
    print("\033[36m" + "="*70)
    print("🔍 JAVASCRIPT PATH EXTRACTOR - BY darkboss1bd")
    print("="*70 + "\033[0m")

if __name__ == "__main__":
    display_banner()
    
    js_url = input("\033[37m[\033[32m?\033[37m] Enter the JavaScript file URL: \033[36m").strip()
    print("\033[0m")
    
    links, filename = extract_relative_links(js_url)

    if links:
        print(f"\033[32m[\033[37m+\033[32m] Found \033[37m{len(links)}\033[32m unique paths in the JavaScript file\033[0m")
        print("\033[37m[\033[32m*\033[37m] Extracted absolute URLs:\033[36m")
        
        for i, link in enumerate(links, 1):
            print(f"  {i:2d}. {link}")
        
        # Save to domain-based filename
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# JavaScript Path Extractor Results\n")
                f.write(f"# Target: {js_url}\n")
                f.write(f"# Extracted by: darkboss1bd\n")
                f.write(f"# Telegram: https://t.me/darkvaiadmin\n")
                f.write(f"# Total paths found: {len(links)}\n")
                f.write(f"# Date: {requests.get('http://worldtimeapi.org/api/ip').json().get('datetime', 'N/A')}\n")
                f.write("="*50 + "\n\n")
                
                for link in links:
                    f.write(link + "\n")
            
            print(f"\033[32m[\033[37m✓\033[32m] Links have been saved to: \033[37m{filename}\033[0m")
            print(f"\033[32m[\033[37m*\033[32m] File location: \033[37m{os.path.abspath(filename)}\033[0m")
            
        except IOError as e:
            print(f"\033[31m[!] Error writing to file {filename}: {e}\033[0m")
    else:
        print("\033[31m[!] No relative URLs found or an error occurred.\033[0m")
    
    print("\033[36m" + "="*70)
    print("✨ Tool by darkboss1bd | Happy Hacking! 🚀")
    print("="*70 + "\033[0m")
