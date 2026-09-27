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
    
    quote_boxes = soup.find_all("div", class_="quote")
    
    for i, box in enumerate(quote_boxes, start=1):
        text = box.find("span", class_="text").text
        author = box.find("small", class_="author").text
        print(f"Quote {i}: {text} - {author}")

    print(f"--- Successfully Scraped Quotes from {url} ---\n")

if __name__ == "__main__":
    scrape_quotes()