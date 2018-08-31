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
    get_news_url = base_url.format(category, apikey)

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
        source = 
        title =
        description =
        picture =
        time =
