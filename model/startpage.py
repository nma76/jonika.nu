from dataclasses import dataclass
from model.story import Stories
from model.blog import Blog
from model.hero import Hero
import json

@dataclass()
class Startpage:
    hero: Hero
    featuredstories: Stories
    featuredblog: Blog
    # sitesettings: Optional[SiteSettings] = field(default_factory=None)
        
def get_startpage():
    with open('./content/startpage.json') as file:
        data = json.load(file)
        return Startpage(**data)