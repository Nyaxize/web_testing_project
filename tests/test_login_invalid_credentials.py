from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import yaml

def test_login_invalid_credentials():
    """Verify that the system rejects login attempts with invalid password."""

    # Path to ChromeDriver
    service = Service("D:/ZajeciaPotemDoUsuniecia/WebDriver_Chrome/chromedriver.exe")
    
    # Set Chrome options
    options = Options()
    options.binary_location = "C:/Users/Damian/chrome/win64-114.0.5735.90/chrome-win64/chrome.exe"
    driver = webdriver.Chrome(service=service, options=options)

    # Load YAML configuration
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    login_url = config["login_url"] + config["login_page"]
    invalid_credentials = config["invalid_credentials"]
    username = invalid_credentials["username"]
    password = invalid_credentials["password"]

    try:
        # Step 1: Open login page
        driver.get(login_url)
        time.sleep(2)  # Wait for the page to load

        # Step 2: Enter username
        username_field = driver.find_element(By.NAME, "username")
        username_field.send_keys(username)  

        # Step 3: Enter password
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys(password)  

        # Step 4: Click the login button
        login_button = driver.find_element(By.CLASS_NAME, "radius")
        login_button.click()

        # Step 5: Verify login success
        time.sleep(3)  # Wait for redirection
        failed_message = driver.find_element(By.ID, "flash")
        assert "Your password is invalid!" in failed_message.text
        print("Login test passed!")
    
    except Exception as e:
        print(f"Login test failed: {e}")
    
    finally:
        # Close the browser
        driver.quit()
