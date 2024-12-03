from selenium.webdriver.common.by import By
import time
 
def verify_sistema_cliente_inicio(driver):
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ SISTEMA CLIENTES - INICIO ++++++++++++++++++++++++++++++++++++++++++++++++++++

    titulo = driver.find_element(By.XPATH, "//h1[@class='welcome-title']").text
    time.sleep(4)
    if (titulo == '¡Bienvenido a nuestra farmacia en línea!'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nPagina de inicio de clientes, vista con exito")
    else:
        print("\nPagina de inicio de clientes, vista erronea")
    time.sleep(4)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ SISTEMA CLIENTES - CONTACTOS ++++++++++++++++++++++++++++++++++++++++++++++++++++

    driver.get('http://localhost:3001/pagina_pedidos/otros/contactanosP')
    titulo2 = driver.find_element(By.XPATH, "//h2[text()='Contacto']").text
    time.sleep(4)
    if (titulo2 == 'Contacto'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nPagina de contactos de clientes, vista con exito")
    else:
        print("\nPagina de contactos de clientes, vista erronea")
    time.sleep(4)