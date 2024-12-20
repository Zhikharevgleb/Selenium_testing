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
#   'normal' (по умолчанию): ждать, пока свойство document.readyState станет complete.
#   'eager' ждать, пока свойство document.readyState станет interactive, 
#   что означает, что основное содержимое загружено и доступно для взаимодействия.
#   'none' не ждать завершения загрузки страницы.
options.page_load_strategy = 'normal'  

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://askusers.ru/blog/pravila/testirovanie-form-avtorizatsii/")

# возвращает тип элемента
# print('>>>>>>>', type(driver.find_element("id", "splide01-slide06")))

driver.find_element("id", "splide01-slide06").click()

time.sleep(3)  




# Закрытие браузера
driver.quit()