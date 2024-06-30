# e-commerce Backend Service

---

The ```ecommerce-iws``` represents an internal web service.


## Folder Structure Conventions

---

```
    /
    ├── modules                     # The modules
    ├── e-commerce-iws              # The e-commerce backend service
    |    └── README.md
    └── README.md
```


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


## Install Requirements

```shell
python3 -m pip install -r requirements.txt
```

## Save Requirements (Dependencies)
```shell
pip freeze > requirements.txt
```


# Author

---

- Rohtash Lakra
