"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la libreria necesaria

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:3001/login')

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_form_login(self):
        self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@gmail.com")
        self.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("admin123.")
        self.time.sleep(4)
        self.driver.find_element(By.XPATH, "//i[@id='show_password']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        time.sleep(4)
        actual_verf1 = self.driver.find_element(By.XPATH, "//h2[@id='swal2-title']").text
        esperada_verf2    = "Conexión exitosa"
        actual_verf1 = self.driver.find_element(By.XPATH, "//div[@id='swal2-content']").text
        esperada_verf2 = "Inicio de sesión correcto"
        assert esperada_verf1 in actual_verf1, f"ERROR, actual {actual_verf1}, esperado: {esperada_verf1}"
        assert esperada_verf2 in actual_verf2, f"ERROR, actual {actual_verf2}, esperado: {esperada_verf2}"

    

    def test_verify_login_notificar(self):
        self.driver.find_element(By.XPATH, "//button[@id='sign-up-btn']").click()
        self.driver.find_element(By.XPATH, "//textarea[@name='descripcion']").click()
        time.sleep(4)
        
   
    
