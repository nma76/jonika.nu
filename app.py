from flask import Flask, render_template, send_from_directory
from model.startpage import get_startpage
from model.aboutpage import get_aboutpage
from model.articlepage import get_articlepages
from model.sitesettings import get_sitesettings

app = Flask(__name__)

# Load global site settings
sitesettings = get_sitesettings()

# Load all articles
articles = get_articlepages()

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

@app.route('/article/<int:id>')
def article(id=id):
    model = next((article for article in articles if article.id == id), None)
    model.sitesettings = sitesettings
    return render_template('article.html.j2', model=model)

app.run(debug=True)