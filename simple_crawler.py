from selenium import webdriver
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Driver setup
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# Change the URL to a desired URL.
driver.get('https://CHANGE-ME.com')
print (driver.title)

#Main logic

wait = WebDriverWait(driver, 2)
while True:
        main = driver.find_elements(By.CSS_SELECTOR, "<CSS.ID>")  #Change the CSS id to a desired selector.
        time.sleep(2)
        for m in main:
            print(m.text, file=open("output.txt", "a")) #Generates a text file containing the output of the crawled website.
        try:
                element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '<CSS.ID>'))) #Change the CSS id to a desired selector.
                element.click()
        except TimeoutException:
                break

driver.quit()
