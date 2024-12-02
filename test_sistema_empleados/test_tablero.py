from selenium.webdriver.common.by import By
import time


def verify_contenido_tablero(driver):
    """Interacciona con elementos dentro del iframe 'contenidoFrame'."""
    
    # Cambia al iframe
    time.sleep(4)
    driver.switch_to.frame("contenidoFrame")


    time.sleep(4)
    # Interactúa con el elemento dentro del iframe
    driver.find_element(By.XPATH, "//a[@class='verdetallesventas']").click()
    time.sleep(4)


    # Vuelve al contexto principal
    driver.switch_to.default_content()
