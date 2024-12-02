from selenium.webdriver.common.by import By
import time

def verify_login_cliente(driver):
    driver.find_element(By.XPATH, "//a[@id='tienda-loc']").click()  
    actual_ver = driver.find_element(By.XPATH, "//h2[@class='page-title']").text
    time.sleep(4)
    if actual_ver == 'Nuestros Productos':
        print("Redirecciono a la tienda")
    else:
        print("Error 404")


