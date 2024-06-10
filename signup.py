from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

username = "Taha Ahmed"
email = "test@email.com"
url = "https://secure-retreat-92358.herokuapp.com/"

#Initialize Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Interact with the url
driver.get(url)

# Find Input Boxes
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email_address = driver.find_element(By.NAME, value="email")
submit_button = driver.find_element(By.CLASS_NAME, value="btn")
# Input Data
first_name.send_keys(username.split(" ")[0])
last_name.send_keys(username.split(" ")[1])
email_address.send_keys(email)
submit_button.send_keys(Keys.ENTER)

