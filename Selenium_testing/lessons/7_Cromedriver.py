import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Укажите путь к вашему драйверу и браузеру
chrome_driver_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chromedriver-win64/chromedriver.exe"  # Путь к ChromeDriver
chrome_binary_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/chrome-win64/chrome.exe"  # Путь к браузеру Chrome

# Настройка опций Chrome
options = Options()
options.add_argument("--incognito")
options.add_argument("--window-size=1240,720")
options.binary_location = chrome_binary_path  # Указываем путь к браузеру
options.page_load_strategy = 'eager'

# Настройка пути загрузки файлов
download_path = "C:/Users/zhikh/Desktop/Программинг/Для портфолио QA/Selenium_testing/lessons/downloads"
prefs = {
    "download.default_directory": download_path,  # Указываем папку для загрузок
    "download.prompt_for_download": False,         # Не запрашивать подтверждение на скачивание
    "download.directory_upgrade": True,            # Разрешить обновление директории
    "safebrowsing.enabled": True,                  # Включить безопасный просмотр
    "profile.default_content_settings.popups": 1x, # Отключить всплывающие окна
}
options.add_experimental_option("prefs", prefs)

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Переход на страницу с файлами для загрузки
driver.get("https://the-internet.herokuapp.com/download")
time.sleep(6)  

# Нахождение кнопки для скачивания файла
download_button = driver.find_element(By.XPATH, "//a[@href='download/download.jpg']")
download_button.click()  # Кликаем для скачивания

time.sleep(5)  # Ждем завершения загрузки

# Закрытие браузера
driver.quit()
