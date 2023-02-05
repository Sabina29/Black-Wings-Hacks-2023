from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/explore")
# def about():
#     return render_template("explore.html")

# @app.route("/zipcode")
# def about():
#     return render_template("zipcode.html")

# @app.route("/login")
# def about():
#     return render_template("login.html")

# @app.route("/signup")
# def about():
#     return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)