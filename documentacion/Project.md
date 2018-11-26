# Creación de nuestro entorno aislado.

En este proyecto usare virtualenv con el cuál aislaremos nuestro proyecto, de nuestra máquina. Para ello tenemos que llevar los siguientes pasos:

1.Con sudo apt-get install python-virtualenv virtualenv o pip install virtualenv instalamos virtualenv.
2.Una vez lo tenemos instalado ejecutamos virtualenv nombre del entorno elegido, dicho comando nos creara una carpeta que contendrá nuestro entorno.
3.Pasamos a ejecutar nuestro entorno con . nombreentorno/bin/activate.

Como ya tengo mi proyecto creado en un repositorio de github, dentro de nuestro entorno hago un git clone de nuestro repositorio.

Puesto que usare flask dentro del entorno creado y activado instalare flask, mongo para la bd y gunicorn con el cual podre subir automaticamente a heroku nuestro projecto.

##### pip install flask

##### pip install flask gunicorn

##### pip install flask PyMongo

También nos creamos o añadimos a nuestro fichero requirements.tx  los paquetes nuevos con pip freeze > requirements.txt y ejecutamos :

##### pip install -r requiremts.txt

### La estructura de nuestro projecto sera la tipico de un projecto flask:

1.Carpeta llamada templates que contendrá las plantillas html de nuestra web.
2.Una carpeta llamada static que contendra tanto hojas de estilos como javascript e imagenes,etc..
3.En src pondré las clases necesaria para la realización del proyecto.
