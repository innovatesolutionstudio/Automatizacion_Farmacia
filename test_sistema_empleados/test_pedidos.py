from selenium.webdriver.common.by import By
import time


def verify_contenido_pedidos(driver):
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE PEDIDOS ++++++++++++++++++++++++++++++++++++++++++++++++++++
 
    #barra de menu click al recursos humanos 

    driver.find_element(By.XPATH, "//a[@href='#pedidos']").click()
    time.sleep(2)
  
    driver.switch_to.frame("contenidoFrame")
    time.sleep(2)
   

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE PEDIDOS - NOTIFICACIONES ++++++++++++++++++++++++++++++++++++++++++++++++++++
 
    driver.find_element(By.XPATH, "//p[text()='Notificaciones']/following-sibling::div//a[@href='/notificaciones_pedidos']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@href='/detallespedido_not/2' and contains(text(), 'Detalles del Pedido')]").click()
    time.sleep(2)

    actualsperado2 =  driver.find_element(By.XPATH, "//div[h2[text()=' Marny Colorado'] and p[text()='Nombre del cliente ']]/h2").text
    time.sleep(2)
    if actualsperado2 =='Marny Colorado':
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de historial de pedidos, verificado con exito")

    else:
        print("\nvista de modulo de historial de pedidos, error ")

 
    driver.find_element(By.XPATH, "//h1[contains(text(), 'Notificaciones')]").click()
    time.sleep(2)
    

    driver.switch_to.default_content()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE PEDIDOS - NOTIFICACIONES ++++++++++++++++++++++++++++++++++++++++++++++++++++
 


    time.sleep(2)
    driver.find_element(By.XPATH, "//span[normalize-space()='Historial de Pedidos']").click()
    time.sleep(4)
    
    
    driver.switch_to.frame("contenidoFrame")
    time.sleep(2)
    
    
    #hacer click en ver detalles 
    driver.find_element(By.XPATH, "//a[@class='btn btndetalles' and @data-id='1']").click()
    time.sleep(2)
    #hacer click en el boton Si ver
    driver.find_element(By.XPATH, "//button[@type='button' and text()='Sí, ver!']").click()
    time.sleep(2)

    actualsperado3 =  driver.find_element(By.XPATH, "//h2[text()=' Adam Baker, Nigel B.']").text


    time.sleep(2)
    if actualsperado3 =='Adam Baker, Nigel B.':
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de historial de pedidos, verificado con exito")

    else:
        print("\nvista de modulo de historial de pedidos, error ")

    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/vista_pedidos']").click()

    # Vuelve al contexto principal
    driver.switch_to.default_content()
    
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='#pedidos']").click()
    time.sleep(2)