import requests
from bs4 import BeautifulSoup
import time # Implements a gentle delay so we don't spam the website's server

def crawl_multiple_pages():
    # Start on the very first page
    current_url = "https://quotes.toscrape.com"
    page_counter = 1
    max_pages_to_scrape = 3 # Hard limit so our script doesn't run forever during testing

    print("--- Initiating Multi-Page Web Crawler ---\n")

    while current_url and page_counter <= max_pages_to_scrape:
        print(f"[Crawling Page {page_counter}] Connecting to: {current_url}")
        
        response = requests.get(current_url)
        if response.status_code != 200:
            print("Failed to reach page. Terminating crawl.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        quote_boxes = soup.find_all("div", class_="quote")

        #  Open all_scraped_pages and save the full text and author in a clean format
        with open("all_scraped_pages.txt", "a", encoding="utf-8") as file:
            file.write(f"=== PAGE {page_counter} DATA ===\n\n")
            for i, box in enumerate(quote_boxes, start=1):
                text = box.find("span", class_="text").text
                author = box.find("small", class_="author").text
                format = f"Quote {i}: {text}\nAuthor: {author}\n"

                file.write(format)
            file.write("\n") # Add a blank line between pages for clarity
        print("quotes saved to \"all_scraped_pages.txt\"\n")

        # === THE PAGINATION GATE ===
        # Look for the 'next' button container in the HTML layout
        # <li class="next"><a href="/page/2/">Next</a></li>
        next_button_box = soup.find("li", class_="next")
        
        if next_button_box:
            # Extract the raw anchor href link: "/page/2/"
            next_page_partial = next_button_box.find("a").get("href")
            
            # Reconstruct the absolute URL for the NEXT loop iteration
            current_url = "https://quotes.toscrape.com" + next_page_partial
            page_counter += 1
            
            # GENTLE SCRAPING ETHICS: Pause the program for 1 second before loading the next page.
            # This mimics human behavior and prevents your script from overloading the site's server.
            time.sleep(1)
        else:
            # If find() returns None, there is no "Next" button. We have reached the final page!
            print("\n[End of Web Map] No further pages detected.")
            current_url = None # This breaks the while loop cleanly

    print(f"\n[Success] Crawl complete! Successfully processed {page_counter - 1} continuous pages.")

if __name__ == "__main__":
    crawl_multiple_pages()