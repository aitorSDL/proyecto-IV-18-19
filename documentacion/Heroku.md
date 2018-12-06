## Despliegue de app en Heroku.

En este documento voy a explicar cómo  crear una aplicacion en los servidores de heroku, y configurar heroku para que se conecte con git para subir automaticamente cada cambio en nuestro proyecto cuando hagamos un push en git.




###  Creacion de cuenta en heroku y configuracion de enlazado con git.

###  Nos registramos en  [Heroku](https://www.heroku.com/) .

Le damos a sign up for free:

![Registro](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/registro1.jpg) 

<br>

Insertamos los datos que nos pide heroku:

![Registro Datos](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/registro2.jpg) 

y verificamos nuestra cuenta con el enlace enviado a nuestro correo.

<br>

###  Creamos nuestra aplicacion.


Le doy a create new app:

![Creacion app](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/creacionapp.jpg) 

<br>

y despues tenemos que introducir el nombre y la region:

![datos app](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/creacionapp1.jpg) 


<br>

### Configuramos nuestra aplicacion para conectarse con nuestro proyecto de git.

<br><br>
En la pestaña deploy dentro de la aplicacion le damos a conectar con git y seleccionamos nuestro proyecto:

![conectar git](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/conectarcongit.jpg) 

<br>

### Configuramos nuestra aplicacion para automatizar la subida cada vez que se modifique desde git y pase los test de travisCI

<br>

Le damos a automatizar subida cuando git tenga cambios despues de pasar los test de travisCI:

![Automatizacion](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/automatizacion.jpg) 


<br>

### Aquí muestro la app corriendo en heroku:

![status](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/statusOK.jpg) 