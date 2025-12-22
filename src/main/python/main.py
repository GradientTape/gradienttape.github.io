import os
from jinja2 import Environment, FileSystemLoader

from my_site import *


ALL_POSTS = [
]


def create_website():
    site = MySite()
    for post_data in ALL_POSTS:
        site.posts.append(BlogPost.create(post_data))

    return site


if __name__ == '__main__':
    environment = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

    site = create_website()
    site.render(environment)
