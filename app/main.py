from flask import Flask, session, redirect
from database import init_db

from routes.auth_routes import auth_bp
from routes.admin_routes import admin_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"

init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")
    return f"Welcome {session['user']}"

if __name__ == "__main__":
    app.run(debug=True)