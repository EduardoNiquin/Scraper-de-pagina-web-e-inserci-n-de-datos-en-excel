# Scraper de página web e inserción de datos en hoja excel.
Este programa busca los datos de fuente de poder en la página web de solotodo.cl y los ordena por nombre, potencia y precio en un archivo .xlsx

Para su utilización se implementó el uso de BeafitulSoup para la lectura del html de la página web.
También se hizo uso de xlsxwriter para la creación y escritura del archivo xlsx.

Línea 7 puede ser modificada para cambiar el nombre del archivo generado, éste será generado en la dirección del documento Scraper.py

En la línea 14, 15 y 16 están los títulos de las columnas para un mejor entendimiento de los valores en el documento excel.

De la línea 24 a 27 están los datos de carga y estado, éstos sirven para llevar un registro de cuántos elementos han sido insertados en el archivo y así poder saber el porcentaje que falta hasta su finalización.

En la línea 29 tenemos el input del usuario, de esta forma el usuario puede determinar cuántas páginas quiere que revise y cargue el programa, debe ser igual o mayor a 1.


Posteriormente se hace el request para los datos de la página web y éstos por parseados de dal forma que podemos obtener los datos que queramos a continuación:

De la línea 41 a la 55 se realiza la búsqueda de éstos datos a través de sus etiquetas y los nombres de las clases para obtener el nombre del producto, su potencia en watts y el precio mínimo del mismo.

De la 58 a la 64 procedemos por la escritura en la hoja del documento xlsx ordenando por coordenadas (X,Y) según corresponda.

Luego en la línea 79 tenemos el avance en la página en caso de que el usuario haya pedido más de una.

Y por último el cierre del archivo para evitar errores.
