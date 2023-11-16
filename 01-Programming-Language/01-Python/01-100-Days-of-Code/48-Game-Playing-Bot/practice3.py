from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events={}
for n in range(0,len(dates)):
    events[n] = {
        "time":dates[n].text,
        "name":event[n].text,
    }

print(events)
driver.quit()