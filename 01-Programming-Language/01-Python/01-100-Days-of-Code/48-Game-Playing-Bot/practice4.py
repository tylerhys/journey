from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

num = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
print(num.text)
# num.click()

all_portals = driver.find_element(By.LINK_TEXT,value="English")
# all_portals.click()

search = driver.find_element(By.NAME,value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
# driver.close()