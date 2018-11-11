# Integración Continua. Travis.CI

## En este projecto usare Travis CI como sistema de integracion continua para ello seguiremos los siguientes pasos:

1. Primero debemos ir a la pagina : https://travis-ci.org/ y logearnos con nuestra cuenta de github .

2. Segundo tendremos que decirle a travis sobre que proyecto queremos que se active en mi caso es proyecto-IV-18-19.

3. Tercero tendremos que añadir al proyecto dos archivos:

	- .travis.yml con el cual le diremos en que lenguaje estamostrabajando que version, las dependencias  y que archivos contienen lostest para que los ejecute.
	- requirements.txt que contendra las dependencias y los paquetes instalados para el funcionamiento de nuestro proyecto.

4. Por ultimo cada vez que hagamos un push se ejecutara travis el cual hara que el projecto pase por los test puestos por nosotros 
