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
driver.get('https://enlace.univalle.edu/san/webform/pautenticar.aspx')

# Acciones para interactuar con el navegador
driver.find_element(By.XPATH, "//input[@id= 'ContentPlaceHolder1_cuAutenticar_txtCuenta']").send_keys("QAE2026498")
time.sleep(2)


#Selecionar dia especifico
driver.find_element(By.XPATH, "//img[@id= 'btn1']").click()
time.sleep(1)
#Selecionar dia especifico
driver.find_element(By.XPATH, "//img[@id= 'btn6']").click()
time.sleep(1)
#Selecionar dia especifico
driver.find_element(By.XPATH, "//img[@id= 'btn3']").click()
time.sleep(1)
#Selecionar dia especifico
driver.find_element(By.XPATH, "//img[@id= 'btn0']").click()
time.sleep(1)
#Selecionar dia especifico
driver.find_element(By.XPATH, "//img[@id= 'btn5']").click()
time.sleep(1)
#Selecionar dia especifico
driver.find_element(By.XPATH, "//img[@id= 'btn9']").click()
time.sleep(1)

#Acciones para selecionar Dia
driver.find_element(By.XPATH, "//td[@id = 'ContentPlaceHolder1_cuAutenticar_TableCell7']").click()
time.sleep(1)
#Selecionar dia especifico
driver.find_element(By.XPATH, "//td[@id = 'ContentPlaceHolder1_cuAutenticar_TableCell7']//option[text()='ESTUDIANTE']").click()
time.sleep(3)

#Click en boton Enviar Consulta
driver.find_element(By.XPATH, "//input[@id= 'ContentPlaceHolder1_cuAutenticar_btnInicioSession']").click()

time.sleep(5)
#Click en boton de Cerrar Sesion
driver.find_element(By.XPATH, "//a[@id = 'LKBCerrarSesion']").click()



driver.quit()

print("Prueba visual completada")
