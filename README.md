# CursoPowerBI

---

## ¿Qué es Power BI?

Para saber que es Power BI primero se debe definir Business Intelligence, que es la habilidad de transformar los datos en información y la información en conocimiento, de forma que se pueda optimizar el proceso de toma de decisiones en los negocios.

Los datos normalmente vienen en bases, cuando se conocen los datos y como se relacionan, lo que significa cada campo y como se quiere plasmar hacia el objetivo final, se transforman y se convierten en información, una vez teniendo la información se muestran en una gráfica o diferentes indicadores para transformar la información en conocimiento y optimizar el proceso de toma de decisiones en los negocios.

Ahora si, Power BI es la solución destinada a la inteligencia empresarial (business intelligenge), que permite unir diferentes fuentes de datos, modelizar y analizar datos para después, presentarlos a través de páneles e informes; que puedan ser consultados de una manera muy fácil, atractiva e intitiva.

---

## Descarga de Power BI

- Buscar en google: descargar power bi
- Entrar en el primer link (powerbi.microsoft.com)
- En el menú Microsoft Power BI.Desktop, seleccionar opciones avanzadas de descarga
- Seleccionar el lenguaje con el que se quiera trabajar click en descargar
- Seleccionar la versión a 64 bits (si el pc es a 64) click en next y se descargará el ejecutable de PowerBI
- Dar doble click sobre el ejecutable, seleccionar el lenguaje, siguiente, siguiente, aceptar los términos y condiciones, siguiente, dejar la ruta predeterminada, siguiente, si quiere dejar el acceso directo marcar el chulo, sino desmarcarlo y darle click en instalar

---

## Introducción a los bloques de creación

Los bloques de creación son:
- Visualizaciones:
- Paneles:
- Informes:
- Aplicaciones:
- Conjuntos de datos:

A veces se hace referencia como contenido de Power BI y, dicho contenido se encuentra en las áreas de trabajo.

![Imagen de flujo de lo que se habló](Imagenes%20de%20relevancia/Flujo%20Power%20BI.png)

---

## Servicios de Power BI

- Bases de datos en la nube: desde el servicio de Power BI se puede conectar con:
    - Azure SQL Database
    - Azure SQL Data Warehouse
    - Spark en HDInstinct de Azure

- Conexiones a otras bases de datos: existen mas de 100 conexiones a origenes de datos con Power BI, entre las cuales de cuales destacan:
XML, bases de datos con access, Adobe Analytics, Amazon RedShift, azure analysis services, excel, facebook, github, google analytics, Google big Query, JSON, MySQL, Oracle, PDF, Script de Python, Script de R, Survey Monkey, Texto o CSV, Web, Objetos/informes de salesforce.

---

## Conexión a origenes de datos

Para ver las diferentes conexiones a datos que ofrece Power BI, se va a inicio, en la sección de datos, seleccionar el icono "obtener datos", se desplega, seleccionar mas y ahí están todas las posibles conexiones.

---

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

---

## Reemplazar valores

En caso que haya una actualización con un campo específico en una base de datos, por ejemplo una nueva cantidad en un campo específico se hace lo siguiente:

- Seleccionar la base de datos sobre la cual se va a trabajar
- Ir a la sección de consultas (queries), seleccionar transformar datos (transform data)
- Abrirá la base, al lado izquierdo se ven las bases que se tienen, se va a la base que se desea modificar
- Selecciona el dato que se quiere cambiar
- Ir al menú de transformar (transform), seleccionar la opción reemplazar los valores (replace values)
- Click en cerrar y aplicar (clase & apply)
- Se volverá a cargar la información con los cambios aplicados y se verá reflejado en la base de datos

---

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

---

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
    ![Logo_Pivot-Unpivot](Imagenes%20de%20relevancia/Pivot-unpivot.png)
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

---

## Split

Sirve para dividir una consulta en dos, para empezar se obtienen los datos

- Primeramente abrir el archivo en su respectivo formato
- Click en transformar datos, abre el power query
- Guardar en una base la base original, sin cambio, y en una segunda base obtener la base transpuesta (aplicando unpivot) y hacer la consulta que se necesita
    - Seleccionar los campos a hacer el unpivot
    - Hacer el unpivot
    - Hacer el filtro que se necesita consultar su información específica
- Crear la base alterna a la consulta específica:
    - Ir al apartado de la pantalla de pasos aplicados, seleccionar el paso desde donde se quiere guardar la nueva base, es decir, seleccionar desde donde se anula la dinamización
    - Click derecho donde se quiera hacer el split o la división
    - Seleccionar extraer anteriores
    - Abre una ventana emergente, pide nombre para la nueva consulta o la nueva base (ponerle base original)
    - Ir a inicio, cerrar y aplicar
    - Las bases (incluyendo la nueva) aparecerán en el apartado de campos
---

## Esquema estrella
Es un enfoque de modelado maduro ampliamente adoptado por los almacenes de datos relacionales. Requiere que los modeladores clasifiquen sus tablas modelo como dimensión o hecho.

**Tablas de dimensiones:** Describen las entidades comerciales, es decir, las cosas que modela. Las entiedades pueden incluir productos, personas, lugares y conceptos, incluído el tiempo en sí. Una tabla de dimensiones contiene una columna (o columnas) clave que actúa como un identificador único y columnas descriptivas.

**Tablas de hechos:** Almacenan observaciones o eventos y, pueden ser ordenes de venta, saldos de existencias, tipos de cambio, temperaturas, etc. Contiene columnas de clave de dimensión que se relacionan con tablas de dimensión y columnas de medidas  numéricas.

Generalmente las tablas de dimensiones contienen un número relativamente pequeño de filas. Las tablas de hechos, por otro lado, pueden contener una gran cantidad de filas y continuar creciendo con el tiempo.

![Esquema_Estrella](Imagenes%20de%20relevancia/Esquema%20estrella.png)

Por cada registro que hay en una tabla de dimensión, le corresponden muchos en la tabla de hechos.

### Pasos

