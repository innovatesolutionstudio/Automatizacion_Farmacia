from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from test_login_cliente import verify_login_cliente  

class Test_Sistema:

    def setup_method(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get('http://localhost:3001/pagina_pedidos/clientes_index')

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_sistema(self):
        """Llama a la función de login y verifica el resultado."""
        verify_login_cliente(self.driver) 