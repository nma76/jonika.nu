from dataclasses import dataclass

@dataclass
class Story:
    heading: str
    intro: str
    url: str
    urlcaption: str

@dataclass
class Stories:
    heading: str
    stories: list[Story]