from dataclasses import dataclass
import json

@dataclass()
class Meta:
    description: str
    author: str

@dataclass()
class MenuItem:
    heading: str
    url: str
        
@dataclass()
class TopMenu:
    homecaption: str
    menuitems: list[MenuItem]
    
@dataclass()
class Footer:
    copyright: str

@dataclass()
class SiteSettings:
    meta: Meta
    title: str
    topmenu: TopMenu
    footer: Footer
           
def get_sitesettings():
    with open('./content/sitesettings.json') as file:
        data = json.load(file)
        return SiteSettings(**data)