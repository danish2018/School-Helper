# Requirements

- Make sure you have [Python 3](https://www.python.org/downloads/) installed.
- That's it!

# Steps to run the project on Windows

- Create virtual environment using following command:

```cmd
python3 -m venv venv
```

- Activate virtual environment using following command:

```cmd
venv\Scripts\activate
```

- Install dependencies using following command:

```cmd
pip install -r requirements.txt
```

- Go inside the project flder

```cmd
cd EduTask
```

- Run the following two commands to create database

```
python manage.py makamigrations
python manage.py migrate
```

- Create SUPERUSER with the following command

```
python manage.py ceatesuperuser
```

- Run the code using the following command

```
python manage.py runserver 
```
