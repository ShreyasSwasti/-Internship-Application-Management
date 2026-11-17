
from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from models.user_model import (
    get_user_by_email,
    create_applicant,
    authenticate_user
)

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        qualification = request.form.get("qualification", "").strip()

        # Validate required fields
        if not all([name, email, password, qualification]):
            flash("Please fill in all fields", "error")
            return render_template("register.html")

        # Check whether email already exists
        existing_user = get_user_by_email(email)

        if existing_user:
            flash("Email already registered", "error")
            return render_template("register.html")

        # Create applicant with hashed password
        create_applicant(
            name,
            email,
            password,
            qualification
        )

        flash("Registration successful. Please login.", "success")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Validate login fields
        if not email or not password:
            flash("Please enter email and password", "error")
            return render_template("login.html")

        # Authenticate user
        user = authenticate_user(email, password)

        if not user:
            flash("Invalid email or password", "error")
            return render_template("login.html")

        # Clear previous session data
        session.clear()

        # Store authenticated user information
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        session["user_email"] = user["email"]
        session["role"] = user["role"]

        # Redirect based on user role
        if user["role"] == "HR":
            return redirect(url_for("hr.dashboard"))

        return redirect(url_for("applicant.dashboard"))

    return render_template("login.html")


@auth_bp.route("/logout", methods=["GET", "POST"])
def logout():

    session.clear()

    flash("You have been logged out successfully", "success")

    return redirect(url_for("auth.login"))
