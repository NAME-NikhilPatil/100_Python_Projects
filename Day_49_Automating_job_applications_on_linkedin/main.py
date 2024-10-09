from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Here you need your details i has removed my details from hre hehehehehe
ACCOUNT_EMAIL = "your_login_email@example.com"
ACCOUNT_PASSWORD = "your_password"
PHONE = "1234567890"


def abort_application():
    try:
        # Click Close Button
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "artdeco-modal__dismiss"))
        )
        close_button.click()

        time.sleep(2)
        # Click Discard Button
        discard_buttons = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
        if len(discard_buttons) > 1:
            discard_buttons[1].click()
    except (NoSuchElementException, TimeoutException):
        print("Abort elements not found, skipping abort operation.")


# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Click Reject Cookies Button
try:
    time.sleep(2)
    reject_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[action-type="DENY"]'))
    )
    reject_button.click()
except (NoSuchElementException, TimeoutException):
    print("No Reject Cookies button found, continuing...")

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the CAPTCHA manually and logged in...")

# Ensure the page has loaded and listings are available
time.sleep(5)
try:
    all_listings = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container--clickable"))
    )
except TimeoutException:
    print("Job listings not found. Exiting...")
    driver.quit()
    exit()

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        # Insert Phone Number
        time.sleep(5)
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if not phone.get_attribute('value'):
            phone.send_keys(PHONE)

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()

        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except (NoSuchElementException, ElementNotInteractableException) as e:
        print(f"Error: {e}. No application button or element not interactable, skipped.")
        abort_application()
        continue

# Optional: Quit driver after completion
time.sleep(5)
driver.quit()
