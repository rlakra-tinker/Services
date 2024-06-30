# ecommerce-ews

---

The ```ecommerce-ews``` represents an external webapp service.

## Folder Structure Conventions

---

```
    /
    ├── modules                     # The name of the module
    ├── ecommerce-ews               # The ecommerce-ews external module/service
    |    ├── api                    # The API of the client
    |    ├── blueprints             # The routes of the views
    |    ├── models                 # contains the definition of the application’s models.
    |    ├── static                 # contains the application’s static files.
    |    |    ├── css               # css files
    |    |    ├── images            # image files
    |    |    ├── js                # JavaScript files
    |    ├── templates              # contains the application’s templates.
    |    |    ├── views             # The HTML views/pages
    |    ├── config.py              # contains the application configuration parameters.
    |    ├── models.py              # contains the definition of the application’s models.
    |    ├── webapp              # contains the web application logic.
    |    └── README.md              # The README file of ews module
    └── README.md
```


Although this layout is pretty straightforward, it has several drawbacks that arise as the app complexity increases. 
For example, it will be hard for you to reuse the application logic in other projects because all the functionality is 
bundled in ```webapp.py```. If you split this functionality into modules instead, then you could reuse complete modules 
across different projects.



# Building Application

---

## Create Virtual Env
```shell
python3 -m pip install virtualenv
python3 -m venv venv
```

## Activate ```venv```

```source``` is Linux/macOS command and doesn't work in Windows.

- Windows

    ```shell
    venv\Scripts\activate
    ```

- Mac OS/Linux

    ```shell
    source venv/bin/activate
  
  OR
  
    . ./venv/bin/activate
    ```

The parenthesized (venv) in front of the prompt indicates that you’ve successfully activated the virtual environment.

## Upgrade ```pip``` release

```shell
pip install --upgrade pip
```

## Install Packages

- Install Flask

**Note**: - You can skip ```Install Packages``` steps and run [Install Requirements](./Install_Requirements) steps directly. But if any error comes, come back to run these steps.

```shell
python3 -m pip install Flask
```


## Install Requirements

```shell
python3 -m pip install -r requirements.txt
```



## Save Requirements (Dependencies)
```shell
pip freeze > requirements.txt
```


## Configuration Setup

Set local configuration file.

```shell
pip install python-dotenv
cp default.env .env
```

Now, update the default local configurations as follows:

```text
APP_HOST = 0.0.0.0
APP_PORT = 8080
```

**By default**, Flask will run the application on **port 5000**.

## Run Flask Application

```shell
python -m flask --app webapp run --port 8080 --debug
```

**Note**:- You can stop the development server by pressing ```Ctrl+C``` in your terminal.


## Access Application
```shell
http://localhost:8080/ecommerce-ews
```


# Author

---

- Rohtash Lakra
