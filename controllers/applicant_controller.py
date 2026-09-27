from flask import Blueprint, render_template, session, redirect, url_for

applicant_bp = Blueprint("applicant", __name__)


@applicant_bp.route("/applicant/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        name=session.get("name"),
        email=session.get("email")
    )