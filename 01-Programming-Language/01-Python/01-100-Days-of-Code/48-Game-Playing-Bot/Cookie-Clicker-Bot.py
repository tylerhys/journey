from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,value="cookie")
store = driver.find_elements(By.CSS_SELECTOR,value="#store div b")

store_dict = {}
for item in store:
    temp = item.text.split(sep=" - ")
    if len(temp) > 1:
        store_dict[temp[0]] = int(temp[1].replace(",",""))

check_time = time.time() + 5
end_time = time.time() + 2*60

Loop = True
while Loop:
    cookie.click()
    if time.time() > check_time:
        money = driver.find_element(By.ID,value="money")
        for item in store_dict:
            if int(money.text.replace(",","")) > store_dict[item]:
                buy = item
        driver.find_element(by=By.ID, value=f"buy{buy}").click()
        check_time = time.time() + 5
    if time.time() > end_time:
        Loop = False
        print(driver.find_element(By.ID,value="cps").text)

driver.quit()