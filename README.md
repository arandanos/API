# API
Para ejecutar la API: 

```bash
$ docker compose build

$ docker compose run web python manage.py makemigrations

$ docker compose run web python manage.py migrate

$ docker compose up 
```

Para importar la copia de la base de datos ejecutar el script import.sh