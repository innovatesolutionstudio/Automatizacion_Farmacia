from selenium.webdriver.common.by import By
import time


def verify_contenido_tablero(driver):
    """Interacciona con elementos dentro del iframe 'contenidoFrame'."""
    
    # Cambia al iframe
    time.sleep(4)
    driver.switch_to.frame("contenidoFrame")


    time.sleep(4)
    # ventas mes
    driver.find_element(By.XPATH, "//a[@onclick='verDetallesVentas()']").click()
    actual_1 = driver.find_element(By.XPATH, "//h2[@class='swal2-title']").text 
    if actual_1 == 'Ventas del Mes':
        print("Abrio correctamente la ventana emergente de ventas mes")
    else:
        print("Error")
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@class='swal2-close']").click()

    # clientes del mes
    driver.find_element(By.XPATH, "//a[@onclick='verDetallesClientes()']").click()
    actual_2= driver.find_element(By.XPATH, "class='swal2-title'").text 
    if actual_2 == 'Clientes Registrados en el Mes':
        print("Abrio correctamente la ventana emergente de clientes del mes")
    else:
        print("Error")
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@class='swal2-close']").click()

    # compras del mes
    driver.find_element(By.XPATH, "//a[@onclick='verDetallesCompras()']").click()
    actual_3= driver.find_element(By.XPATH, "//h2[@class='swal2-title']").text 
    if actual_3 == 'Compras del Mes':
        print("Abrio correctamente la ventana emergente de Compras del Mes")
    else:
        print("Error")
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@class='swal2-close']").click()

    # escazes medicamento
    driver.find_element(By.XPATH, "//a[@onclick='verDetallesInventario()']").click()
    actual_4= driver.find_element(By.XPATH, "//h2[@class='swal2-title']").text 
    esperada_4= "Productos con menos de 5 unidades"
    assert esperada_4 in actual_4, f"ERROR, actual {actual_4}, esperado: {esperada_4}"
    if actual_4 == 'Productos con menos de 5 unidades':
        print("Abrio correctamente la ventana emergente de escazes medicamento")
    else:
        print("Error")
    driver.find_element(By.XPATH, "//button[@id='dropdownMenuButton']").click()


    # Recuadro venta mensual
    driver.find_element(By.XPATH, "//a[@onclick='verDetallesVentasG()']").click()
    actual_5= driver.find_element(By.XPATH, "//h2[@class='swal2-title']").text 
    esperada_5= "Ventas de toda la Gestion"
    assert esperada_5 in actual_5, f"ERROR, actual {actual_5}, esperado: {esperada_5}"
    if actual_5 == 'Ventas de toda la Gestion':
        print("Abrio correctamente la ventana emergente de Recuadro venta mensual")
    else:
        print("Error")
    driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()

    # Recuadro productos
    driver.find_element(By.XPATH, "//a[@onclick='verProductosVendidosMes()']").click()
    actual_6= driver.find_element(By.XPATH, "//h2[@class='swal2-title']").text 
    esperada_6= "Total de Productos Vendidos por Mes"
    assert esperada_6 in actual_6, f"ERROR, actual {actual_6}, esperado: {esperada_6}"
    if actual_6 == 'Total de Productos Vendidos por Mes':
        print("Abrio correctamente la ventana emergente de Total de Productos Vendidos por Mes")
    else:
        print("Error")
    driver.find_element(By.XPATH, "//button[@style='display: inline-block;']").click()


    # Recuadro pedidos
    driver.find_element(By.XPATH, "//a[@onclick='verPedidosMensualesAno()']").click()
    
    # Recuadro compras
    driver.find_element(By.XPATH, "//a[@onclick='verProductosCompradosMes()']").click()
    

    

    actual_6= driver.find_element(By.XPATH, "//h2[@class='swal2-title']").text 
    
    time.sleep(4)
    

    # Vuelve al contexto principal
    driver.switch_to.default_content()
