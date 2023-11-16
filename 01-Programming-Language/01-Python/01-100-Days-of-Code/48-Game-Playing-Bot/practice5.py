from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME,value="fName")
fname.send_keys("Tyler")
lname = driver.find_element(By.NAME,value="lName")
lname.send_keys("Ho")
email = driver.find_element(By.NAME,value="email")
email.send_keys("Tylerfakeemail@gmail.com")

button = driver.find_element(By.TAG_NAME,value="button")
button.click()