import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://appbrewery.github.io/Zillow-Clone/"
LINK_FORM = ("https://docs.google.com/forms/d/e/1FAIpQLSdJqNXCmQcBOJbDLqMTMf9EbK5YlZB_yNiPvT59DERvbQBbrQ/viewform?usp"
             "=sf_link")

response = requests.get(URL)
properties = response.text
soup = BeautifulSoup(properties, 'html.parser')

link_soup = soup.find_all(name='a', class_='StyledPropertyCardDataArea-anchor')
price_soup = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine")

# ---------Create a list of links for all the listings you scraped-------
links = []

for link in link_soup:
    link_text = link.get('href')
    links.append(link_text)

# ------------Create a list of prices for all the listings you scraped--------
prices = []

for price in price_soup:
    value = price.text.strip().split('+')[0].split('/')[0]  # removes appendix on the price e.g. '+/mo' or '/mo'
    prices.append(value)

# ------------Create a list of addresses for all the listings you scraped------
addresses = []

for address in link_soup:
    address_tag = address.find('address')
    address_text = address_tag.get_text(strip=True).replace('|', "")  # clean up address data from unnecessary symbols
    addresses.append(address_text)

# ---------------Use Selenium to fill in the form you created---------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(LINK_FORM)

# Enter values in form
for entry in range(len(links)):
    address_form = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div['
                                                                                         '2]/div/div[2]/div['
                                                                                         '1]/div/div/div[2]/div/div['
                                                                                         '1]/div/div[1]/input')))
address_form.send_keys(addresses[entry])

price_form = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
price_form.send_keys(prices[entry])

link_form = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
link_form.send_keys(links[entry])

send_button = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()

more_data_button = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
