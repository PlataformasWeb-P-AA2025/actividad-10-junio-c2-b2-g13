from app import app, db  # Importamos la instancia de la aplicación Flask y la base de datos

# Creamos un contexto de aplicación para interactuar con la base de datos
with app.app_context():
    db.create_all()  # Crea todas las tablas definidas en los modelos si no existen
