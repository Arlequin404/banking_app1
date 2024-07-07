from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Configuración de SQLAlchemy para las dos bases de datos
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://sa:8991@ALEX/BankingApp1?driver=ODBC+Driver+17+for+SQL+Server'
    app.config['SQLALCHEMY_BINDS'] = {
        'db2': 'mssql+pyodbc://sa:8991@ALEX/BankingApp2?driver=ODBC+Driver+17+for+SQL+Server'
    }

    db.init_app(app)

    with app.app_context():
        from . import views, models
        db.create_all()  # Crear tablas en la base de datos principal

        # Crear tablas en la segunda base de datos
        engine_db2 = create_engine(app.config['SQLALCHEMY_BINDS']['db2'])
        models.Base.metadata.create_all(bind=engine_db2)

    return app
