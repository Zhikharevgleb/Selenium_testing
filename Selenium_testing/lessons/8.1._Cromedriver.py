from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


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
driver.implicitly_wait(10) # <<<<< ЭТО ПРИМЕР ИСПОЛЬЗОВАНИЯ НЕЯВНЫХ ОЖИДАНИЙ (ЗАДАЕТСЯ ГЛОБАЛЬНО)

#|=================================================================================================================================|#
#|=================================================================================================================================|#

driver.get("https://demoqa.com/dynamic-properties")

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id = 'visibleAfter']")

buttom = driver.find_element(*VISIBLE_AFTER_BUTTON)
buttom.click()

print("GOOD BOY")

driver.quit()
