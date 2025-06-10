from flask import render_template, request
from app.models import Usuario, db

def saludo():
    nombre = request.args.get("name", "").strip()  

    if not nombre:
        nombre = "Invitado"

    usuario_existente = Usuario.query.filter_by(nombre=nombre).first()
    if not usuario_existente:  
        nuevo_usuario = Usuario(nombre=nombre)
        db.session.add(nuevo_usuario)
        db.session.commit()

    return render_template("saludo.html", nombre=nombre)
