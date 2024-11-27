import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import easyocr

# Configuración del WebDriver usando Service
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Maximizar la ventana y abrir la URL
driver.maximize_window()
driver.get('https://enlace.univalle.edu/san/webform/PAutenticar.aspx')

# Completa el formulario
driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbCuenta']").send_keys("jpj2026628")
time.sleep(1)
driver.get('https://enlace.univalle.edu/san/WebForm/PCaptcha.aspx')

#driver.find_element(By.XPATH, "//div[@class='row justify-content-center ']//div//div//input[@name = 'ctl00$CPHBody$imbRecargar']").click()

time.sleep(2)
# Obtiene la URL de la imagen
img_element = driver.find_element(By.XPATH, "//div[@class='row justify-content-center ']//div//div//img")
img_url = img_element.get_attribute("src")



# Define la ruta de descarga en la carpeta de Descargas
download_path = os.path.join(os.path.expanduser("~"), "Downloads", "captcha_image.png")

# Descarga la imagen y guárdala en la carpeta de Descargas
img_data = requests.get(img_url).content
with open(download_path, 'wb') as handler:
    handler.write(img_data)




print(f"La imagen se ha descargado en: {download_path}")


time.sleep(1)

# Inicializa el lector de EasyOCR
reader = easyocr.Reader(['en'])  # Puedes agregar más idiomas si es necesario

# Procesa la imagen
result = reader.readtext('C:/Users/jerom/Downloads/captcha_image.png', detail=0)

# Imprime el texto detectado
print('Texto detectado:', ' '.join(result))


driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbCaptcha']").send_keys(f"{result}")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$lbtnIngresar']").click()



# Cierra el navegador
driver.quit()
