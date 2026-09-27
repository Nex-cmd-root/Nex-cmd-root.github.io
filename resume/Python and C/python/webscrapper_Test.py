import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    url = "https://quotes.toscrape.com/"
    
    # 1. Download the web page content
    response = requests.get(url)
    
    # Check if the connection to the website was successful (Status Code 200)
    if response.status_code != 200:
        print(f"Error: Could not connect to site. Code: {response.status_code}")
        return

    # 2. Convert the raw text into an organized BeautifulSoup structure
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 3. Find all <span> HTML tags that have the CSS class attribute 'text'
    # This acts like your custom search loops across file text lines!
    quote_elements = soup.find_all("span", class_="text")
    
    print(f"--- Successfully Scraped Quotes from {url} ---\n")
    
    # 4. Iterate over the collection match list and print the text cargo
    for i, quote in enumerate(quote_elements, start=1):
        # '.text' strips away the raw HTML tags (like <span>) and keeps just the clean human words
        print(f"Quote {i}: {quote.text}")

if __name__ == "__main__":
    scrape_quotes()