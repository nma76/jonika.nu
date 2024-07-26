from dataclasses import dataclass, field
from typing import Optional
from model.sitesettings import SiteSettings
from model.story import Story
import json

@dataclass()
class AboutStory(Story):
    image: str
    imagealt: str

@dataclass()
class AboutPage:
    heading: str
    intro: str
    stories: list[AboutStory]
    sitesettings: Optional[SiteSettings] = field(default_factory=lambda: None)
        
def get_aboutpage():
    with open('./content/about.json') as file:
        data = json.load(file)
        return AboutPage(**data)