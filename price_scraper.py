
import requests 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from product import Product

URL = "http://www.amazon.com/"
  
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("/Users/kalle/Downloads/chromedriver", chrome_options=options)

# search_term = raw_input("What are you looking for?\n:")

driver.get(URL)
element = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
element.send_keys("32 inch monitor")
element.send_keys(Keys.ENTER)

for i in driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]'):
    name = ""
    price = ""
    prev_price = ""
    for j in range(len(i.find_elements_by_tag_name('h2'))):
        name = i.find_elements_by_class_name('a-price')[j].text
        price = i.find_elements_by_class_name('a-price')[j].text
        prev_price = i.find_elements_by_class_name('a-text-price')[j].text
        product = Product(name, price, prev_price)
