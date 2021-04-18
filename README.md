# dj-traffic
Conteo de autos para el control de semáforos diseñado en python y arduino
Dj-traffic es un proyecto basado en Django y Arduino que permite integrar un semáforo hecho con arduino. La aplicación en python se conecta directamente al arduino por el puerto serial, permitiendo controlar de acuerdo al conteo que realiza de autos la librería OpenCV utilizando visión computacional y calcular el lado del semáforo con mayor tráfico y decidir los tiempos para alivianar la carga vehicular.

Además, las cámaras IP conectadas al programa **<vehicle_server.py>** se visualizarán en el el servidor desarrollado en Django para la visualización de reportes, cámaras y manupulación de datos sobre los vehículos, los cambios del semáforo, entre totros.

Antes de correr las aplicaciones, realizar un semáforo sencillo con cualquier tipo de arduino que soporte la conexión serial por puerto USB, luego, subir el script de la carpeta **<arduino_semaforo>** y probar que el semáforo funciona de forma automática.

Para ejecutar Dj-traffic debemos configurar el script vehicle_server.py con la siguiente información:
 **host1 = '192.168.1.10' # Coloar ip de la cámara 1**
 **host2 = '192.168.1.10' # Coloar ip de la cámara 2**

Para probar las cámaras puedes utilizar IP Webcam disponible en PlayStore para Android.

 Nota: Se puede testear con los videos incluídos en el repositorio.

Luego de configurar las IP de las cámaras, configuramos la variable **<ser>** con el puerto serial del arduino

**ser = get_serial('COM4') #Dond COM4 es el puerto serial local de mi arduino**

Probar si se comunica correctamente con el semáforo en arduino y de ser así, pasar al siguiente paso.

Ahora instala los requerimientos de python en tu ambiente virtual utilizando el archivo requirements.txt

**pip install -r requirements.txt**

Por último correr la aplicación en django ejecutando "run server 0:80" en el archivo **<manage.py>**

**python manage.py runserver 0:80**

Accesar a la ruta *http://localhost* y visualizar el sistema

Si tienes problemas con la instalación del proyecto, comunicate conmigo al correo *4c1dhydr4@gmail.com*


