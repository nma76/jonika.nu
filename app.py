from flask import Flask, render_template, send_from_directory
from model.startpage import get_startpage

app = Flask(__name__)

@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)

@app.route('/')
def index():
    model = get_startpage()
    return render_template('index.html.j2', model=model)

@app.route('/about')
def about():
    return render_template('about.html.j2')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

app.run(debug=True)