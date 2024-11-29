import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    driver.get('http://localhost:3001/pagina_pedidos/clientes_index')

    contacto_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link' and text()='Contacto']"))
    )
    contacto_link.click()
    time.sleep(3)

    # Sección de contacto 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "contacto"))
    )
    time.sleep(3)

    # Validar que los elementos de contacto estén presentes
    contacto_info = driver.find_element(By.XPATH, "//div[@class='contact-info']")
    contacto_details = driver.find_element(By.XPATH, "//div[@class='contact-details']")
    print("Sección de contacto cargada correctamente.")
    time.sleep(3)

    # Opcional: Validar si el horario, teléfono, o correo están visibles
    horario = contacto_details.find_element(By.XPATH, ".//div[@class='detail-item'][1]//p").text
    telefono = contacto_details.find_element(By.XPATH, ".//div[@class='detail-item'][2]//p").text
    correo = contacto_details.find_element(By.XPATH, ".//div[@class='detail-item'][3]//p").text

    print(f"Horario de atención: {horario}")
    print(f"Teléfono: {telefono}")
    print(f"Correo: {correo}")
    time.sleep(3)

    # Esperar que el iframe de Google Maps se cargue correctamente
    mapa = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src, 'google.com/maps/embed')]"))
    )
    if mapa.is_displayed():
        print("Mapa de Google cargado correctamente.")
    time.sleep(3)
    
finally:
    driver.quit()
    print("Prueba completada y navegador cerrado.")
