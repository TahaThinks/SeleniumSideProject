from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

#Interact with the Wikipedia page
# articles_count.click()

#Get hold of the Search Bar
search_bar = driver.find_element(By.NAME, value="search")

#Add text to Search Bar
search_bar.send_keys("Python", Keys.ENTER)

# driver.close()

