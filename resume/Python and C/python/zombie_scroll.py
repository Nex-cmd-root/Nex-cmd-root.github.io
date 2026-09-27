import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def run_headless_scroll_automation():
    print("--- Launching Scroll Automation Driver ---")

    # Execute the browser in headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Load the dedicated JavaScript-powered infinite scroll layout
        driver.get("https://toscrape.com")
        time.sleep(1)
        # Navigate to the exact JavaScript-powered infinite scroll page
        scroll_page_link = driver.find_element(By.LINK_TEXT, "Scroll")
        scroll_page_link.click()
        time.sleep(2)

        # Get initial page height before looping
        last_height = driver.execute_script("return document.body.scrollHeight")
        i = 0

        while True:
            # Scroll to the bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) # Wait for page to load

            # Calculate new page height
            new_height = driver.execute_script("return document.body.scrollHeight")

            # If the height matches the old height, no new content was loaded. Break out!
            if new_height == last_height:
                print("Reached the absolute bottom of the infinite feed.")
                break

            last_height = new_height

            # soft limit for testing purposes, to avoid infinite scrolling in case of a bug
            if i == 10:
                break
            i += 1

        # 3. HARVEST: After scrolling 3 times, let's extract all the quotes currently loaded
        loaded_quotes = driver.find_elements(By.CLASS_NAME, "text")
        print(f"\n[Success] Harvest Complete! Total quotes currently rendered on screen: {len(loaded_quotes)}")
        
        # Print out the first few matches to verify they look accurate
        for index, quote in enumerate(loaded_quotes[:5], start=1):
            print(f"Captured Quote {index}: {quote.text[:50]}...")

        # Save a screenshot before exiting the webpage
        driver.save_screenshot("Data_harvest_proof.png")
        print("Saved screenshot as 'Data_harvest_proof.png'")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        print("\n--- Closing Automated Browser Driver Channel ---")
        driver.quit()

if __name__ == "__main__":
    run_headless_scroll_automation()