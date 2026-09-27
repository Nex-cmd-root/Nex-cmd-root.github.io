import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def run_form_automation():
    print("--- Launching Automated Browser Driver ---")
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://toscrape.com")
        time.sleep(2)

        # 1. Navigate to the login screen panel
        login_button = driver.find_element(By.LINK_TEXT, "Login")
        login_button.click()
        print("Moved to Login Page.")
        time.sleep(2) # Give the new form layout page time to load

        # 2. Locate the text input fields
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")

        # 3. KEYBOARD INJECTION: Type text strings into the fields
        print("Typing credentials automatically...")
        username_field.send_keys("MyAutomatedBot")
        time.sleep(1) # Subtle delay so you can visibly see it type
        password_field.send_keys("SecretPassword123")
        time.sleep(1)

        # 4. SUBMIT: Find the login submit button and click it
        # On this sandbox site, the login button uses a CSS class named 'btn-primary'
        submit_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
        submit_button.click()
        print("Form submitted successfully!")

        time.sleep(3) # Pause so you can watch the dashboard load

        # Display success message if the bot logged in
        logout_button = driver.find_element(By.LINK_TEXT, "Logout")
        if logout_button:
            print("-> Authentication Confirmed! The bot is logged in.")
            driver.save_screenshot("login_success_proof.png")     # Save a screenshot of the login page
            print("Visual asset saved: 'login_success_proof.png'")

    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        print("--- Closing Automated Browser Driver Channel ---")
        driver.quit()

if __name__ == "__main__":
    run_form_automation()