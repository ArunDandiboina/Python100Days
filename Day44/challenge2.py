import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://secure-retreat-92358.herokuapp.com/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(url)

# chrome_driver.find_element(By.NAME, 'fName').send_keys('John')
# chrome_driver.find_element(By.NAME, 'lName').send_keys('Doe')
# chrome_driver.find_element(By.NAME, 'email').send_keys('John@gmail.com')
# chrome_driver.find_element(By.CSS_SELECTOR, 'form button').click()

# one line
chrome_driver.find_element(By.NAME, 'fName').send_keys('John', Keys.TAB, 'Doe', Keys.TAB, 'John@gmail.com', Keys.ENTER)

# chrome_driver.close() 