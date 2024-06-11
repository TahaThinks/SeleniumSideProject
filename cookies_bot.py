from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://orteil.dashnet.org/cookieclicker/"

#Initialize Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Interact with the url
driver.get(url)

#Enter the Game
time.sleep(20)
while True:
    cookie = driver.find_element(By.ID, value="bigCookie")
    cookie.send_keys(Keys.ENTER)

