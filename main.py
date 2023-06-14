import requests
from bs4 import BeautifulSoup
import re

print("""
___________.__                              ________.__            _____             .__ 
\_   _____/|  |__   ___________    ____    /  _____/|  |__ _____ _/ ____\____ _______|__|
 |    __)_ |  |  \ /  ___/\__  \  /    \  /   \  ___|  |  \\__  \\   __\\__  \\_  __ \  |
 |        \|   Y  \\___ \  / __ \|   |  \ \    \_\  \   Y  \/ __ \|  |   / __ \|  | \/  |
/_______  /|___|  /____  >(____  /___|  /  \______  /___|  (____  /__|  (____  /__|  |__|
        \/      \/     \/      \/     \/          \/     \/     \/           \/                                                                                    
         [!] Supports multiple keywords
""")
def extract_emails(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all email addresses using regular expressions
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, str(soup))

    return emails

def scrape_website_emails(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all anchor tags
    anchor_tags = soup.find_all('a')

    # Extract email addresses from each URL
    all_emails = []
    for tag in anchor_tags:
        href = tag.get('href')
        if href and href.startswith('http'):  # Consider only external links
            emails = extract_emails(href)
            all_emails.extend(emails)

    return all_emails

# Usage
website_url = 'Site Address'
emails = scrape_website_emails(website_url)
print(emails)
