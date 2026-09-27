import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_browser_automation():
    print("--- Launching Automated Browser Driver ---")
    
    # 1. Initialize the automated Chrome browser instance
    # This will physically open a Chrome window on your desktop screen!
    driver = webdriver.Chrome()
    
    # Maximize the desktop window layout frame for clear visibility
    driver.maximize_window()

    try:
        # 2. Tell the browser to load our target website link address
        driver.get("https://quotes.toscrape.com")
        print("Successfully navigated to website target.")
        
        # Give the website layout page 3 seconds to completely render its assets
        time.sleep(3)

        # 3. Search for a visual element inside the browser layout sheet
        # Instead of BeautifulSoup tag lookups, Selenium uses 'By.CLASS_NAME' or 'By.ID'
        # Let's locate the very first quote text element container
        first_quote_element = driver.find_element(By.CLASS_NAME, "text")
        
        # '.text' extracts the human word content out of the active browser screen
        print(f"\nExtracted Live Text from Screen: {first_quote_element.text}")
        
        # Keep the window open for an additional 3 seconds so you can watch it
        time.sleep(3)

    except Exception as e:
        print(f"An error occurred during browser execution: {e}")
        
    finally:
        # 4. THE GOLDEN RULE OF SELENIUM: Always call quit()!
        # If you don't call quit, the hidden automated background browser processes 
        # stay open forever, draining your computer's RAM memory chips.
        print("\n--- Closing Automated Browser Driver Channel ---")
        driver.quit()

if __name__ == "__main__":
    run_browser_automation()