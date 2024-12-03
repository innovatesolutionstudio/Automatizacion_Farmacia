from selenium.webdriver.common.by import By
import time


def verify_contenido_ventascarrito(driver):
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ SISTEMA CLIENTES - CONTACTOS ++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    driver.get('http://localhost:3001/pagina_pedidos/productos/1')
    time.sleep(2)
    #hacer click en la tineda 
    driver.find_element(By.XPATH, "//a[text()='Tienda']").click()
    time.sleep(4)

    actualsperado4 =  driver.find_element(By.XPATH, "//h3[@class='product-name' and text()='Tramadol']").text
    time.sleep(2)
    if actualsperado4 =='Tramadol':
        print("Texto correcto")
    else:
        print("Error 404")

    #hacer click en el boton de añadir un producto 
    driver.find_element(By.XPATH, "//h3[text()='Tramadol']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)
    #hacer click en el boton de añadir un producto 
    driver.find_element(By.XPATH, "//h3[text()='Tramadol']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)
    #hacer click en el boton de añadir un producto 
    driver.find_element(By.XPATH, "//h3[text()='Tramadol']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)
    #hacer click en el boton de añadir un producto 
    driver.find_element(By.XPATH, "//h3[text()='Tramadol']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)

    actualsperado5 =  driver.find_element(By.XPATH, "//h3[@class='product-name' and text()='Atropina']").text
    time.sleep(2)
    if actualsperado5 =='Atropina':
        print("Texto correcto")
    else:
        print("Error 404")

    #hacer click en el boton de añadir segundo producto 
    driver.find_element(By.XPATH, "//h3[text()='Atropina']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)
    #hacer click en el boton de añadir segundo producto 
    driver.find_element(By.XPATH, "//h3[text()='Atropina']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)
    #hacer click en el boton de añadir segundo producto 
    driver.find_element(By.XPATH, "//h3[text()='Atropina']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)
    #hacer click en el boton de añadir segundo producto 
    driver.find_element(By.XPATH, "//h3[text()='Atropina']/ancestor::div[contains(@class, 'product-card')]//button[@class='add-to-cart']").click()
    time.sleep(4)
    #hacer click en el boton de carrito
    driver.find_element(By.XPATH, "//a[@class='cart-icon']//i[@class='fas fa-shopping-cart']").click()
    time.sleep(4)
    #hacer click en confirmar el pedido
    driver.find_element(By.XPATH, "//button[@class='btn-checkout' and contains(text(), 'Continuar')]").click()
    time.sleep(4)

    #hacer click en aumentar cantidad
    driver.find_element(By.XPATH, "//button[@onclick='updateQuantity(0, 1)']").click()
    time.sleep(4)
    #hacer click en aumentar cantidad
    driver.find_element(By.XPATH, "//button[@onclick='updateQuantity(0, 1)']").click()
    time.sleep(4)
    #hacer click en disminuir cantidad
    driver.find_element(By.XPATH, "//button[@onclick='updateQuantity(1, -1)']").click()
    time.sleep(4)
    #hacer click en disminuir cantidad
    driver.find_element(By.XPATH, "//button[@onclick='updateQuantity(1, -1)']").click()
    time.sleep(4)
    #hacer click en el boton contimuar con el pedido
    driver.find_element(By.XPATH, "//button[@onclick='finalizarCompra()']").click()
    time.sleep(4)

    #ingresar nombre 
    driver.find_element(By.XPATH, "//input[@type='text' and @name='nombre']").send_keys("kevin")
    time.sleep(4)
    #ingresar apellido 
    driver.find_element(By.XPATH, "//input[@type='text' and @name='apellido']").send_keys("Quispe")
    time.sleep(4)
    #ingresar nit 
    driver.find_element(By.XPATH, "//input[@type='text' and @name='ci_nit']").send_keys("7058675")
    time.sleep(4)
    #ingresar direccion 
    driver.find_element(By.XPATH, "//input[@type='text' and @name='direccion']").send_keys("Calle santa clara zona elizardo perez")
    time.sleep(4)
    #ingresar celular 
    driver.find_element(By.XPATH, "//input[@type='text' and @name='telefono']").send_keys("69917223")
    time.sleep(4)
    #ingresar nota 
    driver.find_element(By.XPATH, "//textarea[@placeholder='Dejar en la recepción del edificio, tercer piso.']").send_keys("dejar en el segundo piso departamento B")
    time.sleep(4)

    #hacer click en el boton confirmar pedido
    driver.find_element(By.XPATH, "//button[text()='Confirmar Pedido']").click()
    time.sleep(4)

    ventana_original = driver.current_window_handle
    #hacer click en el boton si confirmar 
    driver.find_element(By.XPATH, "//button[text()='Sí, confirmar']").click()
    time.sleep(4)


    nueva_ventana = None
    for handle in driver.window_handles:
        if handle != ventana_original:
            nueva_ventana = handle
            driver.switch_to.window(nueva_ventana)
            break

    if nueva_ventana:
        driver.close()
        print("Cerrando la nueva pestaña/ventana.")

    driver.switch_to.window(ventana_original)
    time.sleep(4)
    #hacer click en el boton ok
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(4)

    print("/////////////////////////////////////////////////////////////////////////////////////////////")
    print("SIGUIENTE MODULO")
    print("/////////////////////////////////////////////////////////////////////////////////////////////")
