#
# Author: Rohtash Lakra
# Reference - https://realpython.com/flask-project/
#
from ecommerce.webapp.app import WebApp

# init app by calling crate api function.
web_app = WebApp()
app = web_app.create_app()


"""
Main Application

How to run:
- python3 webapp.py
- python -m flask --app webapp run --port 8080 --debug

"""
# App Main
if __name__ == "__main__":
    web_app.run(app)
