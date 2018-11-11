#Despliegue de mi app en Heroku.

En este documento voy a explicar cómo realizar un deploy a los servidores de Heroku de mi proyecto web desarrollado con Python. Lo he dividido en tres pasos, que son los siguientes:

    1. Creación de un entorno virtual.
    2. Creación de los archivos necesarios para el deploy.
    3. Realizar el deploy propiamente dicho.

1.Preparación del entorno.
1.1. Creación de un entorno virtual para nuestro desarrollo aislado.

Desde una terminal creamos un nuevo directorio llamado “project”, donde crearemos el entorno de desarrollo. Para ello, necesito apoyarme de la herramienta de virtualenv la cual hace que cada proyecto sea independiente con respecto a los paquetes que necesita.

Para instalar virtualenv, he ejecutado el siguiente comando en mi terminal:

pip install virtualenv

Una vez instalado en mi equipo, cuando queremos crear un nuevo entorno, escribimos lo siguiente en la terminal que estamos utilizando.

virtualenv project

Esperamos un par de segundos a que se cree nuestro entorno, y ya tenemos la carpeta llamada “project”. Cuando queremos ejecutarlo, basta con escribir lo siguiente:

. project/bin/activate

Este entorno está completamente vacío y no tiene ningún paquete. 
Como vamos a utilizar Flask nos hace falta instalarlo:

	pip install flask

Además nos hace falta instalar “gunicorn”, el cual nos va a permitir realizar el deploy a los servidores de Heroku, con lo cual realizamos lo siguiente:

pip install flask gunicorn

Esperamos un par de segundos y ya los tendremos instalados.

1.2. Creación de los archivos necesarios para el deploy.

Si entramos a nuestra carpeta y todo el proceso del paso 1 se ha realizado correctamente, vamos a poder visualizar las siguientes carpetas: “bin”, “include” y “lib”.

Creamos una nueva carpeta llamada “[....]”, donde vamos a colocar nuestro servidor. Creamos un nuevo fichero dentro, llamado “[...]”, que contendrá el código principal. Guardamos y lo ejecutamos, a ver si funciona todo correctamente, de la siguiente forma:

python [...].py

Abrimos un navegador para acceder a la dirección correspondiente y vemos que todo está OK. Como vamos a utilizar Flask, tenemos que cambiar el puerto en nuestro fichero [...].py, al número 5000, y la bandera “debug” la ponemos a false.


Lo siguiente es crear un fichero llamado “requirements.txt”, donde colocaremos todos los paquetes necesarios para que nuestro servidor funcione. Para saber cuáles necesitamos hacemos lo siguiente en la terminal:

pip freeze

Esto nos lista todos los paquetes que tenemos instalados. Si se ha realizado bien el punto 1, todos los que nos aparezcan se han instalado como consecuencia. Para tenerlos dentro de nuestro fichero, simplemente ejecutamos el siguiente comando en nuestra terminal:

pip freeze > requirements.txt

Por último, tenemos que crear el archivo “Procfile”. No debe tener extensión y dentro de él colocamos qué archivo se va a ejecutar como servidor. Ponemos:

web: gunicorn [mi_archivo.py]:app

1.3. Realización del deploy.

Lo primero es tener una cuenta en Heroku. Una vez que la hemos creado, vamos a instalar Heroku Toolbert. Descargamos el que corresponda a nuestro SO, y una vez instalado nos logueamos. Para crear una nueva aplicación, ejecutamos en la terminal lo siguiente:

heroku create

Si entramos en la URL de nuestra cuenta Heroku vamos a ver que se ha creado una nueva app, con un nombre aleatorio: “[....]”. Si no estamos dentro de la sesión, nos logueamos desde la terminal, y accedemos a la sección de “Deploy” dentro de la URL anterior. Para loguearnos ejecutamos:

heroku login
(email)
(password)

Realizamos un clon del repositorio utilizado para la asignatura y luego enlazamos con el repositorio remoto de la app creada anteriormente. Para ello utilizamos lo siguiente:

heroku git:remote -a [...]
git add .
git commit -am “make it better”

Y ahora realizamos el deploy:

	git push heroku master

Esto actualiza el repositorio remoto. Lo que va a hacer es ir dentro de nuestro fichero “requirement.txt” y va a instalar todas las dependencias necesarias.

Para decirle a heroku que se actualize cada vez que hagamos un push y pase los test de travis tenemos que irnos a heroku seccion deploy sincronizar con github y habilitar la subida autmatica despues de pasar los test de travis CI.


https://young-meadow-45069.herokuapp.com/

