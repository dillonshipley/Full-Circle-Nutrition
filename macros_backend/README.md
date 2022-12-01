Macros Backend
===

## Local development

1. Start virtual environment
    ```bash
    source env/bin/activate
    ```
1. Install required packages
    ```bash
    pip install -r requirements.txt
    ```
1. Start the server locally at http://127.0.0.1:8000/
    ```bash
    python3 manage.py runserver
    ```

    or

    ```shell
    ./runserver.sh
    ```

## Environment Variables

If it is your first time running the app locally, create a .env file in the macros-backend directory. YOU MUST CREATE THIS TO RUN THE APP LOCALLY, OR TO CREATE DOCKER IMAGES
```shell
touch macros_backend/.env
```
There is a `dist.env` file that has the keys already filled out, the values can be found in the GitHub secrets page. *DO NOT* fill in the values into the `dist.env` file, this file is tracked by version control, use the `.env` file instead.

## Postgre

Since there is no production environment yet, we should use a Postgres Docker image. You can pull the image using this command:
```bash
docker pull postgres
```

Create a new container with this command. Notice that you will have to enter in the user and password environment variables manually

``` bash
docker run --name Macros -e POSTGRES_USERNAME=<USERNAME>-e POSTGRES_PASSWORD=<PASSWORD> -p 5432:5432 -d postgres
```

Use/create the environment variables file at `macros-backend/.env` to store the user and password for the database instance you create. You will need to create your own username and password. I recommend using the default username and generating a random password and saving it in the `.env` file for now.

## Build Backend Docker Image
From the root `/macros/` directory, run these commands to build the back end application Docker image
