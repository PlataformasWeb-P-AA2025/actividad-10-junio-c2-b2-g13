from app import app  # Importamos la instancia de la aplicación Flask desde el módulo "app"
from app.views import saludo  # Importamos la función "saludo" desde el módulo "views"
from flask import render_template  # Importamos "render_template" para renderizar archivos HTML

# Definimos una ruta para la página principal
@app.route("/")
def home():
    return render_template("index.html")  # Renderiza el archivo "index.html" ubicado en la carpeta de templates

# Definimos una ruta para "/saludo" que solo acepta solicitudes GET
@app.route("/saludo", methods=["GET"])
def saludo_view():
    return saludo()  # Llama a la función "saludo" definida en el módulo "views" y devuelve su resultado
