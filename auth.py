from flask import Blueprint, request, redirect, session, render_template
from models.user import User
from utils.password import hash_password, verify_password

auth = Blueprint("auth", __name__)


# ==========================
# Register
# ==========================
@auth.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Check if user already exists
        if User.find_by_email(email):
            return "User already exists"

        hashed_password = hash_password(password)

        User.create_user(username, email, hashed_password)

        return redirect("/login")

    return render_template("register.html")


# ==========================
# Login
# ==========================
@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.find_by_email(email)

        if user and verify_password(user["password"], password):

            session["user"] = user["username"]

            return redirect("/dashboard")

        return "Invalid Email or Password"

    return render_template("login.html")


# ==========================
# Dashboard
# ==========================
@auth.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


# ==========================
# User Profile
# ==========================
@auth.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login")

    user = User.find_by_username(session["user"])

    return render_template(
        "profile.html",
        user=user
    )


# ==========================
# Logout
# ==========================
@auth.route("/logout")
def logout():

    session.clear()

    return redirect("/login")