class Config(object):
    API_PORT = 9900
    MONGO_URL = "mongodb://localhost:27017/"

class DevelopmentConfig(Config):
    API_PORT = 9901
    DEBUG = True

class TestingConfig(Config):
    API_PORT = 9902
    TESTING = True

class StagingConfig(Config):
    API_PORT = 9903
    TESTING = True

class ProductionConfig(Config):
    API_PORT = 9904
    DEBUG = False
    TESTING = False