- Abrir los datos con los que se vaya a trabajar
- Ir a transformar datos
- Ir a la parte de consultas que aparece en el lado izquierdo, seleccionar la base
- Click derecho
- Seleccionar referencia, creará una segunda base idéntica a la primera sin ninguna relación
- Borrar las columnas que no interesan
- Seleccionar alguna de las columnas que se dejan
- Ir a quitar filas, desplegar, quitar duplicados
- Creará registros únicos

Ahora lo que sigue es relacionarlos, para esto ir a la tercera opción del lado izquierdo de la pantalla, generalmente la relación se dará automáticamente.

---

## Diferencia entre duplicado y referencia

- Duplicar crea una base exactamente igual, respetando cada consulta que se hizo en los pasos aplicados, sirve para realizar las mismas consultas a otra base, esto para cuando se requieran reutilizar las consultas.

- Referencia: Es necesario ir a la base original, click derecho y seleccionar referencia, solamente respeta la base salida, es decir a la cual se le aplicó la última consulta, pero no muestra los pasos aplicados. Usar la referencia es útil cuando se quieren realizar pasos o consultas posteriores a las que se le realizan a la consulta base.

---

## Tablas manuales

Tener en cuenta que se pueden crear máximo 3000 filas (o celdas)

- En la sección de inicio ir a la parte de especificar (o introducir) datos, en el apartado de datos, abrirá una interfaz para crear tablas, por default aparece columna 1
- En los *s se integra una columna o fila nueva
- Para editar el nombre, solamente se para sobre el nombre de la columna
- Una vez lista, darle click en editar y abrirá Power Query

---

## Index

**Como agregar una columna nueva de índica?**

- Cargar la base con la cual se vaya a trabajar
- Click en transformar datos, para ir a power query
- Verificar que el tipado de datos sea correcto
- Click en el menú agregar columna
- Columna de índice, desplegar el menú y aparecen 3 opciones
- Seleccionar la opción a convenir:
- desde cero, crea una columna de índice desde el cero hasta el último registro (n-1 registros)
- desde uno, crea una columna de índice desde el 1 hasta el último registro (n registros)
- Personalizado: decirle el índice el inicial y de cuanto va incrementando

---

## Columnas condicionales

- Cargar la base con la cual se vaya a trabajar
- Click en transformar datos, para ir a power query
- Verificar que el tipado de datos sea correcto
- Click en el menú agregar columna
- En la sección "General", seleccionar columna condicional. Aparece una ventana emergente
    - Poner el nombre de la columna
    - Los condicionales respectivos
- Cerrar y aplicar
- Solucionar los posibles errores que genere

---

# Query editor vs Data Model (Power Pivot)

No es necesario usar Power Query y Power Pivot. Son herramientas independientes y es posible que solo se necesite una u otra.

Power Query puede preparar conjuntos de datos simples pero grandes para el análisis. Power Pivot es para modelos mas complejos.

Aunque se pueden utilizar de forma independiente, estas dos herramientas se complementan. Power Pivot contiene características para importar y dar forma a datos, pero se recomienda dejar este trabajo a Power Query.

Luego, los datos se cargan en el modelo para que Power Pivot comience a establecer relaciones y a crear medidas mediante lenguaje DAX.

---

## Relaciones y cardinalidad

Lo primero es obtener los datos de la base a la cual se vaya a trabajar y luego, transformar datos.

En la tercera pestaña donde muestra las relaciones de las bases (modelo) se ve la base, si se quiere por ejemplo, tener una información específica para un dato, por ejemplo en qué sucursal bancaria está cada cliente .

Para lograr esto:
- Click en obtener datos
- Seleccionar la base con la cual se va a relacionar (uno a uno, uno a muchos, muchos a muchos)
    - Para editar esta relación, seleccionar la línea que conecta ambas tablas, esta se resaltará
    - Click derecho y da dos opciones (eliminar relación y propiedades). 
    - Seleccionar los campos que se quieran relacionar y listo

La cardinalidad es la relacion: Muchos a uno, uno a uno, muchos a muchos.

Esto se usa en el esquema tipo estrella.

---

# Lenguaje M vs DAX

Power BI admite dos idiomas diferentes, lenguaje M y DAX (Expresión de análisis de datos) que se pueden usar para filtrar, administrar y visualizar datos.

M se puede considerar como un lenguaje de fórmulas de consulta y se puede usar en el editor de consultas de Power BI para preparar los datos antes de que se puedan cargar en el modelo de Power BI.

Por otro lado, DAX es un lenguaje de cálculo de datos analíticos que se puede utilizar para un análisis de datos en profundidad durante la fase de visualización de datos.

M y DAX no dependen el uno del otro y siguen estructuras lógicas totalmente diferentes, y tienen códigos subyascentes diferentes. M y DAX no se pueden usar simultánreamente ya que el lenguaje M se usa en Query Editor, mientras que DAX se usa principalmente en el modelo de vista de datos.

---

## Cálculo DAX Columna

Para usar lenguaje DAX para calcular una columna:

- Obtener los datos e ir a transformar datos.
- Seleccionar la base en campos
- Seleccionar nueva columna
- Aparecerá una igualdad, del lado izquierdo se pondrá el nombre, del lado derecho se usa la expresión en dax (parecida a la de excel)
    
        **Ejemplo**: if(LogicalTest: que es una pregunta o un test lógico[columna]), ResultIfTrue: "Sentencia o resultado si es verdadero", ifFalse "sentencia o resultado si la sentencia es falsa")

        if(base_soc [deuda_act] == 0, "No presenta deuda", "Saldo mayor a cero")

Así aparecerá una nueva columna

## Cálculo DAX Indicadores

Para realizar un indicador con el lengüaje DAX:

- Obtener los datos e ir a transformar datos.
- Una vez obtenidos los datos que se necesitan aplicar cambios.
- Seleccionar la opción nueva medida ó medida rápida y se habilitará un cuadro de texto con una igualdad
    - En el lado izquierdo irá el nombre de la medida que se quiere tener.
    - En el lado derecho irá la base con la cual se va a trabajar y entre paréntesis las operaciones con las columnas que se están trabajando)

            **Ejemplo:**
            Porcentaje_pago = sum(nombre_bd[col1]) / sum (nombre_bd[col2])

