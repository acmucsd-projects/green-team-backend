import os
from dotenv import load_dotenv
from string import Template

load_dotenv()

postgres_uri_template = Template("postgres://${username}:${password}@${host}:${port}/${database}")
postgres_uri = postgres_uri_template.safe_substitute(
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    database=os.environ["DB_DATABASE"]
)

class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = postgres_uri
    MAX_CONTENT_LENGTH = 512 * 1024

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}