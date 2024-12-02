from selenium.webdriver.common.by import By
import time


def verify_vista_compras(driver):

    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='#compras']").click()
    
    """Interacciona con elementos dentro del iframe 'contenidoFrame'."""
    
    # Cambia al iframe
    time.sleep(4)
    driver.switch_to.frame("contenidoFrame")
    esperado = driver.find_element(By.XPATH, "//h1[text()='Compras'][1]").text
    if(esperado=='Compras'):
        print("vista de modulo de compras, verificado con exito")
    else:
        print("vista de modulo de compras, Error en la verificacion")

    time.sleep(4)

    driver.find_element(By.XPATH, "//a[@href='/nueva_compra'][1]").click()
    
    time.sleep(4)

    # Vuelve al contexto principal
    driver.switch_to.default_content()
