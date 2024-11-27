from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
from PIL import Image
import time
import re
import os
 
# Specify the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
 
# Configuración automática del WebDriver
driver = webdriver.Chrome()
 
# Maximizar la ventana del navegador
driver.maximize_window()
 
# Abrir URL en el navegador
driver.get('https://enlace.univalle.edu/san/webform/PAutenticar.aspx')

intentos = 0 
 
while True:
    intentos += 1 
    time.sleep(1)
 
    driver.find_element(By.XPATH, "//input[@maxlength='15']").send_keys("jpj2026628")
 
    # espera a que el capcha sea visible
    captcha_element = driver.find_element(By.ID,"CPHBody_imgCaptcha")
   
    # Tomar la captura de pantalla
    MyCapcha = captcha_element.screenshot_as_png

    with open("Mycaptcha.png", "wb") as file:

        file.write(MyCapcha)
 
    Captura_Mycapcha = Image.open("Mycaptcha.png")

    resultado = pytesseract.image_to_string(Captura_Mycapcha)
    
    #limpiamos el texto del capcha
    texto = re.sub(r'[^a-zA-Z0-9]', '', resultado)
  
    #introducimos el capcha al input
    driver.find_element(By.XPATH, "//input[@id='CPHBody_txbCaptcha']").send_keys(texto)
    time.sleep(3)


    driver.find_element(By.XPATH, "//input[@id='CPHBody_lbtnIngresar']").click()
    time.sleep(1)
 
 
    # Eliminar la cada ves que reiniciamos
    os.remove("Mycaptcha.png")

    #validacion de si da o no da el capcha
    try:

        driver.find_element(By.XPATH, "//*[@id='CPHBody_lblCaptchaError']")
        print("--------------------------------------------------------------------------------------------------")
        print("Error: CAPTCHA incorrecto.")
        print(f"Código del CAPTCHA incorrecto: {texto}")
        print(f"Intento número: {intentos}")
    except:
        print("CAPTCHA ingresado correctamente.")
        print(f"Intentos realizados: {intentos}")
        break  # Salir del bucle si el CAPTCHA es correcto



 
driver.find_element(By.XPATH, "//input[@value='ESTUDIANTE']").click()
time.sleep(10)


driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbDigito1']").send_keys(1)
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbDigito2']").send_keys(6)
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbDigito3']").send_keys(9)
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbDigito4']").send_keys(8)
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbDigito5']").send_keys(7)
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='ctl00$CPHBody$txbDigito6']").send_keys(4)
time.sleep(1)


time.sleep(1)
driver.find_element(By.XPATH, "//input[@id='CPHBody_lkbValidatePin']").click()

time.sleep(30)

print("\n\n\n\n")
print("""       
                💖        💖
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀💖💖💖⠀⠀⠀💖💖💖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀💖💖💖💖💖💖💖💖💖⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀💖💖💖💖💖💖💖💖💖💖⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀💖💖💖💖💖💖💖💖💖⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀💖💖💖💖💖💖💖⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀💖💖💖💖💖⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀💖💖💖⠀⠀⠀
                💖
      ¡Apruébeme, Inge! 💻✨⠀⠀⠀⠀⠀⠀⠀
""")
