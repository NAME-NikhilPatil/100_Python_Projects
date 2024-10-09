from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")

# driver.close()
driver.quit()
