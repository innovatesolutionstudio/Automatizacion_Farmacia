# test_sistema.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
#llamado a la funcion del login
from test_login_empleado import verify_contenido_inicio  

#llamado a la funcion del tablero
from test_tablero import verify_contenido_tablero  

#llamado a la funcion del modulo de compras
from test_compras import verify_vista_compras
class Test_Sistema:

    def setup_method(self):
        """Configura el entorno inicial para las pruebas."""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get('http://localhost:3001/login')

    def teardown_method(self):
        """Cierra el navegador."""
        self.driver.quit()
        print("\nPrueba de automatizado completado")

    def test_sistema(self):
        """Llama a la función de login y verifica el resultado."""
        verify_contenido_inicio(self.driver) 
        time.sleep(5)
      #  """Llama a la función del tablero"""
    #    verify_contenido_tablero(self.driver) 


        """Llama a la función para la vista del modulo de compras"""
        verify_vista_compras(self.driver) 

       
