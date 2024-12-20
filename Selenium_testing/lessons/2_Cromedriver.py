import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Укажите путь к вашему драйверу и браузеру
chrome_driver_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chromedriver-win64/chromedriver.exe"  # Путь к ChromeDriver
chrome_binary_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chrome-win64/chrome.exe"  # Путь к браузеру Chrome
# chrome_binary_path = "C:/Users/zhikh/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Yandex.lnk"  # Путь к браузеру Chrome

# Настройка опций Chrome
options = Options()
options.binary_location = chrome_binary_path  # Указываем путь к браузеру

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Открытие страницы Google
driver.get('https://ru.wikipedia.org/')

# Получение текущего url
url = driver.current_url
print("\nURL страницы:", url)

time.sleep(3)

# Получение текущего тайтла страницы
current_title = driver.title
print("\nТекущий заголовок страницы:\n", current_title )

# Сравнение url 
assert url == 'https://ru.wikipedia.org/', "\nОткрыта не та страница"

# Вывод всего кода страницы
print(driver.page_source)

# Закрытие браузера
driver.quit()