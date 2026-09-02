from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Lista completa de usuarios con el usuario 03 actualizado con el nuevo GIF animado
usuarios = [
    {
        "id": "01",
        "nombre": "Usuario 01",
        "rol": "Admin",
        "banner": None,
        "avatar": "fondo03.png"
    },
    {
        "id": "02",
        "nombre": "Usuario 02",
        "rol": "Moderador",
        "banner": None,
        "avatar": "fondo03.png"
    },
    {
        "id": "03",
        "nombre": "Usuario 03",
        "rol": "Fundador",
        "banner": "banner-03.gif",  # <--- Aquí está apuntando a tu nuevo GIF animado
        "avatar": "fondo03.png"
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/usuarios')
def get_usuarios():
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)