from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

search = driver.find_element(By.NAME, value="q")
print(search.tag_name)
print(search.get_attribute("placeholder"))

button = driver.find_element(By.ID,value="submit")
print(button.size)

doc_link = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(doc_link.text)

newslink = driver.find_element(By.XPATH,value='//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[3]/a')
print(newslink.text)

    # # Close single tab
# driver.close()

    # # Close entire browser
driver.quit()