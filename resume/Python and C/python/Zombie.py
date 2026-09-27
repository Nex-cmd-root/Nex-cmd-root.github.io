import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 1. IMPORT OPTIONS: Required to configure background browser switches
from selenium.webdriver.chrome.options import Options

def run_headless_automation():
    print("--- Initializing Silent Headless Engine ---")
    
    # 2. Configure the background flags
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") # Activates modern headless execution
    chrome_options.add_argument("--window-size=1920,1080") # Sets a default virtual screen resolution
    
    # 3. Pass our options straight to the driver initialization
    # NOTICE: When you run this, NO physical browser window will pop up on your screen!
    driver = webdriver.Chrome(options=chrome_options)

    try:
        print("Navigating to target invisible stream panel...")
        driver.get("https://quotes.toscrape.com")
        time.sleep(2)

        # Scrape data normally to prove the engine is actively running background tasks
        first_quote = driver.find_element(By.CLASS_NAME, "text")
        print(f"\n[Success] Read from background viewport: {first_quote.text}")

        # 4. CAPTURE PROOF: Take a screenshot of the completely hidden browser state!
        driver.save_screenshot("headless_invisible_proof.png")
        print("Saved visual verification asset: 'headless_invisible_proof.png'")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        print("--- Destroying Silent Headless Engine Channel ---")
        driver.quit()

if __name__ == "__main__":
    run_headless_automation()