from blog_post import BlogPost
from utils import my_write


class MySite:
    def __init__(self):
        self.posts = []

    def render(self, environment):
        template = environment.get_template('index.html')
        my_write('index.html', template.render())

        for post in self.posts:
            post.render(environment)
