from flask import Flask
from config import Config
from database.mongodb import mongo

from routes.auth import auth
from routes.document import document

app = Flask(__name__)

# Secret key for sessions
app.secret_key = "devpulse_secret_key"

# Load configuration
app.config.from_object(Config)

# Initialize MongoDB
mongo.init_app(app)

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(document)


@app.route("/")
def home():
    return """
    <h1>Welcome to DevPulse</h1>

    <p>Collaborative Real-Time Markdown Editor & Team Wiki</p>

    <hr>

    <a href="/register">Register</a>
    <br><br>

    <a href="/login">Login</a>
    <br><br>

    <a href="/documents">My Documents</a>
    """


if __name__ == "__main__":
    app.run(debug=True)