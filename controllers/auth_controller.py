from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.user_model import get_user_by_email, create_applicant

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()
        qualification = request.form.get("qualification", "").strip()

        # Check if any field is empty
        if not name or not email or not password or not qualification:
            flash("All fields are required", "error")
            return render_template("register.html")

        # Check email format
        allowed_domains = [
            ".com",
            ".org",
            ".net",
            ".edu",
            ".gov",
            ".in",
            ".co.in",
            ".ac.in"
        ]

        if "@" not in email or not any(
            email.lower().endswith(domain)
            for domain in allowed_domains
        ):
            flash("Please enter a valid email address", "error")
            return render_template("register.html")

        # Check whether email already exists
        existing_user = get_user_by_email(email)

        if existing_user:
            flash("Email already registered", "error")
            return render_template("register.html")

        # Create new applicant
        create_applicant(
            name,
            email,
            password,
            qualification
        )

        flash(
            "Registration successful. Please login to continue.",
            "success"
        )

        return render_template("register.html")

    return render_template("register.html")