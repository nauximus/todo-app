from flask import Flask
from models import db
from routes import init_routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_routes(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Creates database tables
        app.run(host="0.0.0.0", port=5000, debug=True)