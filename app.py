from flask import Flask, render_template

application = Flask(__name__)

@application.route("/")
def home():
    return render_template("index.html")

@application.route("/info")
def info():
    return render_template("info.html")

@application.route("/owner")
def owner():
    return render_template("owner.html")

if __name__ == "__main__":
    application.run()