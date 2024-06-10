from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://en.wikipedia.org/wiki/Main_Page"

#Initialize Webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Navigate to Wikipedia
driver.get(url)

#Get Article Count
articles_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(articles_count.text)

driver.close()

