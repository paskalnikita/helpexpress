Install
-------------------
  * Install Python >= 3.x
  * Install dependencies (django >=1.9, <2)
  
```bash
$ pip install -r requirements.txt
```


Run in virtual environments
-------------------

```bash
virtualenv venv -p C:\Python36\python.exe
cd venv
cd Scripts
.\activate
```


Build and run
-------------------
```bash
$ (env) python .\manage.py createsuperuser
$ (env) python .\manage.py migrate
$ (env) python .\manage.py runserver
```

Open browser: 127.0.0.1:8000

Tests
-------------------

```bash
$ (env) python .\manage.py test
```
