import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_scroll_automation():
    print("--- Launching Scroll Automation Driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Load the dedicated JavaScript-powered infinite scroll layout
        driver.get("https://toscrape.com")
        time.sleep(1)
        # Navigate to the exact JavaScript-powered infinite scroll page
        scroll_page_link = driver.find_element(By.LINK_TEXT, "Scroll")
        scroll_page_link.click()
        time.sleep(3)

        # We will loop 3 times to simulate a user scrolling down 3 full pages
        scroll_count = 3
        for i in range(scroll_count):
            print(f"Executing automated page scroll action [{i + 1}/{scroll_count}]...")
            
            # 1. Command the browser layout window to slide to the absolute bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # 2. CRUCIAL DELAY: Give the website's background JavaScript 2 full seconds 
            # to fetch the new records from the server and render them onto the desktop screen.
            time.sleep(2)

        # 3. HARVEST: After scrolling 3 times, let's extract all the quotes currently loaded
        loaded_quotes = driver.find_elements(By.CLASS_NAME, "text")
        print(f"\n[Success] Harvest Complete! Total quotes currently rendered on screen: {len(loaded_quotes)}")
        
        # Print out the first few matches to verify they look accurate
        for index, quote in enumerate(loaded_quotes[:5], start=1):
            print(f"Captured Quote {index}: {quote.text[:50]}...")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        print("\n--- Closing Automated Browser Driver Channel ---")
        driver.quit()

if __name__ == "__main__":
    run_scroll_automation()