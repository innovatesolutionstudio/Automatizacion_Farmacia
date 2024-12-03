from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

def verify_vista_ventas(driver):


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE VENTAS++++++++++++++++++++++++++++++++++++++++++++++++++++
    
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='#ventas']").click()
    
    # Cambia al iframe
    time.sleep(4)
    driver.switch_to.frame("contenidoFrame")

    esperado = driver.find_element(By.XPATH, "//span[text()='Nueva Venta']").text

    if(esperado=='ventas'):
        print("vista de modulo de compras, verificado con exito")
    else:
        print("vista de modulo de compras, Error en la verificacion")

    time.sleep(4)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE VENTAS - NUEVA COMPRA++++++++++++++++++++++++++++++++++++++++++++++++++++
 


def verify_registro_ventas(driver):

    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='#ventas']").click()
    
    time.sleep(4)
    driver.switch_to.frame("contenidoFrame")

    driver.find_element(By.XPATH, "//a[@href='/nueva_venta'][1]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//input[@id='carnet']").send_keys("123456")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='nit']").send_keys("987654")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='apellido']").send_keys("Perez")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("Juan")
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='productoFiltro']").send_keys("Tramadol")
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[contains(text(), 'Tramadol')]").click()
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//input[@id='cantidad']").send_keys("1")
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//button[@id='agregarProducto']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//a[contains(@onclick, 'confirmarVenta()')]").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()
    time.sleep(1)
    
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sí, proceder')]").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(2)

    ventana_original = driver.current_window_handle
    time.sleep(2)

    # Buscar la nueva ventana
    nueva_ventana = None
    for handle in driver.window_handles:
        if handle != ventana_original:
            nueva_ventana = handle
            driver.switch_to.window(nueva_ventana)
            break

    if nueva_ventana:
        driver.close()
        print("Cerrando la ventana de la factura.")
        
        driver.switch_to.window(ventana_original)

    driver.find_element(By.XPATH, "//a[@href='#ventas']").click()
    time.sleep(3)
    driver.switch_to.frame("contenidoFrame")


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - HISTORIAL DE VENTAS++++++++++++++++++++++++++++++++++++++++++++++++++++
   
    driver.find_element(By.XPATH, "//a[@href='/ventas'][1]").click()
    time.sleep(3)

    campo_fecha_inicio = driver.find_element(By.XPATH, "//input[@id='fechaInicio']")
    campo_fecha_inicio.send_keys("02/05/2024")  
    campo_fecha_inicio.send_keys(Keys.TAB)  
    time.sleep(3)
    
    campo_fecha_inicio.send_keys("12:23")  
    time.sleep(3)

    campo_fecha_inicio = driver.find_element(By.XPATH, "//input[@id='fechaFin']")
    campo_fecha_inicio.send_keys("02/12/2024")
    campo_fecha_inicio.send_keys(Keys.TAB)
    time.sleep(3)

    campo_fecha_inicio.send_keys("12:23")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[@id='btnFiltrar']").click()
    time.sleep(10)

    driver.find_element(By.XPATH, "//button[@id='btnLimpiar']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "//select[@name='tablaVentas_length']/option[@value='25']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@type='search' and @aria-controls='tablaVentas']").send_keys("72251")
    time.sleep(3)  
    
    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]//option[@value='copiar']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]//option[@value='detalle']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "//a[@href='/ventas'][1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//a[@href='/vista_ventas']").click()
    time.sleep(3)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - INVENTARIO++++++++++++++++++++++++++++++++++++++++++++++++++++
  
    driver.find_element(By.XPATH, "//a[@href='/inventario_vista']").click()
    time.sleep(3)


    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]/option[@value='copiar']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//input[@type='search' and @aria-controls='tablaInventario']").send_keys("1111")
    time.sleep(3)   
    
    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "(//select[@class='form-select acciones-select'])[1]//option[@value='detalles']").click()
    time.sleep(3)


    driver.find_element(By.XPATH, "//a[@href='/inventario_vista']").click()
    time.sleep(3)

    driver.find_element(By.XPATH, "//select[@name='tablaInventario_length']/option[@value='25']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, "//a[@href='/vista_ventas']").click()
    time.sleep(3)

    driver.switch_to.default_content()
