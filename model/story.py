from dataclasses import dataclass

@dataclass
class Story:
    heading: str
    intro: str

@dataclass
class Stories:
    heading: str
    stories: list[Story]