# python-flask-docker

Desarrollo de una aplicación en Python utilizando Flask y Docker siguiendo las instrucciones de:
https://www.youtube.com/watch?v=YENw-bNHZwg


## Comenzando 🚀

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.


### Entorno desarrollo 📋

Python3 y flask

```
yum install -y python3
pip3 install virtualenv
virtualenv venv
cd venv\bin
source ./activate
pip install flask
```

Creación del fichero requirements.txt

```
pip freeze > requirements.txt
```

## Despliegue 📦

Build image

```
docker build -t flaskapp .
```

Run container docker

```
docker run -it -p 4000:4000 -d flaskapp
```


## Construido con 🛠️

* Python3
* Flask
* Docker



## Wiki 📖

https://www.youtube.com/watch?v=YENw-bNHZwg&t=234s


## Autores ✒️

Gonzalo Déniz

