from app import app  # Importamos la instancia de la aplicación Flask desde el módulo "app"

# Verificamos si el script se está ejecutando directamente (no como un módulo importado)
if __name__ == "__main__":
    app.run(debug=True)  # Iniciamos la aplicación Flask en modo de depuración (debug)
