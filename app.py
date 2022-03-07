from project import create_app, ext_celery

app = create_app()
celery = ext_celery.celery

# import time
# from flask import Flask
# from celery import Celery


# app = Flask(__name__)

# celery = Celery(
#     __name__,
#     broker="redis://127.0.0.1:6379/0",
#     backend="redis://127.0.0.1:6379/0"
# )

# @app.route('/')
# def hello():
#     return "Hello World"

# @celery.task
# def divide(x, y):
#     time.sleep(3)
#     return x / y