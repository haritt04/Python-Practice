from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.youtube.com/")

input_box = driver.find_element(By.NAME, "search_query")
input_box.send_keys("The aura farming kid")
input_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 30)
video_link = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "The Aura Farming Kid")))
video_link.click()
fullscreen_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-keyshortcuts='f']")))
fullscreen_btn.click()
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "video-stream html5-main-video")))

time.sleep(30)  