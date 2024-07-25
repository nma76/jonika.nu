from dataclasses import dataclass

@dataclass()
class ActionButton:
    caption: str
    targeturl: str
    
@dataclass()
class Hero:
    heading: str
    intro: str
    image: str
    imagealt: str
    actionbutton: ActionButton