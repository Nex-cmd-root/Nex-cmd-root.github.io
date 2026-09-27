import requests
from bs4 import BeautifulSoup

def scrape_quotes_to_file():
    url = "https://quotes.toscrape.com/"
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not connect to site. Code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    quote_boxes = soup.find_all("div", class_="quote")
    
    print(f"--- Successfully Scraped Quotes from {url} ---\n")

    # Open our output text file in write mode ("w")
    with open("scraped_quotes.txt", "w", encoding="utf-8") as file:

        # Loop through each container block exactly once
        for i, box in enumerate(quote_boxes, start=1):
            # Extract localized variables cleanly inside the loop scope
            text = box.find("span", class_="text").text
            author = box.find("small", class_="author").text
            
            # Grabs all raw text from inside the tags block container
            tags_text = box.find("div", class_="tags").text.strip()
            
            # Format our output data string
            output_line = f"Quote {i}: {text}\nAuthor: {author}\n{tags_text}\n"
            
            # 1. Print to the terminal console screen
            print(output_line.strip())
            
            # 2. Instantly write it permanently to our text file disk
            file.write(output_line + "\n")
            
    print("\n[Success] All data harvested and logged to 'scraped_quotes.txt'!")

if __name__ == "__main__":
    scrape_quotes_to_file()