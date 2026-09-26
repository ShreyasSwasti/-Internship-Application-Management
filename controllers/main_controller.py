from flask import Blueprint, redirect, url_for

main_controller = Blueprint("main_controller", __name__)


@main_controller.route("/", methods=["GET"])
def home():
    return redirect(url_for("auth.register"))