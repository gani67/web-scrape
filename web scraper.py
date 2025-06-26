import requests
from bs4 import BeautifulSoup

# Step 1: Target URL (example: BBC News)
url = 'https://www.bbc.com/news'

# Step 2: Fetch the HTML content
response = requests.get(url)
html_content = response.text

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4: Find headline elements (usually in <h2> tags)
headlines = soup.find_all('h2')

# Step 5: Extract and save the headlines to a text file
with open('headlines.txt', 'w', encoding='utf-8') as file:
    for h in headlines:
        text = h.get_text(strip=True)
        if text:  # avoid empty headlines
            file.write(text + '\n')

print("✅ Headlines saved to 'headlines.txt'")