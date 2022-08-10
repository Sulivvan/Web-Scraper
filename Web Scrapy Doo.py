from selenium.webdriver.edge.service import Service
from selenium import Webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time 
import pandas as pd 


os.chdir("direccion donde se baja el archvo")

try: # un try para borrar el archivo si ya se encuentra en descargas y no se duplique
    os.remove('nombre_descargado_a_borrar')
    print("Removed")
except:
    print("File not found")


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

#agregado falta comentar para subir a git

print(os.getcwd())
stage= ['BRAND', 'BE_CHECKPOINT'] #Lista de los Stages que hay en el area de interes

#un try para abrir el archivo y no morir en el intento
try:
    ws =pd.read_excel('nombre_archivo_descargado')
    print("Load succesfull")
except:
    ("File not found")

#ahora filtramos primero por location segun mi archivo de interes
first_filter = ws.query("Location == 'MEXPROCESS'")
#despues filtramos por stage segun mi interes estas lineas se pudiesen convertir en 1 pero
#me sirve tenerlo asi para mas control y menos confusion 
lot_list = first_filter.query("Stage == @stage")

#una vez ya filtrado vamos a borrar el archivo si es que existe previamente
#para refrescar los datos dia a dia, otro try para no morir en el intento
try:
    os.remove("filter_list.xlsx")
except:
    print("filter_list not found")

# ahora nuestra lista ya filtrada la exportamos como excel en la carpeta en la que nos encontramos
lot_list.to_excel("./filter_list.xlsx")

#y abrimos el archivo automaticamente con un try
try:
    os.startfile('filter_list.xlsx')
except:
    print("file not found")

    
