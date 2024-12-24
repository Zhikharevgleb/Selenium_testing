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

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

REMOVE_BUTTOM = ("xpath", "//button[text() = 'Remove']")
ENABLE_BUTTOM = ("xpath", "//button[text() = 'Enable']")
TEXT_FIELD = ("xpath", "//input[@type = 'text']")

driver.find_element(*REMOVE_BUTTOM).click()

wait.until(EC.invisibility_of_element_located(REMOVE_BUTTOM))

print("GOOD BOY")

# driver.find_element(*ENABLE_BUTTOM).click()
wait.until(EC.element_to_be_clickable(ENABLE_BUTTOM)).click()
wait.until(EC.element_to_be_clickable(TEXT_FIELD)).send_keys("Hello, world")
wait.until(EC.text_to_be_present_in_element_value(TEXT_FIELD, "Hello, world"))

print("GOOD BOY")

driver.quit()
