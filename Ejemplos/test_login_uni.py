from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import unicodedata

class TestSIU:
    
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://wordledehoy.com/')
        time.sleep(2)

        
    def teardown_method(self):
        self.driver.quit()

    def test_verify_title(self):

        self.driver.find_element(By.XPATH, "//span[text() = 'Nuevo']//parent::div[@class = 'article-content']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class = 'reveal-button']").click()
        time.sleep(2)
      

        solucion = self.driver.find_element(By.XPATH, "//p[@class = 'solution-word']").text
        solucion = solucion.lower()  # Convertir a minúsculas
        solucion = ''.join(
            (c for c in unicodedata.normalize('NFD', solucion) if unicodedata.category(c) != 'Mn')
        )

        print(f"LA SOLUCION ES: {solucion}")
        time.sleep(5)
        self.driver.get('https://lapalabradeldia.com/')
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='¡Jugar!']").click()
        time.sleep(5)

        for letra in solucion:
            print(f"Escrbiendo la letra {letra}")
            self.driver.find_element(By.XPATH, f"//button[text()='{letra}']").click()
            time.sleep(1)
        
        self.driver.find_element(By.XPATH, f"//button[@aria-label = 'procesar palabrakey']").click()
        time.sleep(10)

        esperado2="Victorias"
        actual2 = self.driver.find_element(By.XPATH, "//p[text()='Victorias']").text
        assert esperado2 in actual2, f"FAIL: actual{actual2}, esperado {esperado2}"
      
        



