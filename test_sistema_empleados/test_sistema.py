# test_sistema.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


#llamado a la funcion del login
from test_login_empleado import verify_contenido_inicio  

#llamado a la funcion del modulo de compras
from test_compras import verify_modulo_compras
from test_finanzas import verify_modulo_finanzas

#llamado a la funcion del tablero
from test_recursos import verify_contenido_recursos  
#llamado a la funcion del tablero
from test_pedidos import verify_contenido_pedidos  
#llamando a la funcion modulo ventas
from test_ventas import verify_registro_ventas


class Test_Sistema:


    def setup_method(self):

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get('http://localhost:3001/login')

    def teardown_method(self):
    
        self.driver.quit()
        print("/////////////////////////////////////////////////////////////////////////////////////////////")
        print("\nPrueba de automatizado completado")
        print("/////////////////////////////////////////////////////////////////////////////////////////////")

    def test_sistema(self):
        
        #login
        verify_contenido_inicio(self.driver) 
        time.sleep(2)

        #tablero

        time.sleep(2)

        #finanzas
        verify_modulo_finanzas(self.driver)
        time.sleep(2)

        #ventas
        verify_registro_ventas(self.driver)
        time.sleep(2)

        #compras
        verify_modulo_compras(self.driver) 
        time.sleep(2)
        
        #pedidos
        verify_contenido_pedidos(self.driver)
        time.sleep(2)

        #recursos humanos
        verify_contenido_recursos(self.driver)
        time.sleep(2)
   