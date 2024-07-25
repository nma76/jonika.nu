from dataclasses import dataclass
from model.post import Post

@dataclass
class Blog:
    heading: str
    intro: str
    posts: list[Post]