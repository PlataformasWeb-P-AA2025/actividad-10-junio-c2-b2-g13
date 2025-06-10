from flask import render_template, request  # Importamos Flask para manejar solicitudes y renderizar plantillas
from app.models import Usuario, db  # Importamos el modelo Usuario y la instancia de la base de datos

def saludo():
    nombre = request.args.get("name", "").strip()  # Obtiene el parámetro "name" de la solicitud GET y elimina espacios en blanco

    if not nombre:  # Si el nombre está vacío, asignamos "Invitado" como valor por defecto
        nombre = "Invitado"

    # Verificamos si el usuario ya existe en la base de datos
    usuario_existente = Usuario.query.filter_by(nombre=nombre).first()
    if not usuario_existente:  # Si el usuario no existe, lo creamos y lo guardamos en la base de datos
        nuevo_usuario = Usuario(nombre=nombre)
        db.session.add(nuevo_usuario)
        db.session.commit()

    # Renderizamos la plantilla "saludo.html" y pasamos el nombre como contexto
    return render_template("saludo.html", nombre=nombre)
