# Content-Apis

## Instructions and Navigations
Clone [project](https://github.com/ThucNguyen007/apis-content-systems)

`git clone https://github.com/ThucNguyen007/apis-content-systems.git`

Create a file '.env' in the root folder
```
SECRET_KEY=
ENV=DEV
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_NAME= "Your local Postgres Database name"
DATABASE_USER= "Your local Postgres Database User"
DATABASE_PASSWORD= "Your local Postgres Database Password"
DATABASE_HOST=localhost - Default
DATABASE_PORT=5432 - Default
POSTGRES_USER= "Your Docker Postgres Database User"
POSTGRES_PASSWORD= "Your Docker Postgres Database Password"
POSTGRES_DB= "Your Docker Postgres Database name"
```

**Download Postgres version 14.8 to manage server with this link:**

https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

**After completing steps above**, `cd` to this root code folder, 
Then create a `virtual environment` to compile neccessary packages: 

Now that we have Python installed, we have to ensure that we have virtualenv installed:

`py -m pip install --user virtualenv`

Commands will create the venv directory containing the installed Python packages and the necessary configuration to access these packages when the virtual environment is activated:

`py -m venv venv`

The next step is to activate the virtual environment:

`.\venv\Scripts\activate`

Now that we have our virtual environment setup, we can install every essential packages:

`pip install -r requirements.txt`

Great – we have the adapter installed, let’s quickly create the database we’ll use for this project.
For that, we need to connect as a Postgres user in the terminal and then access the psql terminal.
In that terminal, we can enter SQL commands.

`psql -U postgres`

* Let’s create the database: `CREATE DATABASE ...;`

* To connect to the database, we need USER with a password:
`CREATE USER 1 WITH PASSWORD 'your-password-here';`

* and the next step is to grant access to our database to the new user:
`GRANT ALL PRIVILEGES ON DATABASE ... TO 1;`

* We are nearly done. We also need to make sure this user can create a database. This will be helpful when
we can run tests. To run tests, Django will configure a full environment but will also use a database:
`ALTER USER 1 CREATEDB;`

With that, we are done with the creation of the database. Connect this database to our Django project.

* Open the settings.py inside `ParentRoot` and update the DATABASES variable:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("DATABASE_NAME", "..."),
        'USER': os.getenv("DATABASE_USER", "1"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD", "your-password-here"),
        'HOST': os.environ.get("DATABASE_HOST", "localhost"),
        'PORT': os.getenv("DATABASE_PORT", "5432"),
    }
}
```

In the project directory, run the `makemigrations` command to create migrations for those changes:

`python manage.py makemigrations`

Then run migrate again to apply those changes to the database:

`python manage.py migrate`

Now we can run the server:

`python manage.py runserver`

## Testing the Rest APIS with POSTMAN:

1) This is the `GET` method:
http://localhost:8000/api/user/
or
http://127.0.0.1:8000/api/user/

    * Output:
```
{
    "detail": "Authentication credentials were not provided."
}
```

2) This is the `POST` register method:
http://127.0.0.1:8000/api/auth/register/
or
http://localhost:8000/api/auth/register/

    * JSON body:
```
{
    "email": "testuser@gmail.com",
    "username": "up-to-you",
    "password": "up-to-you-with-digits-and-characters",
    "first_name": "Miles",
    "last_name": "Morales"
}
```

3) This is the `POST` login method:
http://127.0.0.1:8000/api/auth/login/
or
http://localhost:8000/api/auth/login/

    * JSON body:
```
{
    "email": "testuser@gmail.com",
    "username": "up-to-you",
    "password": "up-to-you-with-digits-and-characters"
}
```

4) This is the `POST` method:
http://127.0.0.1:8000/api/auth/refresh/
or
http://localhost:8000/api/auth/refresh/

    * JSON body:
```
{
    "refresh": "Your refresh token provided by the login method in the response"
}
```

5) This is the `PATCH` method to retrieve user:
http://127.0.0.1:8000/api/user/your-id-from-login-method/
or
http://localhost:8000/api/user/your-id-from-login-method/

    * JSON body:
```
{
    "last_name": "Morales"
}
```

* Output:

```
{
    "detail": "Authentication credentials were not provided."
}
```

6) This is the `POST` post method to start a chat:
http://localhost:8000/api/post/
or
http://127.0.0.1:8000/api/post/

    * Before using this method, you must provide an access token - "Bearer Token" in the header of the request inside `POST` register method

    * JSON body:
```
{
    "author": "your-generated-id-from-login-method",
    "body": "A simple posted"
}
```

7) This is the `GET` method to retrieve all posts:
http://localhost:8000/api/post/
or
http://127.0.0.1:8000/api/post/

    * JSON Body:
```
{
    "author": "your-generated-id-from-login-method",
    "body": "A simple posted"
}
```

8) This is the `PUT` method to update a post:
http://localhost:8000/api/post/your-generated-id-from-login-method/
or
http://127.0.0.1:8000/api/post/your-generated-id-from-login-method/

    * JSON Body:
```
{
    "author": "your-post-id-from-get-method-above",
    "body": "A simple posted"
}
```


