# test_login_empleado.py
from selenium.webdriver.common.by import By
import time

def verify_contenido_inicio(driver):  # Cambiar el nombre de la función
    """Verifica el inicio de sesión."""
    driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@gmail.com")
    driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("admin123.")
    time.sleep(4)
    driver.find_element(By.XPATH, "//i[@id='show_password']").click()
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(4)
    actual_ver1 = driver.find_element(By.XPATH, "//h2[@id='swal2-title']").text

    driver.find_element(By.XPATH, "//button[@class = 'swal2-confirm swal2-styled']").click()
    time.sleep(4)

    if actual_ver1 == 'Conexión exitosa':
        print("Conexión exitosa - login correcto")
    else:
        print("error 404")
