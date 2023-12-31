# CursoPowerBI
## ¿Qué es Power BI?

Para saber que es Power BI primero se debe definir Business Intelligence, que es la habilidad de transformar los datos en información y la información en conocimiento, de forma que se pueda optimizar el proceso de toma de decisiones en los negocios.

Los datos normalmente vienen en bases, cuando se conocen los datos y como se relacionan, lo que significa cada campo y como se quiere plasmar hacia el objetivo final, se transforman y se convierten en información, una vez teniendo la información se muestran en una gráfica o diferentes indicadores para transformar la información en conocimiento y optimizar el proceso de toma de decisiones en los negocios.

Ahora si, Power BI es la solución destinada a la inteligencia empresarial (business intelligenge), que permite unir diferentes fuentes de datos, modelizar y analizar datos para después, presentarlos a través de páneles e informes; que puedan ser consultados de una manera muy fácil, atractiva e intuitiva.

## Descarga de Power BI

- Buscar en google: descargar power bi
- Entrar en el primer link (powerbi.microsoft.com)
- En el menú Microsoft Power BI.Desktop, seleccionar opciones avanzadas de descarga
- Seleccionar el lenguaje con el que se quiera trabajar click en descargar
- Seleccionar la versión a 64 bits (si el pc es a 64) click en next y se descargará el ejecutable de PowerBI
- Dar doble click sobre el ejecutable, seleccionar el lenguaje, siguiente, siguiente, aceptar los términos y condiciones, siguiente, dejar la ruta predeterminada, siguiente, si quiere dejar el acceso directo marcar el chulo, sino desmarcarlo y darle click en instalar

## Introducción a los bloques de creación

Los bloques de creación son:
- Visualizaciones:
- Paneles:
- Informes:
- Aplicaciones:
- Conjuntos de datos:

A veces se hace referencia como contenido de Power BI y, dicho contenido se encuentra en las áreas de trabajo.

![Imagen de flujo de lo que se habló](Imagenes%20de%20relevancia/Flujo%20Power%20BI.png)

## Servicios de Power BI

- Bases de datos en la nube: desde el servicio de Power BI se puede conectar con:
    - Azure SQL Database
    - Azure SQL Data Warehouse
    - Spark en HDInstinct de Azure

- Conexiones a otras bases de datos: existen mas de 100 conexiones a origenes de datos con Power BI, entre las cuales de cuales destacan:
XML, bases de datos con access, Adobe Analytics, Amazon RedShift, azure analysis services, excel, facebook, github, google analytics, Google big Query, JSON, MySQL, Oracle, PDF, Script de Python, Script de R, Survey Monkey, Texto o CSV, Web, Objetos/informes de salesforce.

## Conexión a origenes de datos

Para ver las diferentes conexiones a datos que ofrece Power BI, se va a inicio, en la sección de datos, seleccionar el icono "obtener datos", se desplega, seleccionar mas y ahí están todas las posibles conexiones.

## Append y Merge

Cuando una tabla tiene una información similar, pero en columnas diferentes, es decir, que está separada y se quiere mezclar en una sola tabla para luego mostrar sus valores, se hace de la siguiente manera:

- Si es un archivo de excel y este tiene las columnas separadas, se abre en Power BI y se seleccionan todas las tablas sobre las cuales se va a trabajar.
- Seleccionar transformar datos (transform data) y abre una nueva ventana
- En la sección de combinar (combine) seleccionar anexar consultas (append queries), allí seleecionar consultas para crear una nueva (append queries as new)
- Pregunta si se quieren apendizar 2 tablas o 3 o más, seleccionar la opción a conveniencia.
- Seleccionar la primer tabla que se desea y posteriormente la que se le va a mezclar
- Una vez apendizadas o mezcladas (append), se procede a combinarlas (merge)
- Seleccionar combinar consultas (merge queries), luego combinar consultas para crear una nueva (merge queries as new)
- En caso que se haya hecho un append, se creará una tabla llamada append1; se va a seleccionar esa tabla y luego se selecciona la llave (id), selecciona el tipo de combinación que se desea (generalmente se deja el que aparece por defecto)
- En caso que aparezca una información diferente a la deseada y diga "table" se selecciona la flecha que aparece en la cabecera y se elige el campo que se desea dejar.

