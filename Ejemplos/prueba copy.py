import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import easyocr

# Configuración del WebDriver usando Service
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Maximizar la ventana y abrir la URL
driver.maximize_window()
driver.get('https://enlace.univalle.edu/san/webform/PAutenticar.aspx')

# Completa el formulario
driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbCuenta']").send_keys("jpj2026628")
time.sleep(1)
time.sleep(1)
driver.get('https://enlace.univalle.edu/san/WebForm/PCaptcha.aspx')

time.sleep(1)

time.sleep(6)
# Cierra el navegador
driver.quit()
