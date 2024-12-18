from selenium.webdriver.common.by import By
import time

def verify_login_cliente(driver):
    driver.find_element(By.XPATH, "//a[@id='tienda-loc']").click()  
    actual_ver = driver.find_element(By.XPATH, "//main[@class='login-container'']//h1").text
    time.sleep(4)

    driver.find_element(By.XPATH, "//input[@id='Codigo']").send_keys("qwerty")
    driver.find_element(By.XPATH, "//input[@id='Contrasena']").send_keys("2323")
    time.sleep(4)
    driver.find_element(By.XPATH, "//button[@class='btn-login']").click()
    time.sleep(4)
    actual_ver1 = driver.find_element(By.XPATH, "//div[@class='topbar']").text
    time.sleep(4)
    if actual_ver == 'Iniciar Sesión':
        print("Redirecciono al login")
    else:
        print("Error 404")

    if actual_ver1 == 'Bienvenido de nuevo':
        print("Incio de sesion exitosa")
    else:
        print("Error 404")