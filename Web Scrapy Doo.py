from selenium.webdriver.edge.service import Service
from selenium import Webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time 
import numpy as np

#FIX ME PLEASE
#esta parte funcionaba pero ya no esta jalando falta hacer pruebas
os.chdir("direccion donde se baja el archvo")

try: # un try para borrar el archivo si ya se encuentra en descargas y no se duplique
    os.remove('nombre_archivo_borrar')
    print("Removed")
except:
    print("File not found")
#HASTA AQUI

#esto cambia dependiendo del driver que usemos , yo use Edge pero seria bueno probar con Chrome
service = Service(executable_path="path_al_driver_executable")
driver = webdriver.Edge(service=service)
driver.get('direccion de la pagina donde se quiere scrapear')
assert '' in driver.title

elem = driver.find_element(By.ID, 'Id del elemento que se quiere encontrar') #elemento que queremos hacerle una accion
action = ActionChains(driver) 
action.click(elem) #click al elemento que queremos descargar
action.perform() #realizar accion

time.sleep(7) #esperamos 7 segundos para que se ejecute , esto se puede cambiar por una funcion de la libreria selenium hay que prbar
driver.quit() #cerrar driver