Despues de presionar Enter para crear esta columna nueva, no se crea en la base sino en los campos, pero no la muestra como una columna nueva.

Para poder visualizar de forma rápida, se procede a meterla dentro de la visualización de matríz.

- Ir al apartado de gráficas
- En el apartado de visualizaciones seleccionar Matriz

![Matriz](Imagenes%20de%20relevancia/Gráfico%20Matriz.png)

- Seleccionar el campo creado (porcentaje de pago en este caso) y arrastrarlo al apartado Valores

---

## Calculate

![Calculate](Imagenes%20de%20relevancia/Funcion%20calculate.png)

**Los filtros pueden ser:**
- Expresiones de filtro booleano
- Expresión de filtro de tabla
- Funciones de modificación de filtros

**Expresiones de filtro booleano:**
Un filtro de expresión booleana es una expresión que se evalúa como VERDADERO o FALSO. Hay varias reglas que se deben cumplir:
- Pueden hacer referencia a columnas de una sola tabla.
- No pueden hacer referencia a medidas.
- No pueden usar una función CALCULAR anidada.
- No pueden usar funciones que escanean o devuelven una tabla, incluidas las funciones de agregación.

**Expresiones de filtro de tabla:**
Un filtro de expresión de tabla aplica un objeto de tabla como filtro. Podría ser una referencia a una tabla modelo, pero es más probable que sea una función que devuelve un objeto de tabla. Puede utilizar la función FILTRO para aplicar condiciones de filtro complejas, incluidas auqellas que no se pueden definir mediante una expresión de filtro booleana.

**Funciones de modificación de filtro:**
Permiten hacer más que simplemente agregar filtros, Porporcionan un control al modificar el contexto del fiultro

## Calculate on all

All es una modificación de filtro sirve para ignorar algunos filtros o todos los filtros, dependiendo el tipo de all que se utilice.

- Cargar la base de datos con la cual se va a trabajar, click en transformar
- Hacer la depuración correspondiente y dejar las columnas con las cuales se quiere trabajar.
- Crear una visualización de Matriz, seleccionar Matriz
    - Llenar el campo de filas de la matríz con los valores requeridos
    - Llenar el campo de valores de la matriz para que segmente por tipo de cliente.

**Como ejemplo se trabajará con la tabla b_tipo_soc**

- Conservar las columnas id_cliente,venta trimestral, tipo_cliente y sucursal
- Cerrar y aplicar y se podrá visualizar de lado de campos
- Crear una visualización de Matriz
- Para que segmente por tipo de cliente, se arrastra este campo a filas
- Para segmentar la venta trimestral, se pone en valores

**NOTA**
---
Para que la fuente se vea un poco más grande, seleccionar el rodillito de visualización (o click en el pincel que indica visualización), ir al apartado de valores y ajustar el tamño del texto en caso de ser necesario, igual que los encabezados de columna y de fila y también se puede seleccionar el tipo de fuente.

Y para cambiar el formato de un campo dando click sobre el campo que se desea cambiar, en la parte de arriba, en herramienta de tablas se verá que se habilita formato, se selecciona el que se desee y se va a actualizar instantáneamente. En este caso se selecciona el formato moneda.

---

Se desea ver que porcentaje de la venta total consumió cada tipo de cliente, entonces, para esto se crea una nueva medida usando calculate con all, esto servirá para ignorar u obtener el valor de la venta trimestral total.

- Ir a la pestaña de inicio, sección cálculos, seleccionar nueva medida
- Del lado izquiero de la igualdad irá el nombre de la medida, el cual será PORC_VTIM_TIPOCLIENTE (Porcentaje valor trimestral tipo de cliente)

        PORC_VTIM_TIPOCLIENTE = SUM(B_tipo_soc[venta_trimestral]) / CALCULATE(SUM(B_tipo_soc[venta_trimestral]), ALL(B_tipo_soc))

En este ejemplo no importa que se ignore todo, ya que el único filtro que se tiene es el tipo de cliente.

Una vez ejecutado, notar que en Datos se crea PORC_VTIM_TIPOCLIENTE, arrastrarlo al campo de valores y se podrá ver el porcentaje de participación de cada tipo de cliente

**Segundo ejemplo**
---

se agrega un nuevo filtro a la parte de filas de la matriz, el cual será el nombre de la sucursal, aparece un signo + para poder ver la sucursal de cada tipo de cliente y mostrará los valores por cada sede

Si se quiere ver el porcentaje de participación de cada tipo de cliente respecto a la tienda

Para esto, se crea una nueva medida
- Ir a la pestaña de inicio, sección cálculos, seleccionar nueva medida
- Del lado izquiero de la igualdad irá el nombre de la medida, el cual será PORC_REPRE_SUC (Porcentaje representativo por sucursal)

        PORC_REPRE_SUC = SUM(B_tipo_soc[venta_trimestral]) / CALCULATE(SUM(B_tipo_soc[venta_trimestral]), ALL(B_tipo_soc[tipo_cliente]))

Se ignora el filtro de tipo de cliente, porque se quiere que la venta total de tipo de cliente se verá afectada por tipo de cliente y por sucursal, pero la segunda expresión se verá afectada por el tipo de sucursal, es decir que sume la venta trimestral ignorando el tipo de cliente 

Una vez creada esta medida, se procede a arrastrar al campo de valores.

Esto mostrará el porcentaje de participación por tipo de cliente en cada ciudad.

**All Except**

Es una variante del tipo de filtro all, ignora todos los campos excepto el que se está mencionando.

---

## Calculate on filter

Se trabajará con el ejemplo anteriormente creado con calculate.

Ahora lo que se quiere es obtener la venta trimestral obteniendo la visualización tipo card o tarjeta con la venta trimestral para los clientes tipo oro, otra con la venta trimestral para los clientes tipo oro que pertenezcan a la sucursal de OAX y otra con la venta trimestral con los clientes tipo oro que pertenezcan a PUE o QRO..

