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
options.binary_location = chrome_binary_path
options.page_load_strategy = 'eager'  

# Инициализация сервиса и драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15, poll_frequency=1)

#|=================================================================================================================================|#
#|=================================================================================================================================|#
BOTTON = ("xpath", "//button[@id='alertButton']")
BOTTON_2 = ("xpath", "//button[@id='confirmButton']")
BOTTON_3 = ("xpath", "//button[@id='promtButton']")

driver.get("https://demoqa.com/alerts")

# time.sleep(3)

# _____________________________________________________#
wait.until(EC.element_to_be_clickable(BOTTON)).click()
alert = wait.until(EC.alert_is_present()) # условие появления алерта
driver.switch_to.alert # переключение на алерт
# time.sleep(3)
alert.accept()
# time.sleep(3)

# _____________________________________________________#
wait.until(EC.element_to_be_clickable(BOTTON_2)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert
print(alert.text)
# time.sleep(3)
alert.dismiss()
# time.sleep(3)

# _____________________________________________________#
wait.until(EC.element_to_be_clickable(BOTTON_3)).click()
alert = wait.until(EC.alert_is_present())
# time.sleep(3)
driver.switch_to.alert
alert.send_keys("Hello, world!")
# time.sleep(3)
alert.accept()
time.sleep(3)
 
driver.quit()
