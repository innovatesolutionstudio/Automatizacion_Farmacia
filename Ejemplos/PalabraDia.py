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
driver.get('https://wordledehoy.com/')
 
driver.find_element(By.XPATH, "//span[text() = 'Nuevo']//parent::div[@class = 'article-content']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class = 'reveal-button']").click()
time.sleep(2)
solucion = driver.find_element(By.XPATH, "//p[@class = 'solution-word']").text
 
solucion = solucion.lower()
print(f"LA SOLUCION ES: {solucion}")
 
driver.get('https://lapalabradeldia.com/')
 
time.sleep(5)
for letra in solucion:
    print(f"Escrbiendo la letra {letra}")
    driver.find_element(By.XPATH, f"//button[@aria-label = '{letra}']").click()
    time.sleep(1)
 
driver.find_element(By.XPATH, f"//button[@aria-label = 'procesar palabra']").click()
time.sleep(20)