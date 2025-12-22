class BlogPost:
    def __init__(self, title, path):
        self.title = title
        self.path = path

    def render(self, environment):
        pass

    @staticmethod
    def create(data):
        return BlogPost(title=data['title'], path=data['path'])
