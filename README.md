
![Logo](https://i.imgur.com/UnybDrA.png)


# fmartns.dev

Portfólio para compartilhamento de links




## Instalação (Linux)

Clone o repositório

```bash
$ git clone https://github.com/fmartns/fmartns.dev
$ cd fmartns.dev
```

Prepare o ambiente virtual

```bash
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

Rode as migrações

```bash
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py compilemessages
$ python manage.py createsuperuser
```

Inicie o servidor

```bash
$ python3 manage.py runserver
```



## Screenshots

![App Screenshot](https://i.imgur.com/eAW1jh8.png)


## Autor

- [@fmartns](https://www.github.com/fmartns)

