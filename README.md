
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)

## Proyecto-IV-18-19

## Descripción del proyecto.

 El objetivo del proyecto es la realización de una tienda online de productos informáticos, en la cuál se gestionarán usuarios, productos y además  existirá un servicio que nos avisará cuando la competencia tenga el precio mas bajo. 

Elegí este proyoecto puesto que me resulta interesante y útil, en el cuál pueda reflejar conocimientos adquiridos en otras asignaturas y cosas aprendidas de forma libre y autodidacta.

## Documentación herramientas a usar
### Herramientas a usar.

 - Como lenguaje de programación usaré python, puesto que lo dí en una asignatura en años anteriores y creo que tiene un gran potencial y versatilidad.
 - MongoDB para la gestión de productos y usuarios. Por su rapidez y adaptabilidad ante grandes cantidades de datos.
 - Como framework usaré flask. Puesto que su sencillez permite crear aplicaciones web rápidamente y con un mínimo número de líneas de código.
 - Usaré heroku para el despliegue de la aplicación. Puesto que me parece interesante este servicio de cloud computing y aprender a manejarme con él.
 - Gunicorn para automatizar la subida a Heroku
 - Jinja 2 para los templates HTML.

#### Pasar los test con el comando :

	python3 src/test*

![test](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/test.png) 

### Adaptando proyecto para heroku.

#### Archivo procfile

El procfile es el archivo con el que le decimos a heroku cual de todos los archivos del proyecto es el principal, el cual se va a ejecutar podriamos es decir ejecutando "main:app". En mi caso mi proyecto consta de un archivo index.py que es donde se ejecuta todo lo relacionado con Flask y donde se ejecuta el app.run(), que se encarga de inicializar la ejecución de la APP.

![main](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/main.jpg) 
  
#### Instalamos gunicorn y lo añadimos a requirementx.txt

##### - pip install flask gunicorn

- requirementx.txt quedará así:

		pytest>=3.8.2
		Flask==1.0.2
		Flask-PyMongo==2.2.0
		gunicorn==19.9.0
		Jinja2==2.10
		pymongo==3.7.2
		
- Lo Siguiente es instalar las dependencias del requirements.txt:
		
		pip install -r requirements.txt # Para instalar las dependencias

![main](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/main.jpg) 

#### Añadimos ruta / con el status OK

Hemos añadido dos rutas para ver que la aplicacion esta funcionando :

- la raiz / que devuelve ok
- /status que devuelve algunos parámetros mas como el número de productos .

![index](https://github.com/kaizensamuel/proyecto-IV-18-19/blob/master/documentacion/img/index.jpg) 

### Configuración de heroku.
En el siguiente enlace podemos ver toda la configuración necesaria de heroku:

 
- Despliegue en heroku:
 
 [![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](ttps://young-meadow-45069.herokuapp.com/)
  
Se puede  ver en el siguiente enlace como esta en funcionamiento la app en heroku:

[Despliegue](https://young-meadow-45069.herokuapp.com/) 

[![Build Status](https://travis-ci.org/kaizensamuel/proyecto-IV-18-19.svg?branch=master)](https://travis-ci.org/kaizensamuel/proyecto-IV-18-19)
