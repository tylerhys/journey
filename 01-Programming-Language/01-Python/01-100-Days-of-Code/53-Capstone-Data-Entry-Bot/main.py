import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

x = 0

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
page = response.text
soup = BeautifulSoup(page,"html.parser")
pricelist = [title.getText().split("+")[0].split("/")[0] for title in soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")]
print(pricelist)
addlist = [title.getText().strip().replace(" |",",") for title in soup.find_all(name="address")]
print(addlist)
linklist = [title['href'] for title in soup.find_all('a', {'class': 'property-card-link'})]
print(linklist)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for i in range(0,len(pricelist)):
    driver.get('https://forms.gle/dJEPJ4ZRk2mCe4i27')

    time.sleep(1)
    driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addlist[i])
    driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(pricelist[i])
    driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(linklist[i])

    driver.find_element(By.XPATH,value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    time.sleep(1)
    
    x +=1
    print(f"Entry{x} done...")