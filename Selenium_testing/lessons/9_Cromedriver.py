import time

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
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_argument("--user-agent=smth")# эта хрень меняется user-agent
options.binary_location = chrome_binary_path
options.page_load_strategy = 'eager'  

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

#|=================================================================================================================================|#
#|=================================================================================================================================|#

driver.get("https://n5m.ru/usagent.html")

time.sleep(30)

driver.quit()
