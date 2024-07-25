from dataclasses import dataclass

@dataclass
class Story:
    heading: str
    intro: str

@dataclass
class Featured:
    heading: str
    stories: list[Story]