import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pyperclip

service = Service('C:/Users/JFROJAS/Desktop/Merit/Project/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/imghp")
#
print("Google Images opened")
#

# Carpeta con las imágenes
folder = r"C:\Users\JFROJAS\Desktop\Merit\Project\PDF\output"

# Ruta completa de la carpeta donde se guardará el archivo de texto
output_folder = r"C:\Users\JFROJAS\Desktop\Merit\Project\PDF\output"

# Iterar sobre cada archivo en la carpeta
for filename in os.listdir(folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        time.sleep(2)
        filepath = os.path.join(folder, filename)
        filepath = filepath.replace("/", "\\")
        # Seleccionar la opción de "Buscar por imagen" nDcEnd
        search_by_image_button = driver.find_element(by='class name', value='nDcEnd')
        search_by_image_button.click()
        print("Search by image button clicked")
        # Esperar a que cargue la página
        # Escribir el filepath actual en el campo de búsqueda
        search_input = driver.find_element(by='class name', value='cB9M7')
        search_upload = driver.find_element(by='class name', value='DV7the')
        search_upload.click()
        time.sleep(1)
        pyautogui.typewrite(filepath, interval=0.001) 
        pyautogui.press('enter')
        print("File uploaded")
        time.sleep(5)
        pyautogui.click(270, 630)
        print("Tex button clicked")
        time.sleep(3)
        pyautogui.click(750, 570)
        time.sleep(3)
        pyautogui.click(600, 280)
        time.sleep(2)

        # Obtener el texto del portapapeles
        text_to_append = pyperclip.paste()
        
        # Ruta completa del archivo de texto resultante
        output_file_path = os.path.join(output_folder, "texto.txt")

        # Abrir el archivo en modo de escritura y agregar el texto al final
        with open(output_file_path, "a", encoding='utf-8') as f:
            f.write(text_to_append)

        driver.get("https://www.google.com/imghp")
