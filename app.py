from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Base de datos de perfiles
usuarios = [
    {
        "id": "el03",
        "nombre": "EL 03",
        "rol": "FOUNDER",
        "color_rol": "#ef4444",
        "banner": "fondo03.png",  # <--- Tu imagen de la carpeta static
        "stats": {
            "palenques": "2s Palenques Ganados MVP",
            "rolas": "3 Rolas Champs Ganadas MVP",
            "pais": "🇸🇻 El Salvador",
        },
    },
    {
        "id": "angel06",
        "nombre": "angel 06",
        "rol": "CO FOUNDER",
        "color_rol": "#3b82f6",
        "banner": None,
        "stats": {
            "pais": "🇻🇪 Venezuela",
            "estado": "Legend. Retired ❌",
        },
    },
    {
        "id": "cookie04",
        "nombre": "Cookie 04",
        "rol": "CO FOUNDER",
        "color_rol": "#3b82f6",
        "banner": None,
        "stats": {
            "pais": "🇨🇺 Cuba",
            "estado": "Legend. Retired ❌",
        },
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/usuarios")
def get_usuarios():
    return jsonify(usuarios)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)