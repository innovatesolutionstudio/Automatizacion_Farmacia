"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la libreria necesaria

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


# Configuración automática del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir url en el navegador
driver.get('https://www.multicine.com.bo/register')
time.sleep(5)

driver.find_element(By.XPATH, "//div[@class = 'alert-radio-label sc-ion-alert-md']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='Aceptar']").click()
time.sleep(1)

driver.get('https://www.multicine.com.bo/register')
time.sleep(1)

# Acciones para interactuar con el navegador
driver.find_element(By.XPATH, "//input[@class= 'native-input sc-ion-input-md']").send_keys("Juan")
time.sleep(1)
driver.find_element(By.XPATH, "//ion-input[@name= 'lastname']//input").send_keys("Perez")
time.sleep(1)
driver.find_element(By.XPATH, "//ion-input[@name= 'phone']//input").send_keys("77885562")
time.sleep(1)
driver.find_element(By.XPATH, "//ion-input[@name= 'address']//input").send_keys("je@gmail.com")
time.sleep(1)
driver.find_element(By.XPATH, "//ion-select[@name='mySelect']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@class='alert-radio-label sc-ion-alert-md']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='alert-button ion-focusable ion-activatable sc-ion-alert-md']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//ion-input[@name= 'docextend']//input").send_keys("La razon nose ")
time.sleep(1)
driver.find_element(By.XPATH, "//ion-input[@name= 'docid']//input").send_keys("12316546548798765626")
time.sleep(1)

driver.quit()

print("Prueba visual completada")