## Reemplazar valores

En caso que haya una actualización con un campo específico en una base de datos, por ejemplo una nueva cantidad en un campo específico se hace lo siguiente:

- Seleccionar la base de datos sobre la cual se va a trabajar
- Ir a la sección de consultas (queries), seleccionar transformar datos (transform data)
- Abrirá la base, al lado izquierdo se ven las bases que se tienen, se va a la base que se desea modificar
- Selecciona el dato que se quiere cambiar
- Ir al menú de transformar (transform), seleccionar la opción reemplazar los valores (replace values)
- Click en cerrar y aplicar (clase & apply)
- Se volverá a cargar la información con los cambios aplicados y se verá reflejado en la base de datos

## Detección de errores al cargar una base de datos

Cuando hay un error detectado y para reemplazarlos, simplemente se va a la pestaña transformar, selecciona la flechita de transformar valores, desplega, reemplazar errores y poner un valor por el cual se van a reemplazar estos errores.

Otra forma es seleccionando la columna, darle click derecho al título, seleccionar la opción quitar errores y los quitará automáticamente.

Otra forma es seleccionar la columna, ir a la pestaña de inicio, desplegar conservar filas, seleccionar conservar errores.

Mantiene las mismas filas y no le quita información a la base, mantiene los errores, pero los ignora.

Selecciona cerrar y aplicar y listo, la base de datos se cargará correctamente.

En caso que la base de datos esté en una nueva ruta se hace lo siguiente:
- en el menú de inicio, desplegar transformar datos, configuración de origen de datos
- Click en cambiar de origen
- Buscar donde está guardado el archivo
- Click en aceptar y cerrar
- Una vez actualizado se mostrará la base de datos que se necesita
- Si se trataron errores con anterioridad, no es necesario volverlos a tratar; la base de datos se actualizará de manera correcta

## Pivots & Unpivots

**Unpivot:** Es la forma de desvincular datos a través de un tributo o varios tributos conocido como columnas, transponerlos en una sola columna, donde cada entrada será un atributo y convertir una segunda columna en valores

![pivot](Imagenes%20de%20relevancia/imagen%20previa%20a%20pivot.png)

En la imagen de arriba se ve una información de id cliente (1) y ventas realizadas desde 01(enero) hasta 11(noviembre); el unpivot consiste en poner una columna con el id del cliente, otra columna con los meses y otra con las ventas por mes; de la siguiente manera:

![unpivot](Imagenes%20de%20relevancia/unpivot.png)

**Pivot:** Es el paso opuesto al unpivot, es decir que si se tienen las columnas con id cliente, fecha y ventas, todo eso se pase a filas; donde id sea una fila, los meses las columnas y las ventas el valor correspondiente a cada mes.

En power BI se hace de la siguiente manera:
- Cargar la base de datos
- Seleccionar la hoja de interés
- Transformar datos
- En el power query verificar que haya respetado los tipos de datos
- Para el unpivot:
    - seleccionar las columas o atributos a los cuales se les quiere realizar esta función
    - Click en el menú transformar
    - Desplegar dinamización de columnas (unpivot columns)
    - Seleccionar anular dinamización de columnas seleccionadas únicamente (unpivot only selected columns)
    - Dará un atributo que es cada entrada del mes y valor correspondiente
- Para el pivot:
    - Se selecciona la columna que se quiere transponer en fila (únicamente la columna del atributo)
    - Seleccionar transformar columna dinámica (pivot column)
    - Abrirá una nueva ventana donde piden un nombre para crear columnas nuevas, seleccionar la columna de valores
    - Desplegar opciones avanzadas
    - Da una opción de función de valor agregado, si los registros son únicos por cliente o atributo, dará el mismo valor
    - Si no se sabe si hay registros duplicados o no, seleccionar la opción "no agregar"
    - Aceptar y convierte las filas en columnas
