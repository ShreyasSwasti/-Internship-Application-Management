from flask import Blueprint, render_template, request, redirect, url_for, flash , session

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

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        # Check if fields are empty
        if not email or not password:
            flash("Email and password are required", "error")
            return render_template("login.html")

        # Find user by email
        user = get_user_by_email(email)

        # Check credentials
        if not user or user["password"] != password:
            flash("Invalid email or password", "error")
            return render_template("login.html")

        # Store user information in session
        session["user_id"] = user["id"]
        session["name"] = user["name"]
        session["email"] = user["email"]
        session["role"] = user["role"]

        # Redirect based on role
        if user["role"] == "HR Manager":
            return redirect(url_for("hr.dashboard"))

        return redirect(url_for("applicant.dashboard"))

    return render_template("login.html")

@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("You have been logged out successfully.", "success")

    return redirect(url_for("auth.login"))