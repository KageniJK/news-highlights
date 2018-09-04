class NewsArticle:
    """
    News article class
    """

    def __init__(self, source,title,author,description,picture,time,link):
        self.source = source
        self.title= title
        self.author = author
        self.description = description
        self.picture = picture
        self.time = time
        self.link = link


class NewsSource:
    """
    News source class
    """

    def __init__(self, name, link, category):
        self.name = name
        self.link = link
        self.category = category
