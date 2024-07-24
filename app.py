from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)

@app.route('/')
def index():
    # return "<h1>Hello World</h1>"
    return render_template('index.html.j2')

@app.route('/about')
def about():
    # return "<h1>Hello World</h1>"
    return render_template('about.html.j2')

app.run(debug=True)