Para esto se usa la función calculate con filter

- Ir a cálculos, nueva medida
- Del lado derecho el valor es VTRIM_CLIENTESORO (Venta trimestral clientes oro)
        
        VTRIM_CLIENTEORO = CALCULATE(SUM(base_soc[venta_trimestral]), base_soc[tipo_cliente] == "Cliente Oro")

- Ir a la visualizaciones, seleccionar tarjeta y agregar el campo creado y debe coincidir con la que está en la matriz.

Aquí se usa la función filter, debido a que la visualización que se requería era una tarjeta.

Ahora se usará otra tarjeta para los clientes tipo oro que pertenecen a la sucursal de guajaca (OAX)

- Ir a cálculos, nueva medida
- Del lado derecho el valor es VTRIM_ORO_OAX (Venta trimestral clientes oro de la sucursal de guajaca)

        VTRIM_ORO_OAX = CALCULATE(SUM(base_soc[venta_trimestral]), base_soc[tipo_cliente] == "Cliente Oro" && base_soc[nombre_suc] == "OAX")


Y ara Puebla o Queretaro:

    VTRIM_ORO_PUE_QRO = CALCULATE(SUM(base_soc[venta_trimestral]), base_soc[tipo_cliente] == "Cliente ORO" && (base_soc[nombre_suc] == "PUE" || base_soc[nombre_suc] == "QRO"))

---

## Funciones: Sum, Divide, Count, Average, Max, Win

**Función Sum**

Solo requiere el campo de la columna el cual va a sumar, debe ser de tipo no caracter (numérico de preferencia) y seguir estos pasos:

- Ir a nueva medida en la pestaña de inicio y dar click en nueva medida
- Poner el nombre del campo al lado derecho
- Poner la función sum con la tabla y la columna que se quiere sumar del lado derecho

**EJEMPLO**

        SUMA_VTRIM = SUM(base_soc[venta_trimestral])

**Función Count**
Cuenta una cantidad específica de un campo

**EJEMPLO**

        Conteo_Clientes = COUNT(base_soc[id_cliente])

**Función promedio**

Se usa la función divide para sacar promedio y se dividirá la venta trimestral entre los clientes.

**EJEMPLO**

    Promedio de venta trimestral por cliente:

    Prom_VTRIM_Cliente = DIVIDE([SUMA_VTRIM],[Conteo_Clientes],0)

    Promedio de venta por cliente
    AVG_VTRIM = AVERAGE(base_soc[venta_trimestral])

**Función MAX y MIN**
Para mostrar el valor máximo y el mínimo de un campo

**EJEMPLO**

        Para el máximo:
        MAX_VTRIM = MAX(base_soc[venta_trimestral])

        Para el mínimo:
        MIN_VTRIM = MIN(base_soc[venta_trimestral])

---

## Dax Fechas

![Fechas](Imagenes%20de%20relevancia/DAX%20Fechas.png)

- **Función Calendar**: Devuelve una tabla con una sola columna denominada "Fecha" que coniene un conjunto contiguo de fechas

- **Función Calendarauto**: Devuelve una tabla con una sola columna denominada "Fecha" que contiene un conjunto contiguo de fechas

- **Función Date**: Devuelve la fecha especificada en formato de fecha y hora

- **Función Datediff**: Devuelve el recuento de límites de intervalo cruzados entre dos fechas.

- **Función DateValue**: Convierte una fecha en forma de texto en una fecha en formato fecha y hora

**Calendar y calendarauto**

La función Calendar sirve para devolver una secuencia de fechas y recibe como parámetro la fecha mínima y máxima (inicio y fin). Entre estas fechas saca una frecuencia o una secuencia de fechas que serán continuas e irán limitadas por una fecha inicio y  una fecha fin.

Se usa cuando se quieren obtener fechas únicas de un campo, y se usan normalmente para crear una nueva columna  y formar el esquema estrella.

Lo primero para trabajar con estas funciones es cargar la base y hacer su respectiva limpieza.

**Para calendar:**
---
- Ordenar la fecha en forma ascendente
- Crear una nueva tabla
    - Ir a herramientas de tablas
    - Nueva tabla, llamarla tabla 1 = Calendas(fecha de inicio, fecha fin)
            
            Tabla1 = CALENDAR(MIN(base_pagos[fecha]),MAX(base_pagos[fecha]))

        Creará una nueva tabla con las fechas de la máxima a la mínima sin repetirse para los datos que se crearon el mismo día

**Para calendarauto**:
---

Automáticamente selecciona el campo fecha de la base pagos y creará una secuencia.

- Click en la base
- Click en crear nueva tabla
- Abre una igualdad; a la izquierda el nombre de la tabla y a la derecha el calendar auto
    - Si no se le dan parámetros tomará la fecha inicial y creará una tabla de todos los días del año
    - Si se le da un parámetro (solo recibe parámetros del 1 al 12) ignora el mes del parámetro que se le da, es decir ignora el parámetro que se le da hasta el siguiente mes teniéndolo en cuenta para el año entrante.

La aplicación mas práctica es para poder obtener el modelo estrella  y optimizar el modelo.

**Función DatesYTD**:
---

Lo primero que se hace es cargar la base y hacer su limpieza.

Funciona de igual forma que la función Calendar, crea una secuencia con valores únicos a partir de un campo de fecha

- Crear una nueva tabla
- Ponerle su nombre y llamar a la función dateytd, recibe un parámetro obligatorio, el cual es datesytd
        
        Tabla3 = DATESYTD(base_pagos[fecha])

    Creará una nueva tabla con valores únicos con base a la información que suministró en el campo fecha de la base.

    Esta no es su función principal, puesto que dicha función principal es poder obtener el acumulado a partir de una variable numérica y realizar el acumulado fecha por fecha a partir de un campo por fecha.

Crear una visualización de esta tabla en la matriz.

Poner la fecha en el valor filas y los valores que se le quieran dar en el valor valores.

