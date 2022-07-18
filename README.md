# Scraper de página web e inserción de datos en hoja excel.

#### Este programa busca los datos de fuentes de poder en la página web de solotodo.cl y los ordena en un archivo .xlsx

### Para su utilización se implementó el uso de BeafitulSoup para la lectura del código fuente de la página web.
### También se hizo uso de xlsxwriter para la creación y escritura del archivo xlsx.

##### En la línea 7, podemos modificar el nombre del archivo xlsx reemplazando lo que queramos por 'fuentes'.

```
archivo = xlsxwriter.Workbook('fuentes.xlsx')
```

##### En la línea 14, 15 y 16 están los títulos de las columnas para un mejor entendimiento de los valores en el documento excel.

```
hoja.write(0,0,"Nombre Producto")
hoja.write(0,1,"Potencia[W]")
hoja.write(0,2,"Precio[CLP]")
```


##### De la línea 24 a 27 están los datos de carga y estado, éstos sirven para llevar un registro de cuántos elementos han sido insertados en el archivo y así poder saber el porcentaje que falta hasta su finalización.

```
total = 0
carga = 0
carga_reserva = 0
cargado = 0
```

##### En la línea 29 tenemos el input del usuario, de esta forma el usuario puede determinar cuántas páginas quiere que revise y cargue el programa, debe ser igual o mayor a 1.

```
numero_de_paginas = input('¿Cuántas páginas quiere revisar?: ')
```


#### Posteriormente se hace el request para los datos de la página web y éstos por parseados de dal forma que podemos obtener los datos que queramos a continuación:

##### De la línea 41 a la 55 se realiza la búsqueda de éstos datos a través de sus etiquetas y los nombres de las clases para obtener el nombre del producto, su potencia en watts y el precio mínimo del mismo.

```
for div in soup.findAll('div', attrs={'d-flex flex-column category-browse-result'}):
        producto = div.find('a').text
        precio = div.find(class_='price flex-grow').text
        precio = precio[2:9]
        potencia = div.find(class_='description-container').text
        potencia = potencia[9:12]
```

##### De la 58 a la 64 procedemos por la escritura en la hoja del documento xlsx ordenando por coordenadas (X,Y) según corresponda.

```
hoja.write(x,y,producto)
        y = y+1
        hoja.write(x,y,potencia)
        y = y+1
        hoja.write(x,y,precio)
        x = x+1
        y = 0
```
##### Luego en la línea 79 tenemos el avance en la página en caso de que el usuario haya pedido más de una.

```
    contador_de_pagina = contador_de_pagina + 1  
```
##### Y por último el cierre del archivo para evitar errores.
```
archivo.close()
```
