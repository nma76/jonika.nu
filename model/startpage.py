from dataclasses import dataclass
import json

@dataclass()
class Hero:
    heading: str
    intro: str
    image: str
    imagealt: str

@dataclass()
class Startpage:
    hero: Hero
        
def get_startpage():
    with open('./content/startpage.json') as file:
        data = json.load(file)
        return Startpage(**data)