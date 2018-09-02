from flask import render_template
from ..requests import get_news
from . import main
from ..models import News_article

@main.route('/')
def index():
    """
    View root page
    :return:
    """

    news_highlights = get_news('top-headlines?country=us&')
    print(news_highlights)
    title = 'Highlights - News app'
    return render_template('index.html', title=title)
