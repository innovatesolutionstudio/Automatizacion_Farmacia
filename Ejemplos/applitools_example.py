from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from applitools.selenium import Eyes, Target

# Applitools - Configura tu API Key
APPLITOOLS_API_KEY = 'FCRWYxHaRqcMeifG98vayJvkzVgZuMouyORdrmAGuCZM110'

# Inicializar Applitools Eyes
eyes = Eyes()
eyes.api_key = APPLITOOLS_API_KEY

# Configuración automática del WebDriver sin usar Service
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

try:
    # Empezar una sesión de prueba visual con Applitools
    eyes.open(driver=driver, app_name='Demo App', test_name='Prueba Visual con Applitools')

    # Navegar a la página que queremos probar
    driver.get('https://demo.applitools.com')

    # Tomar una captura de pantalla completa de la página
    eyes.check("Página completa", Target.window().fully())

    # Simulación de una interacción: Rellenar campos de formulario y hacer clic en "Log In"
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.find_element(By.ID, "log-in").click()

    # Tomar una captura de pantalla después de la interacción
    eyes.check("Después del Login", Target.window().fully())

    # Cerrar los ojos de Applitools y finalizar la prueba
    eyes.close()

finally:
    # Finalizar la sesión de Selenium y Applitools
    driver.quit()
    eyes.abort_if_not_closed()

print("Prueba visual completada")
