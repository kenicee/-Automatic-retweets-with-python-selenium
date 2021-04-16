from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os 

#esto es el archivo donde estan las cuentas
archivo = open('cuentas.txt')
nombre = archivo.readline()



for nombre in archivo:


    otps= Options()
    otps.add_argument("user-agent=Mozilla/5.0 (X11; linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)")

#   ESTO ES LA UBICACION DEL PROGRAMA

    driver_path1 = 'C:\\Users\\frigh\\OneDrive\\Escritorio\\python\\chromedriver.exe'
    driver_path = driver_path1
    
    driver = webdriver.Chrome(driver_path)
    driver.minimize_window ()
    driver.get("https://twitter.com/login")

#   login
    input_user =WebDriverWait(driver, 15).until(
    (EC.presence_of_element_located((By.XPATH, "//input[@name='session[username_or_email]' and @dir='auto']")))
    )
    input_pass = driver.find_element(By.XPATH, '//input[@name="session[password]"]')

#   En donde estan las cuentas que van a retweetiar

    archivo = open('cuentas.txt')
    input_user.send_keys(nombre)

#   en mi caso tuve que usar la misma contraseña en varias cuentas asi q no precise de abrir un archivo y leerlo
    password = "ASD123"
    input_pass.send_keys(password)
    boton = driver.find_element(By.XPATH, '//main//div[@data-testid="LoginForm_Login_Button"]//div[@dir="auto"]')
    boton.click()

#   Si la cuenta esta bloqueada se la saltea
    try:
        
        bloqued =WebDriverWait(driver, 5).until(
        (EC.presence_of_element_located((By.XPATH, "//div[@class='TextGroup-text']")))
        )
        if bloqued.is_displayed() and bloqued.is_enabled():
            driver.quit()
#   Si no esta bloqueada retwitea.
    except:    
        retweet =WebDriverWait(driver, 10).until(
        (EC.presence_of_element_located((By.XPATH, '//div[@data-testid="retweet"]')))
        )
        retweet.click()
        rtuit =WebDriverWait(driver, 10).until(
        (EC.presence_of_element_located((By.XPATH, '//div[[@data-testid="retweetConfirm"]')))
        )
        rtuit.click()
        driver.quit()

    nombre = archivo.readline()

archivo.close()
