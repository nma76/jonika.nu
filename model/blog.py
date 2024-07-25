from dataclasses import dataclass
from model.contact import Contact

@dataclass()
class Post:
    image: str
    imagealt: str
    tag: str
    heading: str
    url: str
    intro: str
    published: str
    contact: Contact

@dataclass
class Blog:
    heading: str
    intro: str
    posts: list[Post]