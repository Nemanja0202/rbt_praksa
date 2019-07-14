import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


if os.environ['ENV_TYPE'] == 'Development':
    from config.development import Development as Conf
elif os.environ['ENV_TYPE'] == 'Production':
    from config.production import Production as Conf

db = SQLAlchemy()


from marshmallow import ValidationError
from measurement_bp import measurements_bp
from users_bp import users_bp


def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)

    migrate = Migrate(app, db)
    app.register_blueprint(measurements_bp)
    app.register_blueprint(users_bp)

    return app


app = create_app(Conf)


@app.errorhandler(ValidationError)
def _on_validation_error(ex):
    return ex.normalized_messages()


@app.route("/")
def hello():
    return "HELLO WORLD!"
    

