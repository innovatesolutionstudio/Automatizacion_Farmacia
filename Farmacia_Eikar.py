import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestNavegacion:
    def setup_method(self):
        # Configurar el controlador
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()
        print("Prueba completada y navegador cerrado.")

    def test_navegacion_pagina(self):
        try:
            # Navegar a la página inicial
            self.driver.get('http://localhost:3001/pagina_pedidos/clientes_index')

            # Hacer clic en el enlace "Contacto"
            self.driver.find_element(By.XPATH, "//a[text()='Contacto']").click()
            print("Clic en el enlace 'Contacto'.")
            time.sleep(3)

            # Hacer clic en el enlace "Inicio"
            self.driver.find_element(By.XPATH, "//a[text()='Inicio']").click()
            print("Redirigido a la página de inicio.")
            time.sleep(3)

            # Navegar a la página de login
            self.driver.get('http://localhost:3001/login')
            print("Redirigido a la página de login de empleados.")
            time.sleep(3)

            # Ingresar el correo
            self.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("admin@gmail.com")
            print("Correo ingresado: admin@gmail.com")
            time.sleep(2)

            # Ingresar la contraseña
            self.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("admin123.")
            print("Contraseña ingresada: admin123")
            time.sleep(2)

            # Enviar el formulario de inicio de sesión
            self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
            print("Formulario enviado.")
            time.sleep(3)

            # Manejar la alerta de SweetAlert2
            confirm_button = self.driver.find_element(By.CSS_SELECTOR, "button.swal2-confirm")
            confirm_button.click()
            print("Botón 'OK' de la alerta presionado.")
            time.sleep(3)

            # Hacer clic en el enlace 'Ventas'
            self.driver.find_element(By.XPATH, "//a[@href='#ventas']").click()
            print("Clic en el enlace 'Ventas'.")
            time.sleep(3)

                        # Hacer clic en el enlace 'Nueva Venta'
            self.driver.find_element(By.XPATH, "//a[@onclick=\"cargarContenido('/nueva_venta')\"]").click()
            print("Clic en el enlace 'Nueva Venta'.")
            time.sleep(3)


            # Hacer clic en el enlace 'Stock Disponible'
            self.driver.find_element(By.XPATH, "//a[@onclick=\"cargarContenido('/inventario_vista')\"]").click()
            print("Clic en el enlace 'Stock Disponible'.")
            time.sleep(3)


            # Hacer clic en el enlace 'Historial de ventas'
            self.driver.find_element(By.XPATH, "//a[@onclick=\"cargarContenido('/ventas')\"]").click()
            print("Clic en el enlace 'Historial de ventas'.")
            time.sleep(3)

        except Exception as e:
            print(f"Ocurrió un error: {e}")
            raise