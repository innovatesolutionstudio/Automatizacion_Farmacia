from selenium.webdriver.common.by import By
import time


from selenium.webdriver.common.keys import Keys

def verify_modulo_finanzas(driver):
    ventana_original = driver.current_window_handle
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE FINANZAS++++++++++++++++++++++++++++++++++++++++++++++++++++
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@href='#finanzas']").click()
    
    time.sleep(4)
    driver.switch_to.frame("contenidoFrame")


    vista_finanzas = driver.find_element(By.XPATH, "//h1[text()='Finanzas']").text

    if(vista_finanzas=='Finanzas'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de Finanzas, verificado con exito")
    else:
        print("vista de modulo de Finanzas, Error en la verificacion")
    time.sleep(2)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - ADMINISTRAR CAJAS++++++++++++++++++++++++++++++++++++++++++++++++++++

    
    driver.find_element(By.XPATH, "//a[@href='/cajas'][1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='cerrarCajasBtn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Sí, cerrar cajas']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='abrirCajasBtn']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Sí, abrir cajas']").click()
    time.sleep(2)
    
    vista_administrar_cajas = driver.find_element(By.XPATH, "//h1[text()='Cajas']").text

    if(vista_administrar_cajas=='Cajas'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de adm. Cajas, verificado con exito")
    else:
        print("vista de modulo de adm. Cajas, Error en la verificacion")
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@href='/vista_Finanzas']").click()
    time.sleep(2)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - ADMINISTRAR CAJAS++++++++++++++++++++++++++++++++++++++++++++++++++++

    driver.find_element(By.XPATH, "//a[@href='/vista_ganancias'][1]").click()
    time.sleep(30)
    driver.find_element(By.XPATH, "//a[@onclick='verGrafico()']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//select[@id='ventasSelect']//option[@value='429037980']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[text()='×']").click()

    vista_ganancias = driver.find_element(By.XPATH, "//h1[text()='Ganancias']").text

    if(vista_ganancias=='Ganancias'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de Ganancias, verificado con exito")
    else:
        print("vista de modulo de Ganancias, Error en la verificacion")
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@href='/vista_Finanzas']").click()
    time.sleep(2)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ MODULO DE COMPRAS - REPORTES ++++++++++++++++++++++++++++++++++++++++++++++++++++
    driver.find_element(By.XPATH, "//a[@href='/vista_reportes'][1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@href='/reporte_productos'][1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//select[@id='anio']//option[@value = '2023']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//select[@id='mes']//option[@value = '4']").click()
    time.sleep(2)

    ventana_original = driver.current_window_handle

    driver.find_element(By.XPATH, "//a[@id='saveChartBtn']").click()
    time.sleep(5)

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
    time.sleep(2)
    driver.switch_to.frame("contenidoFrame")
    vista_reportes_Productos = driver.find_element(By.XPATH, "//h1[text()='Productos']").text

    if(vista_reportes_Productos=='Productos'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nvista de modulo de reportes de Productos, verificado con exito")
    else:
        print("vista de modulo de reportes de Productos, Error en la verificacion")
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@href='/vista_Finanzas']").click()
    time.sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, "//a[@href='#finanzas']").click()