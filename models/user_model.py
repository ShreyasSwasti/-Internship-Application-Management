
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
    # Hash the password before saving it
    hashed_password = generate_password_hash(password)

    query = """
        INSERT INTO users
        (name, email, password, qualification, role)
        VALUES
        (:name, :email, :password, :qualification, 'Applicant')
    """

    insert_record(
        query,
        {
            "name": name,
            "email": email,
            "password": hashed_password,
            "qualification": qualification
        }
    )


def authenticate_user(email, password):
    user = get_user_by_email(email)

    if not user:
        return None

    stored_password = user["password"]

    # Verify an already-hashed password
    try:
        password_valid = check_password_hash(
            stored_password,
            password
        )
    except (ValueError, TypeError):
        password_valid = False

    # Upgrade old plain-text passwords after successful login
    if not password_valid and stored_password == password:
        password_valid = True

        new_hash = generate_password_hash(password)

        db.session.execute(
            db.text("""
                UPDATE users
                SET password = :password
                WHERE id = :id
            """),
            {
                "password": new_hash,
                "id": user["id"]
            }
        )
        db.session.commit()

    if not password_valid:
        return None

    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": user["role"]
    }
