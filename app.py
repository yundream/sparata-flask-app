from flask import Flask, render_template

app=Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/")
def home():
    return render_template('index.html', message='Hello, Flask!')

app.run(host="0.0.0.0", port=5000)