# Admin Panel
## Service for online cinema administration. 

## Common steps:
1. add `.env` file to `/config` directory (example is attached bellow): 
    ```
    DB_NAME=movies_database
    DB_USER=app
    DB_PASSWORD=123qwe
    DB_HOST=0.0.0.0
    DB_PORT=5434

    SECRET_KEY=django-insecure-aknpu&1*dfo%nd6c3$nx!2#wb_x+o$2d++u3ov(vd!1*+#o&j0 

    DEBUG=True
    ```

## Dev mode

### To run the application on your local machine, do the following:
1. Make sure that you use required python version (python 3.10.12) or change it if it's necessary (using pyenv, for example)
2. Write following commands in terminal:
    * Preparation (do it only once):
        * `python3 -m venv venv`
        * `source venv/bin/activate`
        * `pip install -r requirements.txt`
        * `pre-commit install`
        * `chmod +x entrypoint.sh`
    * To run the service:
        * `./entrypoint.sh`

### Code testing: 
`tests.sh` file contains all the commands to run required tests and linter checks. It automatically runs each time you make commit but you can run them from time to time during development to check if you do everything right.