Apoyándose en la función datesytd para ir calculando el acumulado del día 1 hasta el día 29

- Crear una nueva medida, ponerle el nombre y en los valores con la función calculate y pide como parámetros la expresión, será la suma de la columna que se calcula y se filtra usando la función datesytd diciéndo que lo filtre por el campo de fechas de la base pago y así irá creando el acumulado.

        DATESYTD = CALCULATE(SUM(base_pagos[pgo_tot]), DATESYTD(base_pagos[fecha]))

    Una vez creada la medida, arrastrarla a la parte de valores.

    Esta función tiene un parámetro opcional hasta cierto día poniéndo una coma y la fecha YYYY-MM-DD

        ,"YYYY-MM-DD"

**TotalYTD**
---

Evalúa una expresión especificada a lo largo del intervalo que empieza el primer día del año y temrina con la última fecha de la columna de fecha especificada, después de aplicar los filtros especificados, trae 2 parámetros obligatorios y 2 opcionales.

El primer parámetro obligatorio es una expresión (suma, resta, etc).

El segundo parámetro es dates, el cual recibe una columna o una expresión de tipo fecha

El tercero da opción de filtrar, como se hace en calculate

El cuarto es donde queremos que termine el acumulado y empiece otra vez

**EJEMPLO**

- Una vez se tenga la tabla, se creará una nueva medida en la parte de cálculos en la pestaña de inicio.

        YTD = TOTALYTD(SUM(base_pagos[pgo_tot]),base_pagos[fecha])


**Dates in period**
---

Devuelve las fechas de un periodo especificado; recibe 4 parámetros obligatorios, los cuales son:

- Fechas: fechas de las cuales tomará como referencia
- Fecha de inicio: de las fechas que se da como referencia, en cual se quiere que inicie
- Número de intervalos: Número de intervalos a partir de la fecha de inicio, por ej; si se pide que inicie del 1 de abril del 2023 y que vaya de 1 en 1 en el # de intervalos por día irá uno a uno hasta terminar con el último valor del campo dates (primer parámetro).

    El número de intervalos se puede dar en positivo y negativo; si se da en positivo será desde la fecha de inicio hacia adelante, si se da negativo será de la fecha de inicio hacia atrás, depende del intervalo que se de, puede ser de día, mes o año.

- Intervalo deseado

Una vez cargada la tabla con la que se va a trabajar, crear una nueva medida

**EJEMPLO**

Obtener una medida la cual calcule un acumulado de pagos de 3 en 3 días hacia adelante y hacia atrás.

- Hacia adelante:

        DIP_ADELANTE = CALCULATE(SUM(base_pagos[pgo_tot]), DATESINPERIOD(base_pagos[fecha],MIN(base_pagos[fecha]),3,DAY))

- Hacia atrás:

        DIP_ADELANTE = CALCULATE(SUM(base_pagos[pgo_tot]), DATESINPERIOD(base_pagos[fecha],MIN(base_pagos[fecha]),-3,DAY))

Si en el parámetro start date se le da una fecha anterior a la fecha mínima del campo, lo va a ignorar, debido a que ese valor no se encuentra en la columna, es decir, siempre empezará en la primer fecha de la columna así se le dé una fecha anterior.

---

## Total acumulado

En esta parte del curso se aprenderá a tener un total acumulado manejando las fechas y realizando algunos filtros con ella.

En este caso se puede usar la función filter la cual devuelve una tabla filtrada.

La función filter recibe 2 argumentos

- El primer argumento recibe la tabla.
- El segundo las expresiones de filtrado.

**EJERCICIO**

Realizar un acumulado de pagos totales.

- Cargar y depurar la base con la cual se va a trabajar.
- Crear una nueva medida

        Medida1 = CALCULATE(SUM(base_pagos[pgo_tot]),FILTER(ALLSELECTED(base_pagos),base_pagos[fecha]<=MAX(base_pagos[fecha])))

- Ir a la parte de visualización y crear una matriz para poder verlo de mejor forma

    - Arrastrar en campo fecha a filas
    - Pagos totales a valores
    - Medida a valores

---

## DATEADD

Dateadd recibe 3 argumentos
- Dates: es el campo de fechas
- Número de intervalos que se desplazará hacia adelante o hacia atrás
- Intervalo o tipo de intervalo: es en el cual se va a desplazar el número de intervalos por un tipo, ya sea por día, mes, semestre o año

Después de cargar la base con la cual se va a trabajar.

El objetivo será desplazar los pagos una fecha o un día siguiente y uno hacia atrás.

Para esto se apoya de la función calculate con la función date add y se visualizará en una matríz.

    Para desplazar hacia atrás:
    Medida1 = CALCULATE(SUM(base_pagos[pgo_tot]), DATEADD(base_pagos[fecha],-1,DAY))

    Para desplazar hacia adelante:
    Medida1 = CALCULATE(SUM(base_pagos[pgo_tot]), DATEADD(base_pagos[fecha],1,DAY))

---

## Tablas de tipo calendario

Es una tabla que contiene columna o columnas de fecha y derivados de esta.

La práctica de estas va a optimizar el modelo y se podrá utilizar el lenguaje DAX de una forma más avanzada.

Los requisitos para usarla principalmente es que los campos de tipo fecha ventan únicos (debe ser único y no se puede repetir)

Para hacer la tabla:

- Abrir la base
- Ir a la parte de modelado, en el apartado de cálculos
- Click en nueva tabla
    - Poner el nombre de la tabla 
    - Para los valores usar la función calendar

            Tabla1 = CALENDAR(MIN(base_pagos[fecha]),MAX(base_pagos[fecha]))

        Con esto creará fechas únicas que abarca todas las fechas que vienen en la base con la que se trabaja.

- Para poder convertirla en una tabla de tipo calendario
- Seleccionar la tabla, ir a herramientas de tabla
- En la sección de calendarios click en  marcar la tabla como fechas.
- Desplega un menú donde dice se selecciona la columna de fecha donde pide los requisitos

Después de seguir esos pasos, cambia el formato de esa tabla y será de tipo fecha.

