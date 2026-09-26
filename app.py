import os
from urllib.parse import quote_plus

from flask import Flask
from controllers.db_controller import db_bp
from controllers.auth_controller import auth_bp
from dotenv import load_dotenv

from models import db
from controllers.main_controller import main_controller


load_dotenv()


app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")
app.register_blueprint(db_bp)
app.register_blueprint(auth_bp)


mysql_user = os.getenv("MYSQL_USER", "root")
mysql_password = os.getenv("MYSQL_PASSWORD", "")
mysql_host = os.getenv("MYSQL_HOST", "localhost")
mysql_port = os.getenv("MYSQL_PORT", "3306")
mysql_database = os.getenv("MYSQL_DATABASE", "internship_db")


encoded_user = quote_plus(mysql_user)
encoded_password = quote_plus(mysql_password)


app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://{encoded_user}:{encoded_password}"
    f"@{mysql_host}:{mysql_port}/{mysql_database}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)


app.register_blueprint(main_controller)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)