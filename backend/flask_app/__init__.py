from flask import Flask, request
import yaml


def create_app():
    app = Flask(__name__)
    with open("config.yaml", "r") as cfg_file:
        config = yaml.load(cfg_file)
        app.config.from_object(config)
    return app
