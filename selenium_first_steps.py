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
driver.get('https://yoparticipo.oep.org.bo/')

# Acciones para interactuar con el navegador
driver.find_element(By.XPATH, "//input[@id= 'valDoc']").send_keys("1234567")

#Acciones para selecionar Dia
driver.find_element(By.XPATH, "//select[@id = 'valDay']").click()
#Selecionar dia especifico
driver.find_element(By.XPATH, "//select[@id = 'valDay']//option[text()='2']").click()

#Acciones para selecionar Mes
driver.find_element(By.XPATH, "//select[@id = 'valMonth']").click()
#Selecionar dia especifico
driver.find_element(By.XPATH, "//select[@id = 'valMonth']//option[text()='Enero']").click()

#Acciones para selecionar Año
driver.find_element(By.XPATH, "//select[@id = 'valYear']").click()
#Selecionar dia especifico
driver.find_element(By.XPATH, "//select[@id = 'valYear']//option[text()='2003']").click()



#Click en boton Enviar Consulta
driver.find_element(By.XPATH, "//button[text() = 'Consultar']").click()

driver.quit()

print("Prueba visual completada")
