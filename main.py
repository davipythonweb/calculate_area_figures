from flask import Flask

from routes.home import home_bp
from routes.poligonos import poligonos_bp
from routes.paralelogramos import paralelogramos_bp

app = Flask(__name__)

# Registrar os blueprints
app.register_blueprint(home_bp)
app.register_blueprint(poligonos_bp)
app.register_blueprint(paralelogramos_bp)

if __name__ == "__main__":
    app.run(debug=True)