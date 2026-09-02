from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Base de datos de perfiles
usuarios = [
    {
        "id": "el03",
        "nombre": "EL 03",
        "rol": "FOUNDER",
        "color_rol": "#ef4444",
        "banner": "nuevo-fondo.gif",
        "stats": {
            "palenques": "2s Palenques Ganados MVP",
            "rolas": "3 Rolas Champs Ganadas MVP",
            "pais": "sv El Salvador",
        }
    },
    {
        "id": "angel06",
        "nombre": "angel 06",
        "rol": "CO FOUNDER",
        "color_rol": "#3b82f6",
        "banner": None,
        "stats": {
            "pais": "ve Venezuela",
            "estado": "Legend. Retired X",
        }
    },
    {
        "id": "cookie04",
        "nombre": "Cookie 04",
        "rol": "CO FOUNDER",
        "color_rol": "#3b82f6",
        "banner": None,
        "stats": {
            "pais": "cu Cuba",
            "estado": "Legend. Retired X",
        }
    }
]

@app.route('/')
def home():
    return render_template('index.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)