Ahora se pueden crear los campos, como el día de la fecha, el mes de la fecha y el año, de la siguiente manera:

Para el año:

- Seleccionar la tabla, nueva columna
- Poner el nombre = year(-nombreTabla[Date])
        
        Año = YEAR(Tabla1[Date])

Para el día:
- Seleccionar la tabla, nueva columna
- Poner el nombre = day(-nombreTabla[Date])

        Día = DAY(Tabla1[Date])

Para el mes:
- Seleccionar la tabla, nueva columna
- Poner el nombre = month(-nombreTabla[Date])

        Día = month(Tabla1[Date])

- Semana del año:
- Seleccionar la tabla, nueva columna
- Poner el nombre = weelmi,(-nombreTabla[Date])

        Semana_Año = WEEKNUM(Tabla1[Date])

---

## Variables DAX

Las variables en DAX son muy usadas, debido a que es una forma de usar DAX de forma estructurada, la cual ayudará a mejorar el rendimiento, es más fácil depurar cuando están las variables definidas, se mejora la comprensión al momento de saber lo que se está realizando y disminuye la complejidad.

**EJERCICIO**

Obtener los pagos acumulados de la segunda semana de diciembre a los cuales se les restarán los pagos acumulados de la primera semana de diciembre y se van a dividir entre los pagos acumulados de la primera semana de diciembre para ver en qué porcentaje aumentan o disminuyen los pagos en la segunda semana de diciembre respecto a la primera.

- Crear una matriz


Si se crea una nueva medida así:

        Medida1 = DIVIDE(CALCULATE(SUM(base_pagos[pgo_tot]), DATESINPERIOD(base_pagos[fecha],DATE(2020,12,08),7,DAY)) - CALCULATE(SUM(base_pagos[pgo_tot]),DATESINPERIOD(base_pagos[fecha],MIN(base_pagos[fecha]),7,DAY)),CALCULATE(SUM(base_pagos[pgo_tot]),DATESINPERIOD(base_pagos[fecha],MIN(base_pagos[fecha]),7,DAY)),0)

Es un poco complicado de hacer, difícil de entender y no es lo óptimo

Si se desea hacer usando una variable:

Crear una nueva medida y hacer lo siguiente:

    variable1 = VAR PAGOS_SEMANA1 = CALCULATE(SUM(base_pagos[pgo_tot]),DATESINPERIOD(base_pagos[fecha],MIN(base_pagos[fecha]),7,DAY))
    VAR PAGOS_SEMANA2 = CALCULATE(SUM(base_pagos[pgo_tot]),DATESINPERIOD(base_pagos[fecha],DATE(2020,12,08),7,DAY))
    RETURN DIVIDE(PAGOS_SEMANA2 - PAGOS_SEMANA1,PAGOS_SEMANA1,0)

Así es más fácil de trabajar y mejora el rendimiento ya que solo se calculan una vez los pagos de la semana uno y semana dos

---

## Categorización de datos

Sirve para mejorar la experiencia al momento de realizar visualizaciones, ya que Power BI va a interpretar de una manera en la que se categoricen estos datos.

Para poder visualizar la categorización de datos es necesario:

- Seleccionar el dato o el campo al cual se le va a hacer dicha categorización.

- En el apartado propiedades, donde dice categoría de datos aparece sin clasificar y seleccionar el valor correcto.

---


# Report View

La interfaz en la parte de la visualizaciones es la que ayuda a crear gráficos y se conoce como report view, ahí se pueden encontrar los gráficos predeterminados que ofrece Power BI.

**Primera visualización**

Crear una visualización donde se muestre día por día los pagos que se han realizado por el tipo de cliente en una barra apilada, es decir, todas tendrán la misma altura y estará segmentado dependiendo del porcentaje del tipo de cliente en los pagos

**Interacción y tooltips**

Tooltips es información sobre herramientas, los cambios que se necesiten hacer irán directamente en el apartado de información sobre herramientas.

Si se quiere poner un campo adicional, entonces solamente se arrastra y ya; esto sirve para que al pasar el mouse por cierta parte de la gráfica muestre información.


**Tootips avanzados**
Un tooltip avanzado se diferencia del normal en que muestra la información sobre la gráfica y abrirá una nueva gráfica con información sobre la herramienta.

**EJERCICIO**
Crear  una gráfica de barras donde se muestre la sucursal y la venta trimestral y al poner el mouse sobre la barra perteneciente a la venta trimestral de alguna sucursal, debe desplegar como info de la herramienta o tooltip la composición de la venta trimestral (enero, febrero y marzo)

Pasos:

- Cargar la tabla con la que se va a trabajar.
- Crear un gráfico de columnas agrupadas o apiladas
- En el eje x colocar el nombre de las sucursales y en el y la venta trimestral.
- Mostrar las etiquetas de los datos desde el formato
- Agregar el tooltip básico de enero febrero y marzo, simplemente arrastrando los campos que se quieren consultar directamente en el apartado de información sobre herramientas.
- Para lograr hacer un tooltip avanzado:
    - Crear una nueva página y renombrar como tooltip1
    - Cambiar el tamaño de página a información sobre herramientas y dará un tamaño a como se verá en el informe o la página 1
    - Seleccionar la gráfica de barras agrupadas o apiladas
    - Activar el tooltip
        - Seleccionar afuera del gráfico, en la página
        - En configuración de lienzo seleccionar en el apartado tipo información sobre la herramienta
    - Ahora para que muestre el tooltip avanzado sobre la gráfica:
        - Click sobre la gráfica
        - Ir a formato
        - Click en propiedades
        - Información sobre herramientas
        - En página seleccionar tooltip1

---

## Jerarquía, drill down and drill  up

Una jerarquía es aquella que divide o segmenta los artículos en diferentes grupos.

**EJERCICIO**
Para crear una jerarquía con base a las fechas, teniendo como jerarquía la semana del año y la segunda jerarquía la fecha.

