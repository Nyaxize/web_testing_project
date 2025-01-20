import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

# Load YAML configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

sauce_url = config["sauce_url"]
sauce_credentials = config["sauce_credentials"]
username = sauce_credentials["username"]
password = sauce_credentials["password"]
products_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt"]

# Initialize Faker
fake = Faker()

def test_saucedemo_purchase():
    """Test the full purchase flow on saucedemo.com."""

    # Set up WebDriver
    service = Service("D:/ZajeciaPotemDoUsuniecia/WebDriver_Chrome/chromedriver.exe")
    options = Options()
    options.binary_location = "C:/Users/Damian/chrome/win64-114.0.5735.90/chrome-win64/chrome.exe"
    options.add_argument("--lang=en")  # Force language to English
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Step 1: Log in
        driver.get(sauce_url)
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        # Step 2: Add products to cart
        for product_name in products_to_add:
            # Wait for each product's "Add to cart" button and click it
            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button')
                )
            )
            add_to_cart_button.click()
        time.sleep(2)

        # Step 3: Go to cart and verify products
        driver.find_element(By.ID, "shopping_cart_container").click()
        time.sleep(2)
        cart_products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        cart_product_names = [product.text for product in cart_products]
        assert set(cart_product_names) == set(products_to_add), "Products in the cart do not match the selected items."
        time.sleep(4)

        # Step 4: Proceed to checkout
        driver.find_element(By.ID, "checkout").click()

        # Step 5: Enter checkout information
        first_name = fake.first_name()
        last_name = fake.last_name()
        zip_code = fake.zipcode()
        driver.find_element(By.ID, "first-name").send_keys(first_name)
        driver.find_element(By.ID, "last-name").send_keys(last_name)
        driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        time.sleep(4)
        driver.find_element(By.ID, "continue").click()
        time.sleep(4)

        # Step 6: Verify prices and total
        item_prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        item_prices = [float(price.text.replace("$", "")) for price in item_prices]
        subtotal_element = driver.find_element(By.CLASS_NAME, "summary_subtotal_label")
        subtotal = float(subtotal_element.text.split("$")[-1])
        assert sum(item_prices) == subtotal, "Subtotal does not match the sum of item prices."

        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total = float(total_element.text.split("$")[-1])
        assert total > subtotal, "Total does not include taxes or fees."

        # Step 7: Finish the purchase
        driver.find_element(By.ID, "finish").click()
        time.sleep(2)

        # Step 8: Verify success message
        success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert success_message == "Thank you for your order!"

        print("Purchase test passed!")

    except Exception as e:
        print(f"Test failed: {e}")

    finally:
        # Close the browser
        driver.quit()
