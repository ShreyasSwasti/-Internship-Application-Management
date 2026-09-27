from controllers.db_controller import fetch_records, insert_record


def get_user_by_email(email):
    query = """
        SELECT id, name, email, password, qualification, role
        FROM users
        WHERE email = :email
    """

    records = fetch_records(
        query,
        {"email": email}
    )

    return records[0] if records else None


def create_applicant(name, email, password, qualification):
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
            "password": password,
            "qualification": qualification
        }
    )


def authenticate_user(email, password):
    user = get_user_by_email(email)

    if not user:
        return None

    if user["password"] != password:
        return None

    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "role": user["role"]
    }