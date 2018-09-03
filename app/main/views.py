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

    articles = get_news()
    title = 'highlights - News app'
    return render_template('index.html', title=title , articles = articles)
