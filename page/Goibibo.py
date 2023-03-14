import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

goibibo_url ="https://www.goibibo.com/"

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(goibibo_url)

elms = driver.find_elements(By.XPATH, '//span[@class="font13 padL5 black"]')
for i in elms:
    print(i.text)

print(elms)