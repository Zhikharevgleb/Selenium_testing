import time
import pickle
import os

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
BOTTON_0 = ("xpath", "//input[@type = 'checkbox'][1]")

# driver.get("https://the-internet.herokuapp.com/checkboxes")

# =========== [ПЕРВЫЙ СПОСОБ ПРОВЕРКИ АКТИВИРОВАННОСТИ ЧЕКБОКСА] =========== #
# print(driver.find_element(*BOTTON_0).get_attribute("checked"))
# wait.until(EC.element_to_be_clickable(BOTTON_0)).click() 
# print(driver.find_element(*BOTTON_0).get_attribute("checked")) 
# assert driver.find_element(*BOTTON_0).get_attribute("checked") == "true" # Проверка, что чекбокс был активирован

# =========== [ВТОРОЙ СПОСОБ ПРОВЕРКИ АКТИВИРОВАННОСТИ ЧЕКБОКСА] =========== #
# print(driver.find_element(*BOTTON_0).is_selected()) # Проверка, что чекбокс активирован
# wait.until(EC.element_to_be_clickable(BOTTON_0)).click() 
# print(driver.find_element(*BOTTON_0).is_selected())  # Проверка, что чекбокс активирован

# =========== [ОБРАБОТКА СЛУЧАЕВ, КОГДА INPUT ЧЕМ-ТО ПЕРЕКРЫВАЕТСЯ] =========== #
# CHECKBOX_HOME_STATUS = ("xpath", "//input[@id='tree-node-home']") # ОДИН ЭЛЕМЕНТ ДЛЯ СТАТУСА
# CHECKBOX_HOME_ACTION = ("xpath", "//span[@class ='rct-checkbox']") # ОДИН ЭЛЕМЕНТ ДЛЯ НАЖАТИЯ

# driver.get("https://demoqa.com/checkbox")

# driver.find_element(*CHECKBOX_HOME_ACTION).click()
# print(driver.find_element(*CHECKBOX_HOME_STATUS).is_selected())

# =========== [ОБРАБОТКА СЛУЧАЕВ, КОГДА RADIO BUTTON ЧЕМ-ТО ПЕРЕКРЫВАЕТСЯ] =========== #
driver.get("https://demoqa.com/radio-button")

YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
YES_RADIO_ACTION = ("xpath", "//label[@for='yesRadio']")
NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")
NO_RADIO_ACTION = ("xpath", "//label[@for='noRadio']")

driver.find_element(*YES_RADIO_ACTION).click()
print(driver.find_element(*YES_RADIO_STATUS).is_selected()) # Проверка, что чек
time.sleep(3)
driver.find_element(*NO_RADIO_ACTION).click()
print(driver.find_element(*NO_RADIO_STATUS).is_selected()) # Проверка, что чек
time.sleep(3)
driver.find_element(*NO_RADIO_ACTION).click()
print(driver.find_element(*NO_RADIO_STATUS).is_enabled())

time.sleep(3)

driver.quit()
