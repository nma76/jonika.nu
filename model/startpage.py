from dataclasses import dataclass
import json

@dataclass
class Story:
    heading: str
    intro: str

@dataclass
class Featured:
    heading: str
    stories: list[Story]

@dataclass()
class Hero:
    heading: str
    intro: str
    image: str
    imagealt: str

@dataclass()
class Startpage:
    hero: Hero
    featured: Featured
        
def get_startpage():
    with open('./content/startpage.json') as file:
        data = json.load(file)
        return Startpage(**data)