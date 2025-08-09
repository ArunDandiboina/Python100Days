import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import dotenv, os, time
dotenv.load_dotenv()

linkedin_mail = os.getenv("LINKEDIN_MAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")

url = "https://www.linkedin.com/jobs/search-results/?distance=25&f_AL=true&f_TPR=r86400&geoId=105556991&keywords=python&origin=SEMANTIC_SEARCH_HISTORY"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(url)
time.sleep(5)
chrome_driver.find_element(By.ID, "username").send_keys(linkedin_mail)
chrome_driver.find_element(By.ID, "password").send_keys(linkedin_password)
chrome_driver.find_element(By.XPATH, "//button[@type='submit']").click()

# jobs
time.sleep(5)
chrome_driver.find_element(By.XPATH, '//*[@id="jobs-apply-button-id"]').click()
time.sleep(5)
# scroll down the modal popup.
submit_button = chrome_driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
