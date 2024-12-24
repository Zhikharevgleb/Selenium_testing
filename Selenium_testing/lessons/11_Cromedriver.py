import time
import pickle
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Укажите путь к вашему драйверу и браузеру
chrome_driver_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chromedriver-win64/chromedriver.exe"  # Путь к ChromeDriver
chrome_binary_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Путь к браузеру Chrome

# Настройка опций Chrome
options = Options()
options.add_argument("--window-size=1240, 720") 
options.binary_location = chrome_binary_path
options.page_load_strategy = 'eager'  

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

#|=================================================================================================================================|#
#|=================================================================================================================================|#
BOTTON_0 = ("xpath", "//*[@id='tree-node']/div/button[1]")
BOTTON_1 = ("xpath", "//*[@id='tree-node']/ol/li/ol/li[2]/span/label/span[1]")
# BOTTON_2 = ("xpath", "")

driver.get("https://demoqa.com/checkbox")

# print(driver.get_cookies)

# wait.until(EC.element_to_be_clickable(BOTTON_0)).click()
# time.sleep(1)
# wait.until(EC.element_to_be_clickable(BOTTON_1)).click()
# time.sleep(3)

# # Ensure the cookies directory exists
# cookies_dir = os.path.join(os.getcwd(), "cookies")
# os.makedirs(cookies_dir, exist_ok=True)

# pickle.dump(driver.get_cookies(), open(os.path.join(cookies_dir, "cookies.pkl"), "wb"))

print(driver.get_cookies())
print("____________________________________")

time.sleep(2)

driver.delete_all_cookies() 

time.sleep(2)

print(driver.get_cookies())
print("____________________________________")

driver.add_cookie({"name": "example", "value": "123"})
time.sleep(2)

print(driver.get_cookies())
print("____________________________________")

driver.delete_all_cookies() 

print(driver.get_cookies())
print("____________________________________")

pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

time.sleep(2)

print(driver.get_cookies())
print("____________________________________")

driver.refresh()

print(driver.get_cookies())
print("____________________________________")



time.sleep(2)



driver.quit()
