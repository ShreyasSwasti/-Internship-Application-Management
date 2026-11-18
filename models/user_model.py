
from controllers.db_controller import fetch_records, insert_record
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


def get_user_by_email(email):
    """
    Retrieve a user using their email address.
    """

    if not email or not isinstance(email, str):
        return None

    query = """
        SELECT id, name, email, password, qualification, role
        FROM users
        WHERE email = :email
        LIMIT 1
    """

    records = fetch_records(
        query,
        {"email": email.strip().lower()}
    )

    return records[0] if records else None


def create_applicant(name, email, password, qualification):
    """
    Create a new applicant with a securely hashed password.
    """

    # Validate input
    if not all([name, email, password, qualification]):
        raise ValueError("All applicant fields are required.")

    if not isinstance(password, str) or len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    # Normalize email
    email = email.strip().lower()

    # Generate secure password hash
    hashed_password = generate_password_hash(
        password,
        method="scrypt"
    )

    query = """
        INSERT INTO users
        (name, email, password, qualification, role)
        VALUES
        (:name, :email, :password, :qualification, 'Applicant')
    """

    params = {
        "name": name.strip(),
        "email": email,
        "password": hashed_password,
        "qualification": qualification.strip()
    }

    return insert_record(query, params)


def authenticate_user(email, password):
    """
    Authenticate a user using email and password.
    Returns user details if authentication succeeds.
    """

    if not email or not password:
        return None

    user = get_user_by_email(email)

    if not user:
        return None

    stored_password = user["password"]

    if not stored_password or not isinstance(stored_password, str):
        return None

    try:
        password_valid = check_password_hash(
            stored_password,
            password
        )

    except (ValueError, TypeError):
        password_valid = False

    if not password_valid:
        return None

    # Return only the details required by the application.
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": user["role"]
    }
