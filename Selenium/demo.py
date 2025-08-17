from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC    
import time
# from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://clickcounter.io/")

plus_id = "btnPlus1"
num_clicks_id = "counterResult1"
substract_id = "btnSubstract1"


WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, plus_id)))
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, substract_id)))

plus_btn = driver.find_element(By.ID, plus_id)
# 
while True:
    plus_btn.click()
    time.sleep(0.3)
    num_count = driver.find_element(By.ID, num_clicks_id).text
    print(f"click count: {num_count}")
    # num_count = int(num_count.replace(",", "").split()[0])

    if int(num_count) == 30:
        print("Reached 30 clicks, rolling back to 0...")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, substract_id)))
        subtract_btn = driver.find_element(By.ID, substract_id)
        time.sleep(1)
        while True:
            subtract_btn.click()
            time.sleep(0.3)
            num_count = driver.find_element(By.ID, num_clicks_id).text
            print(f"click count after rollback: {num_count}")
            if int(num_count) == 0:
                print("Successfully rolled back to 0 clicks.")
                break
        break
time.sleep(2)