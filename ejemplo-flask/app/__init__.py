from flask import Flask  # Importamos Flask para crear la aplicación web
from flask_sqlalchemy import SQLAlchemy  # Importamos SQLAlchemy para manejar la base de datos

# Creamos una instancia de Flask y especificamos la carpeta de templates
app = Flask(__name__, template_folder="../templates")  

# Configuramos la base de datos SQLite llamada "usuarios.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Desactivamos el rastreo de modificaciones para mejorar el rendimiento

# Creamos una instancia de SQLAlchemy para gestionar la base de datos
db = SQLAlchemy(app)

# Importamos las rutas de la aplicación para que estén disponibles
from app import routes  
