from dataclasses import dataclass
from model.stories import Featured
from model.hero import Hero
import json

@dataclass()
class Startpage:
    hero: Hero
    featured: Featured
        
def get_startpage():
    with open('./content/startpage.json') as file:
        data = json.load(file)
        return Startpage(**data)