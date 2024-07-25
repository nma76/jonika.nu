from dataclasses import dataclass, field
from typing import Optional
from model.sitesettings import SiteSettings
import json

@dataclass()
class AboutPage:
    sitesettings: Optional[SiteSettings] = field(default_factory=lambda: None)
        
def get_aboutpage():
    return AboutPage()
    # with open('./content/startpage.json') as file:
    #     data = json.load(file)
    #     return Startpage(**data)