from app import app
import urllib.request, json

api_key = app.config[NEWS_API]

base_url = app.config[NEWS_BASE_URL]


def get_news(category):
    """
    Getting the json response
    :param category:
    :return:
    """
    get_news_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results=None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

        return news_results

def process_results(news_list):
    """
    Transforms the list into a list of objects
    :param news_list:
    :return:
    """

    news_results = []

    for news_item in news_list:
        source = news_item.get('source.name')
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        picture = news_item.get('urlToImage')
        time = news_item.get('publishedAt')

        news_object = News(source,title,author,description,picture,time)
        news_results.append(news_object)

    return news_results
