import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Укажите путь к вашему драйверу и браузеру
chrome_driver_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chromedriver-win64/chromedriver.exe"  # Путь к ChromeDriver
chrome_binary_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chrome-win64/chrome.exe"  # Путь к браузеру Chrome

# Настройка опций Chrome
options = Options()
options.add_argument("--window-size=1240,720") 
prefs = {
    "download.default_directory": "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/Selenium_testing/lessons/downloads"  # Полный путь
}
options.add_experimental_option("prefs", prefs)
options.binary_location = chrome_binary_path    
options.page_load_strategy = 'eager'  

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com/download")

# # Нажимаем на окно авторизации
download_buttom = driver.find_element("xpath", "//a[@href = 'download/sm.jpg']")
download_buttom.click()

time.sleep(3)  

# # Закрытие браузера
driver.quit()
