import time
from selenium import webdriver #импорт селениума
from selenium.webdriver.chrome.service import Service #класс отвечащий за установку, открытие и заркытие драйвера
from selenium.webdriver.chrome.options import Options

# Укажите путь к вашему драйверу и браузеру
chrome_driver_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chromedriver-win64/chromedriver.exe"  # Путь к ChromeDriver
chrome_binary_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chrome-win64/chrome.exe"  # Путь к браузеру Chrome

# Настройка опций Chrome
options = Options()
options.binary_location = chrome_binary_path  # Указываем путь к браузеру

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Открытие страницы Google
driver.get('https://www.ya.ru/')

time.sleep(10)

driver.back()

time.sleep(3)

driver.forward()

time.sleep(3)

driver.refresh()

time.sleep(3)


# Закрытие браузера
driver.quit()