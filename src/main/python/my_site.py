from blog_post import BlogPost
from utils import my_write

import math


PAGE_SIZE = 15
RECENT_COUNT = 15


class MySite:
    def __init__(self):
        self.posts = []

    def render(self, environment):
        self.render_index(environment)
        self.render_posts_list(environment)
        for post in self.posts:
            post.render(environment)

    def render_index(self, environment):
        template = environment.get_template('index.html')
        my_write(
            'index.html', 
            template.render(
                featured_posts=self.get_featured_posts(), 
                recent_posts=self.get_recent_posts()))
        
    def render_posts_list(self, environment):
        template = environment.get_template('posts_list.html')
        index = 0
        current_page = 0
        ordered_posts = self.get_ordered_posts()
        total_pages = int(math.ceil(len(ordered_posts) / PAGE_SIZE))
        while index < len(ordered_posts):
            posts = ordered_posts[index : index + PAGE_SIZE]
            index += PAGE_SIZE
            current_page += 1
            my_write(
                'posts_%d.html' % current_page, 
                template.render(
                    title="All posts",
                    posts=posts, 
                    current_page=current_page,
                    total_pages=total_pages))


    def get_featured_posts(self):
        return self.posts
    
    def get_recent_posts(self):
        return self.get_ordered_posts()[:RECENT_COUNT]
    
    def get_ordered_posts(self):
        return self.posts * 100
