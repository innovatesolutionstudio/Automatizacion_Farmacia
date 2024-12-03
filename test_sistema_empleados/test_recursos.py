from selenium.webdriver.common.by import By
import time


def verify_contenido_recursos(driver):
    driver.find_element(By.XPATH, "//a[i[@class='fa fa-user']]").click()
    time.sleep(4)






    """Interacciona con elementos dentro del iframe 'contenidoFrame'."""
    # Cambia al iframe donde quieres cargar la página
    driver.switch_to.frame("contenidoFrame")

    # Espera algunos segundos para asegurarte de que la página se haya cargado
    time.sleep(4)

    
    #hacer click en ver detalle 
    driver.find_element(By.XPATH, "//tr[td[text()='1']]//a[@class='btndetalles']").click()
    time.sleep(4)
    #hacer click en Si ver  
    driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()
    time.sleep(4)
    actualsperado1 =  driver.find_element(By.XPATH, "//div[@class='data-group']/p[strong[text()='Masculino']]").text
    time.sleep(2)
    if actualsperado1 =='Masculino':
        print("texto correcto")
    else:
        print("Error 404")

    #hacer click en el boton de ver contraseña 
    driver.find_element(By.XPATH, "//i[@id='show_password']").click()
    time.sleep(4)
    

    #hacer click en el boton Editar 
    driver.find_element(By.XPATH, "//a[@href='/EditEmpleados/1']").click()
    time.sleep(4)
    #ingresar datos en la casilla de nombre 
    driver.find_element(By.XPATH, "//input[@id='nombre']").send_keys("Pedro")
    time.sleep(4)
    #hacer click en el boton seleccionar caja 
    driver.find_element(By.XPATH, "//select[@id='caja']").click()
    time.sleep(4)
    #hacer click en el boton seleccionar caja seleccionando la caja 
    driver.find_element(By.XPATH, "//option[text()='CS-223-24']").click()
    time.sleep(4)
    #hacer click en el boton guardar
    driver.find_element(By.XPATH, "//button[@id='submitButton']").click()
    time.sleep(4)
    print("/////////////////////////////////////////////////////////////////////////////////////////////")
    print("SIGUIENTE MODULO")


    # Vuelve al contexto principal
    driver.switch_to.default_content()













