import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_screenshot_automation():
    print("--- Launching Visual Capture Driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://toscrape.com")
        time.sleep(1)
        scroll_page_link = driver.find_element(By.LINK_TEXT, "Scroll")
        scroll_page_link.click()
        time.sleep(3)

        # Let's execute a quick scroll action to populate the frame layout
        print("Scrolling down to render fresh dynamic components...")
        driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(2)

        # THE CAPSTONE INTERACTION: Capture the active browser window layout
        # Give it a clean file name ending in '.png'
        filename = "automation_snapshot.png"
        driver.save_screenshot(filename)
        
        print(f"[Success] Desktop frame frozen and saved as '{filename}'!")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        print("--- Closing Automated Browser Driver Channel ---")
        driver.quit()

if __name__ == "__main__":
    run_screenshot_automation()