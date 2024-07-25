from flask import Flask, render_template, send_from_directory
from model.startpage import get_startpage
from model.about import get_aboutpage
from model.sitesettings import get_sitesettings

app = Flask(__name__)

# Load global site settings
sitesettings = get_sitesettings()

# Add route to Assets
@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)

# Website routes
@app.route('/')
def index():
    model = get_startpage()
    model.sitesettings = sitesettings
    return render_template('index.html.j2', model=model)

@app.route('/about')
def about():
    model = get_aboutpage()
    model.sitesettings = sitesettings
    return render_template('about.html.j2', model=model)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

app.run(debug=True)