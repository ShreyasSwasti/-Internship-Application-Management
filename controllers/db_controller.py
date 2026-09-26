from flask import Blueprint, jsonify
from models import db

db_bp = Blueprint("db", __name__)


def fetch_records(query, params=None):
    try:
        result = db.session.execute(
            db.text(query),
            params or {}
        )
        return result.mappings().all()

    except Exception:
        db.session.rollback()
        raise


def insert_record(query, params=None):
    try:
        db.session.execute(
            db.text(query),
            params or {}
        )
        db.session.commit()
        return True

    except Exception:
        db.session.rollback()
        raise


@db_bp.route("/test-db", methods=["GET"])
def test_db():
    try:
        db.session.execute(db.text("SELECT 1"))

        return jsonify({
            "status": "success",
            "message": "Database connection successful"
        }), 200

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "status": "error",
            "message": "Database connection failed",
            "error": str(e)
        }), 500