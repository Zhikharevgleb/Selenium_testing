import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Укажите путь к вашему драйверу и браузеру
chrome_driver_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chromedriver-win64/chromedriver.exe"  # Путь к ChromeDriver
chrome_binary_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chrome-win64/chrome.exe"  # Путь к браузеру Chrome
# chrome_binary_path = "C:/Users/zhikh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Yandex.lnk"  # Путь к браузеру Chrome

# Настройка опций Chrome
options = Options()
options.binary_location = chrome_binary_path  # Указываем путь к браузеру
options.page_load_strategy = 'eager'  

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://askusers.ru/blog/pravila/testirovanie-form-avtorizatsii/")

# Нажимаем на окно авторизации
buttom = driver.find_element("xpath", "//button[@class = 'button button--only-icon askusers-auth-link']")
buttom.click()
time.sleep(1) 

# Вводим значение в поле логин
login = driver.find_element("xpath", "//span/input[@class='field-text__input' and @placeholder='Логин']")
login.send_keys("7777777")

# Выводим в терминал, то что ввели ранее в поле логин 
print(">>>>>", login.get_attribute("value"), "<<<<<<")
time.sleep(1) 
# Очищаем поле
login.clear()
time.sleep(1) 

# Вводим новое значение в поле логин
login.send_keys("8888888")
# Выводим в терминал
print(">>>>>", login.get_attribute("value"), "<<<<<<")

time.sleep(3)  

# Закрытие браузера
driver.quit()
