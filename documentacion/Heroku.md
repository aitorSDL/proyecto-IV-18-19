##Despliegue de app en Heroku.

En este documento voy a explicar cómo  crear una aplicacion en los servidores de heroku, y configurar heroku para que se conecte con git para subir automaticamente cada cambio en nuestro proyecto cuando hagamos un push en git.

###1. Adaptando proyecto para heroku.

####1.1.Instalamos gunicorn y lo añadimos a requirementx.txt

##### - pip install flask gunicorn

![requirements](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/requirements.jpg) 

####1.2.Añadimos el archivo procfile

El procfile es el archivo con el que le decimos a heroku cual de todos los archivos del proyecto es el principal, el cual se va a ejecutar podriamos decir que es el main de nuestra aplicacion.

![main](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/main.jpg) 

####1.3.Añadimos ruta / con el status OK

Hemos añadido dos rutas para ver que la aplicacion esta funcionando :

- la raiz / que devuelve ok
- /status que devuelve algunos parametros mas como el numero de productos .

![index](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/index.jpg) 




###2. Creacion de cuenta en heroku y configuracion de enlazado con git.

###2.1. Nos registramos en  [Heroku](https://www.heroku.com/) .

Le damos a sign up for free:

![Registro](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/registro1.jpg) 

<br>

Insertamos los datos que nos pide heroku:

![Registro Datos](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/registro2.jpg) 

y verificamos nuestra cuenta con el enlace enviado a nuestro correo.

<br>

###2.2. Creamos nuestra aplicacion.


Le doy a create new app:

![Creacion app](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/creacionapp.jpg) 

<br>

y despues tenemos que introducir el nombre y la region:

![datos app](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/creacionapp1.jpg) 


<br>

###2.3. Configuramos nuestra aplicacion para conectarse con nuestro proyecto de git.

<br><br>
En la pestaña deploy dentro de la aplicacion le damos a conectar con git y seleccionamos nuestro proyecto:

![conectar git](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/conectarcongit.jpg) 

<br>

###2.4. Configuramos nuestra aplicacion para automatizar la subida cada vez que se modifique desde git y pase los test de travisCI

<br>

Le damos a automatizar subida cuando git tenga cambios despues de pasar los test de travisCI:

![Automatizacion](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/automatizacion.jpg) 


<br>

###3. Aquí muestro la app corriendo en heroku:

![status](/home/sam/Escritorio/iv/projecto/proyecto-IV-18-19/documentacion/img/statusOK.jpg) 