import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

url = "https://www.python.org"
amazon_product_url = "https://www.amazon.in/gp/aw/d/B08NC3Q2FQ/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=05ff58259c9d352675aa76260f5bdb2d&hsa_cr_id=0&qid=1752626962&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&ref_=sbx_be_s_sparkle_lsi4d_asin_0_price&pd_rd_w=BfI8G&content-id=amzn1.sym.cbe1d71a-30e3-45dc-b787-bad221b13c68%3Aamzn1.sym.cbe1d71a-30e3-45dc-b787-bad221b13c68&pf_rd_p=cbe1d71a-30e3-45dc-b787-bad221b13c68&pf_rd_r=ZGTKF1YV9Z2Z3S7X6FFH&pd_rd_wg=HWahG&pd_rd_r=14c11177-4e13-4523-b3c6-94cb90eaeb17&th=1"

# option to stay open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver
chrome_driver = webdriver.Chrome(options=chrome_options)

chrome_driver.get(url)

# link = chrome_driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a').get_attribute("href")
# print(link)

# chrome_driver.find_element(By.NAME, "q").send_keys("Python")
# chrome_driver.find_element(By.NAME, "q").submit()

# find the price element by XPath
# price_element = chrome_driver.find_element(By.XPATH, '//span[@class="a-price-whole"]')
# print(f"Price: {price_element.text}")
# print(price_element) # selenium.webdriver.remote.webelement.WebElement


# close tab - if you have multiple tabs open
chrome_driver.close()

# close browser - entire browser window
# chrome_driver.quit()