- Crear una gráfica la cual será columna agrupada
- Poner pago total en el eje Y
- Crear la jerarquía con base a semana del año.
    - Pararse sobre el campo al cual se le creará la jerarquía, click derecho y crea unos iconos del lado izquiero a la jerarquía
    - Para agregar campos a la jerarquia click derecho sobre el campo y guardarlo en la jerarquia

Para hacer el drill down y el drill up; en la gráfica aparecen 2 botones para ir cambiando de jerarquía, la flecha hacia arriba es para subir en la jerarquía, las dos flechas hacia abajo es para bajar de jerarquía

---

## Ordernaciones

Si se trabaja con un gráfico de barras, el eje x debe ser de tipo categórico para que pueda habilitar la ordenancia y se pode ordenar de manera ascendente y descendente

---

## Slicer

Es un tipo de filtro que permite filtrar los objetos de visualizaciones o bases a través de este campo.

Para hacer esto:

- Cargar las tablas con las que se vaya a trabajar
- Hacer la relación correspondiente entre ids
- Pasar al apartado de gráficos
- Seleccionar el tipo de dato segmentación de datos, este es un filtro llamado Slicer
- Agregar el campo por el cual se quiere filtrar
- Para que quede como un menú desplegable ir a los estilos (formato)
    - selecciona configuración de la segmentación
    - Seleccionar el estilo menú desplegable

Para darle formato al Slicer
- Quitar el encabezado
- Agregar título y ponerlo como corresponda
- Centrarlo
- Modificar el formato de los elementos (datos que aparecen cuando se despliega el menú, es decir, datos a filtrar)

Ahora hace filtros por los elementos de la sucursal.

- Agregar un gráfico nuevo
- En el eje X poner los nombres con los cuales se hicieron los filtros 

Y así cualquiera que se seleccione, mostrará su gráfico correspondiente

**Sincronizar Slicers**
---

Primero crear la(s) gráfica(s) con la(s) que se desee trabajar (recordar poner el eje x como tipo categórico)

Luego agregar los slicer (son 2)
- Un slicer para campo de fecha
- Otro para tipo de cliente

En este momento, los dos filtros afectarán las visualizaciones, para hacer que no afecte alguna se hace esto:

- Seleccionar el slicer
- Ir al menú de formato (parte superior, centro de la pantalla)
- Click en editar interacciones
- Elegir a qué objetos visuales afectará y a cuales no este filtro. Para decirle que no afecte a un filtro en específico se le da click en el ícono de prohibido que tiene


**Tipos de filtros**
---

Al seleccionar la visualización sobre la cual se aplicará el filtro.

Hay 3 opciones
- **Filtro de este objeto visual**: Solo afectará al filtro del objeto visual seleccionado
- **Filtro de esta página:** los filtros o filtro agregado afectará a todos los objetos visuales de la página
- **Filtro de todas las páginas:** Afectará a todas las páginas, de la 1 hasta la página n

---

## Top /Bottom

- **Top**: es una herramienta que permite filtrar por categoría, para obtener las mejores categorías con base a una expresión, puede ser promedio de ventas, ventas totales, ventas mensuales, trimestrales, pagos, etc..
- **Bottom**: Es lo contrario al top, es la herramienta que permite segmentar las peores categorías, o las categorías que han tenido menos relevancia con base a la expresión, puede ser promedio de ventas, ventas totales, ventas mensuales, trimestrales, pagos, etc..

**Para hallar el top:**
- Crear una nueva medida
- Poner el nombre de la medida
- Enumerar por orden ascendente, dependiendo la venta trimestral de cada sucursal, es decir la que tenga mayor venta como # 1 y la de menor venta como número n
- Usar la función rankx la cual devuelve la clasificación de una expresión evaluada en el contexto actual de la lista de valores para la expresión evaluada por cada fila de tabla especificada. 

    Rankx recibe 5 argumentos (2 obligatorios y 3 opcionales):
    - tabla a la cual se le hará el análisis
    - Expresión (calculate, sum, etc)
    - Argumento de valor (se utiliza cuando se quiere comprar la venta trimestral contra este valor)
    - orden (asc o desc)
    - Ties ( si se repiten 2 sucursales con la misma venta las toma como valores diferentes)

**NOTA**
---
Como para el ejercicio trabajado en el archivo "top" se quieren , entonces se le dice que ignore de la base todos los filtros correspondientes a la columna de sucursal, porque se va a mostrar con una matriz y se quiere que lo compare con el total de la venta, si no se pone el filtro de "ALL" lo va a comprar con la venta de cada sucursal, es decir, siempre dará el valor de 1

Entonces, el código DAX quedaría así:

    Top = RANKX(ALL(base_soc[nombre_suc]),CALCULATE(SUM(base_soc[venta_trimestral])),,DESC,Dense)

RankX devuelve una lista de números en la cual el 1 corresponde a la mayor venta, porque se puso que ordenara descendentemente, y teniendo como menor venta el nombre sucursal sin clasificación

**Para hallar el bottom:**

Para enumerar a partir de la venta menor es algo similar, con la diferencia que el orden en vez de desc se pone como asc:

    Top = RANKX(ALL(base_soc[nombre_suc]),CALCULATE(SUM(base_soc[venta_trimestral])),,DESC,Dense)

Ahora, si se quieren mostrar el top 3 de sucursales que mas han vendido y que menos han vendido en una matriz a parte, se hace lo siguiente:

- Crear una nueva medida

        TOPBOTTOM = IF([Top]<=3 || [bottom] <= 3, 1, 0)

- Arrastrar la medida para asegurarse que haya quedado correcto: 

![top-bottom](Imagenes%20de%20relevancia/top_bottom.png)

- Para poder mostrar las que tuvieron mayor y menor venta en una matriz, basta con crear una nueva matriz,

- arrastrar el nombre de la sucursal a las filas
- Arrastrar el valor de la sumatoria de la venta trimestral a los valores 
- Filtrar este objeto visual con la medida creada, arrastrando la medida hacia el filtro y ponerlo así:

![filtro](Imagenes%20de%20relevancia/filtro.png)

- Finalmente dar click en agregar filtro.

---

