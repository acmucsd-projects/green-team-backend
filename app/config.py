import os
from dotenv import load_dotenv

load_dotenv()

# Any way to make this url cleaner?
local_postgres_uri = "postgres://" + os.environ["DB_USER"] + ":" + os.environ["DB_PASSWORD"] + "@" + os.environ["DB_HOST"] + ":" + os.environ["DB_PORT"] + "/" + os.environ["DB_DATABASE"]
# production_postgres_uri = TBD

class Config:
    DEBUG = False
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = local_postgres_uri

class ProductionConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = production_postgres_uri

config_by_name = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}
key = Config.SECRET_KEY