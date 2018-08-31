from flask import render_template
from app import app
from app.requests import get_news

@app.route('/')
def index():
    """
    View root page
    :return:
    """

    news_highlights = get_news('top-headlines?country=us&')
    print(news_highlights)
    title = 'Highlights - News app'
    return render_template('index.html', title=title)