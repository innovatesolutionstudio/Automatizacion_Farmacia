from selenium.webdriver.common.by import By
import time


from selenium.webdriver.common.keys import Keys

def verify_modulo_compras(driver):


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS++++++++++++++++++++++++++++++++++++++++++++++++++++


    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='#compras']").click()
    
    # Cambia al iframe
    time.sleep(4)
    driver.switch_to.frame("contenidoFrame")


    esperado = driver.find_element(By.XPATH, "//h1[text()='Compras'][1]").text

    if(esperado=='Compras'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de compras, verificado con exito")
    else:
        print("vista de modulo de compras, Error en la verificacion")

    time.sleep(4)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - NUEVA COMPRA++++++++++++++++++++++++++++++++++++++++++++++++++++
 
    driver.find_element(By.XPATH, "//a[@href='/nueva_compra'][1]").click()
    time.sleep(2)

    esperado_nueva_compra = driver.find_element(By.XPATH, "//h1[text()='Nueva Compra'][1]").text

    if(esperado_nueva_compra=='Nueva Compra'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de nueva compra, verificado con exito")
    else:
        print("\nvista de modulo de nueva compra, Error en la verificacion")

    driver.find_element(By.XPATH, "//select[@id = 'ID_Proveedor']//option[@value='1']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id = 'productoFiltro']").send_keys("paracetamol")
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[text()= 'PARACETAMOL - Comprimidos']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//select[@id = 'unidad_empaque']//option[@value='1']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id = 'cantidadEmpaque']").send_keys("2")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id = 'cantidadUnitario']").send_keys("5")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id = 'precio']").send_keys("15")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id = 'fecha_vencimiento']").send_keys("12/09/2025")
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id = 'agregarProducto']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@onclick='confirmarCompra()']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Sí, registrar']").click()
    time.sleep(1)   
    nueva_compra_respuesta = driver.find_element(By.XPATH, "//h2[text()='Compra registrada']").text
    time.sleep(1)

    if(nueva_compra_respuesta=='Compra registrada'):
        
        print("\nCompra registrada correctamente")
    else:
        print("Error al registrar la compra")

    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/vista_compras']").click()
    time.sleep(2)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - HISTORIAL DE COMPRAS++++++++++++++++++++++++++++++++++++++++++++++++++++
        

    driver.find_element(By.XPATH, "//a[@href='/compras'][1]").click()
    time.sleep(2)

    vista_compra = driver.find_element(By.XPATH, "//h1[text()='Historial de Compras']").text
    time.sleep(1)

    if(vista_compra =='Historial de Compras'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nHistorial de compras vista completada")
    else:
        print("\nError de compras vista completada")


    campo_fecha_inicio = driver.find_element(By.XPATH, "//input[@id='fechaInicio']")
    campo_fecha_inicio.send_keys("02/12/2024")  
    campo_fecha_inicio.send_keys(Keys.TAB)  
    time.sleep(1)
    campo_fecha_inicio.send_keys("12:23")  
    time.sleep(2)
    campo_fecha_inicio = driver.find_element(By.XPATH, "//input[@id='fechaFin']")
    campo_fecha_inicio.send_keys("02/12/2024")
    campo_fecha_inicio.send_keys(Keys.TAB)
    time.sleep(1)
    campo_fecha_inicio.send_keys("12:23")
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[@id='btnFiltrar']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[@id='btnLimpiar']").click()
    time.sleep(4)
    driver.find_element(By.XPATH, "//a[@href='/vista_compras']").click()
    time.sleep(2)
    
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - PROVEEDORES++++++++++++++++++++++++++++++++++++++++++++++++++++
  
    driver.find_element(By.XPATH, "//a[@href='/proveedores'][1]").click()
    time.sleep(2)
    
    vista_proveedores = driver.find_element(By.XPATH, "//h1[text()='Registro de Proveedores']").text
    time.sleep(1)

    if(vista_proveedores =='Registro de Proveedores'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nHistorial de proveedores vista completada")
    else:
        print("\nError de proveedores vista completada")

    driver.find_element(By.XPATH, "//tr[td[text() = 'Farmacorp']]//a[@class='btndetalles']").click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//button[text()='Sí, ver!']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/proveedores'][1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/vista_compras']").click()
    time.sleep(4)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - PRODUCTOS++++++++++++++++++++++++++++++++++++++++++++++++++++
  

    driver.find_element(By.XPATH, "//a[@href='/productos'][1]").click()
    time.sleep(4)

    vista_productos = driver.find_element(By.XPATH, "//h1[text()='Gestión de Productos']").text
    time.sleep(1)

    if(vista_productos =='Gestión de Productos'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nHistorial de productos vista completada")
    else:
        print("\nError de productos vista completada")

    driver.find_element(By.XPATH, "//tr[td[text() = 'METAMIZOL SÓDICO']]//a[@class='btndetalles']").click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, "//button[text()='Sí, ver!']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/productos'][1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/vista_compras']").click()
    time.sleep(2)

    driver.switch_to.default_content()
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[@href='#compras']").click()
    time.sleep(2)