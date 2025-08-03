import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(url)

articles = chrome_driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]').text
print(f"Active users: {articles}")

a = chrome_driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[2]/a[1]')
a.click()

# directly use chrome_driver don't need to store the result in a variable and click.

# find by link text
chrome_driver.find_element(By.LINK_TEXT, 'Pages').click()

# search 
chrome_driver.find_element(By.XPATH, '//*[@id="p-search"]/a/span[1]').click()
chrome_driver.find_element(By.NAME, 'search').send_keys('Python', Keys.ENTER)
# chrome_driver.close()