from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Initialize the WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Define the items to be added to the cart
items_to_add = {
    "Mushroom - 1 Kg": 5,
    "Potato - 1 Kg": 4,
    "Corn - 1 Kg": 2,
    "Banana - 1 Kg": 2,
    "Water Melon - 1 Kg": 1
}

# Iterate through the items and add them to the cart
for item, quantity in items_to_add.items():
    # Search for the item
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-keyword"))
    )
    search_box.clear()
    search_box.send_keys(item)

    # Increment the quantity
    for _ in range(quantity):
        # Increment
        increment_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.increment"))
        )
        increment_button.click()
        time.sleep(1)

    # Add to Cart
    add_to_cart_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-action button")))

    # Once the button is visible, click on it
    add_to_cart_button.click()

    for _ in range(quantity):
        decrement_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.decrement"))
        )
        decrement_button.click()

# Click on the cart
cart_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='Cart']"))
)
cart_button.click()

# Click on "Proceed to Checkout" button
proceed_to_checkout_button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))
)
proceed_to_checkout_button.click()

# Verify the items in the cart
cart_items = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.product-name"))
)

for item in items_to_add.keys():
    assert any(item.lower() in cart_item.text.lower() for cart_item in cart_items), f"{item} not found in the cart."

print("Test succeeded! All items were found in the cart.")

# Close the browser
driver.quit()
