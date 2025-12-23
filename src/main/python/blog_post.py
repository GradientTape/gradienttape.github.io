import os
from utils import my_write


def read_post_data(path):
    with open(os.path.join(os.path.dirname(__file__), '../../../data', path)) as f:
        text = f.read()
        return text


class BlogPost:
    def __init__(self, data):
        self.title = data['title']
        self.slug = data['slug']
        self.description = data['description']
        self.published_at = data['published_at']
        self.cover_img = data.get('cover')
        self.text = read_post_data(data['path'])

    def render(self, environment):
        template = environment.get_template('post.html')
        my_write(
            './posts/%s.html' % self.slug, 
            template.render(
                title=self.title, 
                cover_img=self.cover_img,
                text=self.text))

