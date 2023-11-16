from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

# Close single tab
driver.close()

# Close entire browser
driver.quit()