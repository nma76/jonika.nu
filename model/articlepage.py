from dataclasses import dataclass, field
from typing import Optional
from model.sitesettings import SiteSettings
from model.contact import Contact
import json

@dataclass()
class ArticlePage:
    contact: Contact
    heading: str
    published: str
    tags: list[str]
    image: str
    imagealt: str
    mainbody: str
    sitesettings: Optional[SiteSettings] = field(default_factory=lambda: None)
        
def get_articlepage():
    with open('./content/articles.json') as file:
        data = json.load(file)
        return ArticlePage(**data)