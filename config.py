import os
from dotenv import load_dotenv
load_dotenv()



class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = False