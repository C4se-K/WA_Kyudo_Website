from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
#app.secret_key


USERNAME = "temp"
PASSWORD = "temp"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if username == USERNAME and password == PASSWORD:
        return redirect(url_for("dashboard"))
    else:
        flash("Invalid username or password", "error")
        return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
