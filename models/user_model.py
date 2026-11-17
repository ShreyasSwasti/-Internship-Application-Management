
from controllers.db_controller import fetch_records, insert_record
from models import db
from werkzeug.security import generate_password_hash, check_password_hash


def get_user_by_email(email):
    query = """
        SELECT id, name, email, password, qualification, role
        FROM users
        WHERE email = :email
    """

    records = fetch_records(query, {"email": email})

    return records[0] if records else None


def create_applicant(name, email, password, qualification):
    # Generate a secure password hash
    hashed_password = generate_password_hash(password)

    query = """
        INSERT INTO users
        (name, email, password, qualification, role)
        VALUES
        (:name, :email, :password, :qualification, 'Applicant')
    """

    params = {
        "name": name,
        "email": email,
        "password": hashed_password,
        "qualification": qualification
    }

    return insert_record(query, params)


def authenticate_user(email, password):
    # Find user using email
    user = get_user_by_email(email)

    if not user:
        return None

    stored_password = user["password"]

    # Verify the submitted password against its hash
    try:
        password_valid = check_password_hash(
            stored_password,
            password
        )
    except (ValueError, TypeError):
        password_valid = False

    if not password_valid:
        return None

    # Return authenticated user details
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": user["role"]
    }
