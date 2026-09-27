from flask import Blueprint, render_template, session, redirect, url_for

hr_bp = Blueprint("hr", __name__)


@hr_bp.route("/hr/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    if session.get("role") != "HR Manager":
        return redirect(url_for("applicant.dashboard"))

    return render_template(
        "hr_dashboard.html",
        name=session.get("name"),
        email=session.get("email")
    )