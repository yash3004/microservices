from flask import Blueprint, request, jsonify
from flask_oauthlib.client import OAuth

bp = Blueprint("routes", __name__, url_prefix="user")


@bp.route("/login")
def login():
    oauth = OAuth(bp)

