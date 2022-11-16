from flask import Flask, request, render_template

midapp = Flask(__name__)

@midapp.route("/")
def main():
    return render_template("login.html")

if __name__ == "__main__":
    midapp.run(host="0.0.0.0", port = 5050)