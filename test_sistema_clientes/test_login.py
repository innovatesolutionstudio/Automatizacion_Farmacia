from selenium.webdriver.common.by import By
import time
 
def verify_login_cliente(driver):
    driver.get('http://localhost:3001/pagina_pedidos/login_clientes')
    time.sleep(2)

 # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ SISTEMA CLIENTES - LOGIN ++++++++++++++++++++++++++++++++++++++++++++++++++++
  
    driver.find_element(By.XPATH, "//input[@id='Codigo']").send_keys("mk28637046")
    driver.find_element(By.XPATH, "//input[@id='Contrasena']").send_keys("adasd")
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@class='btn-login']").click()
    time.sleep(4)


    actual_ver1 = driver.find_element(By.XPATH, "//h1[text()='Bienvenido de nuevo -> Marny']").text
    time.sleep(4)
    if (actual_ver1 == 'Bienvenido de nuevo -> Marny'):
        print("/////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nLogion inicado correctamente :)")
    else:
        print("\nLogion inicado erronea :()")
 
    