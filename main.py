import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.python.org/"

# initialize the web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open the python.org

driver.get(url)
events_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
events_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(events_times)):
    events[n] = {
        "time": events_times[n].text,
        "name": events_names[n].text
    }

print(events)