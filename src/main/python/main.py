import os
from jinja2 import Environment, FileSystemLoader

from my_site import *


ALL_POSTS = [
    {
        "title": "Test Post #1",
        "slug": "test",
        "cover": "https://i.imgur.com/cXE2Lig.jpeg",
        "path": "test.md",
        "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sit amet orci id metus consequat gravida. Duis nec mauris laoreet, facilisis libero nec, tempus quam. Fusce eleifend tempus ipsum.",
        "published_at": "2025-12-22"
    },
    {
        "title": "Test Post #2",
        "slug": "test_2",
        "cover": "https://i.imgur.com/cXE2Lig.jpeg",
        "path": "test.md",
        "description": "Lorem ipsum dolor sit amet.",
        "published_at": "2025-12-22"
    }
]


def create_website():
    site = MySite()
    for post_data in ALL_POSTS:
        site.posts.append(BlogPost(post_data))

    return site


if __name__ == '__main__':
    environment = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')))

    site = create_website()
    site.render(environment)
