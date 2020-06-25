from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/derek')
def derek():
    return render_template("derek.html")

@app.route('/leo')
def leo():
    return render_template("leo.html")

if __name__ == '__main__':
    app.run(debug=True)