# Gráficos
---

**Gráfico de columnas y gráfico de columas 100% apilado o agrupado**

El gráfico de columnas sirve para graficar o mostrar los resultados de una expresión dividido en un eje x; puede ser por categorías o contínuo

**Gráfico circular**

Es conveniente usarlo cuando hay menos de 7 categorías para interpretar fácil los datos

**Gráfico de líneas**

Sirve para visualizar una o más expresiones a través de un eje x, es decir, el eje x puede ser continuo o categórico, es recomendable usar el gráfico de línea casi siempre para mostrar en el eje x un tipo de eje x contínuo.

Sirve para calcular o visualizar una historia; puede ser historico de pagos, ventas, etc.

Las fechas pueden ser anuales, trimestrales, diaras, semanales, etc.

También se pueden dividir en categorías.

**Gráfico de área**

Es similar a un gráfico de líneas, con la diferencia que para cada valor del eje x va a iluminar las partes o valores debajo de este, de ahí su nombre.

El gráfico de área apilada sirve para comparar entre diferentes categorías, es decir, del eje x se traza una expresión (sumatoria, promedio u otra operación artimética) y se podrá comparar con otras categorías, también se puede comparar entre fechas o entre año o meses.

**Gráfico de dispersión**

Es un tipo de gráfico que permite graficar en dos dimensiones, es decir, con base en el eje X y en el eje Y, va a buscar las coordenadas correspondientes del eje x y las va a graficar en el punto (X,Y)

Son muy útiles para visualizar datos atípicos, también se puede visualizar la correlación o la relación entre dos variables.

Permite pasar del gráfico de dispersión a uno de burbujas, en el cual, cada burbuja tendrá un tamaño con respecto a otra variable.


**Objeto de visualización tipo tabla**

Sirve para obtener un resumen de valores numéricos.

Se le pueden agregar valores categóricos, sin embargo no será correcta la interpretación con respecto a lo que muestra

**Gráfico de matriz**

A diferencia del tipo tabla que solo se especializa en recibir valores o columnas numéricas y obtener un resumen a partir de ellas, la matriz tiene a parte de eso, poderlo segmentar por filas y columnas, estas normalmente suelen ser variables tipo categórico, es decir, se puede ver una mejor distribución de estas variables categóricas respecto a las expresiones o campos numéricos.

**Gráfico de línea y columna**

Es un objeto de visualización de PowerBI que permite combinar estos dos tipos de gráficos en un solo. Es ideal cuando se quieren comparar dos variables o expresiones que tienen rangos muy distintos; es decir, si se trazan en un mismo eje no va a poder compararse o apreciarse bien la diferencia entre esto, debido a que uno tiene una escala y otro tiene una escala distinta

**Gráfico de embudo**

(Pendiente el gráfico)

Es un objeto de visualización que permite analizar diferentes variables de importancia, ya sea pagos, venta, recuento de clientes, a través de un proceso que debe ser secuencial, es decir no se puede pasar a la parte 2 del proceso sin antes haber pasado la parte 1.

También se recomienda usar cuando se tiene al principio del proceso la mayor cantidad de datos y al final del proceso una menor cantidad de datos.

**Treemap**

Es un gráfico que ofrece herramientas parecidas a un gráfico por columnas, pero es más fácil poder apreciar las jerarquías sin necesidad de hacer un drill up o drill down para profundizar en los datos.

Ofrece lo mismo, pero muestra de mejor forma que un gráfico de columnas las jerarquías.

También ordena de mayor a menor, teniendo en la parte superior izquierda el valor o promedio mas grande y en la inferior derecha el más pequeño.

**Tarjeta**

Este objeto permite mostrar únicamente un valor. A veces es importante hacer seguimiento a solo un valor de interés; puede ser el valor de la venta anual, total de la venta por mes, venta trimestral, etc. Pero solo se quiere ver el valor.

**Map**

Es una visualización que ofrece publicar mediante geolicalización un par de coordenadas que se le den o una dirección.

Es útil cuando se requiere ver la distribución por zona geográfica de los clientes o de los pagos o cualquier valor de interés

**KPI**

Indicador que permite saber que tan lejos estamos o donde nos encontramos con base a una meta u objetivo trazado.

Es útil para darle seguimiento contínuo con base a una meta.

**Filtros en gráficos**

Permite realizar segmentaciones o escoger ciertos valores de un campo que solo afectarán a este objeto visual

**Formato condicional en matriz**

Es el formato que aparece mediante ciertas condiciones, es decir, solo se muestra después de que pasen un conjunto de reglas.

- Después de crear la matríz, ir a la parte de formato, está el apartado formato condicional.

**Formato condicional en gráficos**

Funciona parecido al de matriz, se intentará resaltar la parte de la gráfica donde se tenga un número mayor o menor.

**Roles y seguridad**

- Rol: Conjunto de reglas o filtros predeterminadas que se le dan al informe para que lo vea determinado usuario.

- Seguridad: Determinar los roles al usuario.

*Para crear un rol:*

- Ir a modelado
- Administrar roles
- Crear
- Poner el nombre del rol
- Seleccionar la tabla de donde se sacará la expresión de este filtro
- Poner la expresión DAX del filtro de tabla
    - Para que DAX entienda que es un campo se pone en corchetes, ejemplo
        [nombre_sucursal] == CDMX
    - Guardar
- Ir a modelado, seguridad ver como
- Se puede ver el perfil de acuerdo al rol, ahora se aplica el filtro para todos los objetos visuales solo para el campo seleccionado
- Ir a inicio, publicar y publicará el informe en el área de trabajo
*Para administrar la seguridad o asignar los roles al usuario*

- Abrir el navegador
- Ingresas a la app de power bi
- Enviar el trabajo donde se debe tener publicado el informe anteriormente
- Ir a la parte de la base de datos
- Seleccionar los 3 puntos
- Click en seguridad y aparecen los roles
- Asignar a las personas o gurpos que pertenecerán a este rol. Agregar la dirección de correo electrónico de la persona que tendrá los permisos para ver este rol

