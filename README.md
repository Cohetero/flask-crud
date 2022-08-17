# Introducción
Este proyecto sencillo esta implementando con el framework de FastAPI para gestionar una api y entender su funcionamiento. Esta api trabaja junto con SQLAlchemy para trabajar con ORM la parte de la base de datos. Este proyecto trabaja un sencillo crud ocupando dichas tecnologias.

# Servicios de Docker
EL servicio de app corre el proyecto de fastAPI con la imagen que se estable y en que puerto. El servicio de mysql tiene un volumen donde guarda los datos y se le establecio sobre que base se tiene que trabajar junto con la contrseña

# Correr el proyecto
<p>Nota: Por el momento solo ejecuta el servicio de mysql porque el servicio de app aun no esta configurado para sqlAlchemy y restAPI</p>
<p>Para correrlo en docker, es ir al archivo src y ejecutar docker-compose up -d mysql</p>
<p>Se tiene que crear un entorno virtual e instalar los paquetes del archivo requirements.txt</p>
<p>pip install -r requirements.txt</p>
<p>Para correr el proyecto se tiene que situar en la carpeta de src y ejecutar el siguiente comando:</p>
<p>uvicorn app:app --reload </p>
<p>Y listo, el proyecto estara corriendo</p>
