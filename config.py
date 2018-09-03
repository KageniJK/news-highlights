import os


class Config:
    """
    General config
    """
    NEWS_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    # NEWS_API_KEY = os.environ.get('NEWS_API')
    NEWS_API_KEY = '60c409df26d84542840fcc90b1777526'


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
