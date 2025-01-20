import time
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_google_search():
    """Verify that the search functionality in Google works correctly."""

    # Path to ChromeDriver
    service = Service("D:/ZajeciaPotemDoUsuniecia/WebDriver_Chrome/chromedriver.exe")
    
    # Set Chrome options
    options = Options()
    options.binary_location = "C:/Users/Damian/chrome/win64-114.0.5735.90/chrome-win64/chrome.exe" 
    options.add_argument("--lang=en")  # Force language to English

    # Initialize WebDriver with service and options
    driver = webdriver.Chrome(service=service, options=options)
    
    # Load YAML configuration
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Open Google
    google_url = config["google_url"]
    driver.get(google_url)
    print("Browser Language:", driver.execute_script("return navigator.language"))
    time.sleep(2)

    # Handle cookie popup
    try:
        accept_cookies_button = driver.find_element(By.XPATH, '//button[.//text()="Reject all"]')
        accept_cookies_button.click()
        print("Clicked 'Reject all'.")
    except Exception as e:
        print("Cookie popup not found, proceeding.")

    time.sleep(2)

    # Find the search box and type a query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Test automation with Selenium")
    search_box.send_keys(Keys.RETURN)

    # Verify the results page
    assert "Selenium" in driver.title

    # Close the browser
    driver.quit()
