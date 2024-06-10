from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://en.wikipedia.org/wiki/Main_Page"

#Initialize Webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Open Webpage
driver.get(url)

