#Utilizaremos la librería requests para las peticiones HTTP, BS4 para el scrapper y xlsxwritter para escribir en el documento excel.
import requests
from bs4 import BeautifulSoup
import xlsxwriter

#Creación de archivo xlsx.
archivo = xlsxwriter.Workbook('fuentes.xlsx')
#Adición de una nueva hoja de worksheet llamada hoja.
hoja = archivo.add_worksheet()
#posicionamiento inicial para el archivo xlsx.
x = 1
y = 0
#Escritura de los títulos para las columnas en el archivo xlsx.
hoja.write(0,0,"Nombre Producto")
hoja.write(0,1,"Potencia[W]")
hoja.write(0,2,"Precio[CLP]")

#Iterador de la página web para buscar siguientes páginas.
contador_de_pagina = 1

#Contador de cuántos objetos han sido obtenidos.
contador_de_objetos = 0

total = 0
carga = 0
carga_reserva = 0
cargado = 0

numero_de_paginas = input('¿Cuántas páginas quiere revisar?: ')
numero_de_paginas = int(numero_de_paginas)

while contador_de_pagina < numero_de_paginas:
    
    #Llamado a la página web.
    pagina = requests.get(f'https://www.solotodo.cl/power_supplies?ordering=offer_price_usd&page={contador_de_pagina}&')
    #Parseo de la página web.
    soup = BeautifulSoup(pagina.text, 'html.parser')

    #Busca todos los div que tengan como nombre de clase d-flex flex-column category-browse-result.
    #Lo cual nos permite buscar los cuadros donde están los productos ordenados.
    for div in soup.findAll('div', attrs={'d-flex flex-column category-browse-result'}):
        
        #Busca todos los div que tengan como etiqueta <a> y obtiene el texto de ello asignandolo a producto.
        producto = div.find('a').text
        #print (producto)
        #Busca todos los div que tengan como etiqueta <class> con el nombre 'price flex-grow' y obtiene el texto de ello asignandolo a precio.
        precio = div.find(class_='price flex-grow').text
        #Cortamos el texto para solo obtener el precio en números, en este caso hasta 6 números.
        precio = precio[2:9]
        #print(precio)
        #Busca todos los div que tengan como etiqueta <class> con el nombre 'description-container' y obtiene el texto de ello asignandolo a potencia.
        potencia = div.find(class_='description-container').text
        #Cortamos el texto descriptivo para solo obtener el wattage.
        potencia = potencia[9:12]
        #print(potencia)

        #Imprime los datos recibidos en la hoja xlsx.
        hoja.write(x,y,producto)
        y = y+1
        hoja.write(x,y,potencia)
        y = y+1
        hoja.write(x,y,precio)
        x = x+1
        y = 0
        contador_de_objetos = contador_de_objetos + 1

    #Aquí está el sistema para contabilizar qué porcentaje del total lleva obtenido.
    if cargado == 0:
        total = contador_de_objetos * (numero_de_paginas-1)
        carga = (contador_de_objetos * 100)/total
        print("Cargando: {:.0f} %".format(carga))
        carga_reserva = carga
        cargado = 1
    else:
        carga = carga + carga_reserva
        print("Cargando: {:.0f} %".format(carga))   

    #Avance a la siguiente página.
    contador_de_pagina = contador_de_pagina + 1  

#Cierre del archivo.
archivo.close()