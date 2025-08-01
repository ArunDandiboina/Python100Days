from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import datetime

url = "https://www.python.org"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(url)

li = chrome_driver.find_elements(By.CSS_SELECTOR, '.event-widget .menu li')

# {'0': {'date': "name"} ...}

d = {}
for index, item in enumerate(li):
    date = datetime.datetime.strptime(item.find_element(By.CSS_SELECTOR, 'time').get_attribute('datetime'), '%Y-%m-%dT%H:%M:%S%z').date()
    name = item.find_element(By.CSS_SELECTOR, 'a').text
    d[index] = {'time': str(date), 'name': name}
print(d)
chrome_driver.close()