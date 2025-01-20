from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import yaml

def test_login_valid_credentials():
    """Verify that a user can log in with valid credentials."""

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
    valid_credentials = config["valid_credentials"]
    username = valid_credentials["username"]
    password = valid_credentials["password"]

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
        success_message = driver.find_element(By.ID, "flash")
        assert "You logged into a secure area!" in success_message.text
        print("Login test passed!")
    
    except Exception as e:
        print(f"Login test failed: {e}")
    
    finally:
        # Close the browser
        driver.quit()
