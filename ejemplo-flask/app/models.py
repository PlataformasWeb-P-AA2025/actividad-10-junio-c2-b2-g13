from app import db  # Importamos la instancia de la base de datos desde el módulo "app"

# Definimos la clase Usuario que representa una tabla en la base de datos
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Columna ID como clave primaria
    nombre = db.Column(db.String(100), nullable=False)  # Columna nombre con un máximo de 100 caracteres y que no puede ser nula

    # Método de representación en forma de cadena para facilitar la depuración
    def __repr__(self):
        return f"<Usuario {self.nombre}>"
