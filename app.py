from flask import Flask
from routes.example import example_bp
from routes.users import users_bp

app = Flask(__name__)

if __name__ == "__main__":
    app.register_blueprint(example_bp)
    app.register_blueprint(users_bp)
    app.run(debug=True)
