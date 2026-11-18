
import re

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from werkzeug.exceptions import BadRequest

from models.user_model import (
    get_user_by_email,
    create_applicant,
    authenticate_user
)

auth_bp = Blueprint("auth", __name__)


def is_valid_email(email):
    """Basic email format validation."""
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return bool(re.match(pattern, email))


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        qualification = request.form.get(
            "qualification", ""
        ).strip()

        # Validate required fields
        if not all([name, email, password, qualification]):
            flash("Please fill in all fields.", "error")
            return render_template("register.html")

        # Validate name
        if len(name) > 100:
            flash("Name must not exceed 100 characters.", "error")
            return render_template("register.html")

        # Validate email
        if len(email) > 254 or not is_valid_email(email):
            flash("Please enter a valid email address.", "error")
            return render_template("register.html")

        # Validate password
        if len(password) < 8:
            flash("Password must contain at least 8 characters.", "error")
            return render_template("register.html")

        # Validate qualification
        if len(qualification) > 150:
            flash("Qualification is too long.", "error")
            return render_template("register.html")

        try:
            # Check for existing account
            existing_user = get_user_by_email(email)

            if existing_user:
                flash("Email is already registered.", "error")
                return render_template("register.html")

            # Create applicant
            create_applicant(
                name,
                email,
                password,
                qualification
            )

            flash(
                "Registration successful. Please login.",
                "success"
            )

            return redirect(url_for("auth.login"))

        except Exception:
            # Log the exception on the server in production.
            flash(
                "Registration could not be completed. Please try again.",
                "error"
            )
            return render_template("register.html"), 500

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        # Validate login fields
        if not email or not password:
            flash("Please enter your email and password.", "error")
            return render_template("login.html")

        try:
            # Authenticate user
            user = authenticate_user(email, password)

        except Exception:
            flash(
                "Login is temporarily unavailable. Please try again.",
                "error"
            )
            return render_template("login.html"), 500

        if not user:
            flash("Invalid email or password.", "error")
            return render_template("login.html")

        # Prevent session fixation
        session.clear()

        # Store authenticated user information
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]
        session["user_email"] = user["email"]
        session["role"] = user["role"]

        # Redirect according to role
        role = str(user["role"]).strip().lower()

        if role in ("hr", "hr manager"):
            return redirect(url_for("hr.dashboard"))

        if role == "applicant":
            return redirect(url_for("applicant.dashboard"))

        # Reject unexpected account roles
        session.clear()
        flash("Your account has an invalid role.", "error")
        return redirect(url_for("auth.login"))

    return render_template("login.html")


@auth_bp.route("/logout", methods=["POST"])
def logout():

    session.clear()

    flash("You have been logged out successfully.", "success")

    return redirect(url_for("auth.login"))
