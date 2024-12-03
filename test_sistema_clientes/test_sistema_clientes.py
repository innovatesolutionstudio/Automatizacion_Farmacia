# test_sistema.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


#llamado a la funcion del login
from test_login import verify_login_cliente 
from test_inicio import verify_sistema_cliente_inicio   
from test_ventascarrito import verify_contenido_ventascarrito   


class Test_Sistema_clientes:


    def setup_method(self):

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get('http://localhost:3001/')

    def teardown_method(self):
    
        self.driver.quit()
        print("\n////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nPrueba de automatizado completado")
        print("/////////////////////////////////////////////////////////////////////////////////////////////")

    def test_sistema(self):
        #inicio - contactos
        verify_sistema_cliente_inicio(self.driver) 
        time.sleep(2)

        #tienda
        verify_contenido_ventascarrito(self.driver) 
        time.sleep(2)

        #login clientes
        verify_login_cliente(self.driver) 
        time.sleep(2)



