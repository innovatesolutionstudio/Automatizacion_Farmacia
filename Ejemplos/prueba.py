import requests
import base64
import pyautogui
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from io import BytesIO
import pyperclip

# Configuración del WebDriver
options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Abre la página .aspx
driver.get('https://enlace.univalle.edu/san/webform/PAutenticar.aspx')
time.sleep(2)  # Espera para asegurar que la página y la imagen se carguen completamente

# Encuentra el elemento de la imagen y obtiene su atributo src
img_element = driver.find_element(By.XPATH, "//div[@class='row justify-content-center ']//div//div//img")
img_url = img_element.get_attribute("src")
driver.quit()

# Descarga y abre la imagen
if img_url.startswith("data:image"):
    # Si es data URL en base64
    img_data = base64.b64decode(img_url.split(",")[1])
else:
    # Si es URL normal, descargamos la imagen
    img_data = requests.get(img_url).content

image = Image.open(BytesIO(img_data))
image.show()  # Muestra la imagen (opcional)

# Guarda la imagen en el portapapeles para pegar en Paint
pyperclip.copy(img_data)

# Abre Paint
os.system("mspaint")
time.sleep(2)  # Espera para que Paint se abra

# Pega la imagen en Paint y guarda
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
pyautogui.hotkey("ctrl", "s")

# Define la ruta de descarga
download_path = os.path.join(os.path.expanduser("~"), "Downloads", "imagen_guardada.png")
pyautogui.write(download_path)
pyautogui.press("enter")

print(f"La imagen ha sido guardada en: {download_path}")

