import os
from dotenv import load_dotenv
from string import Template

load_dotenv()

local_postgres_uri_template = Template("postgres://${username}:${password}@${host}:${port}/${database}")
local_postgres_uri = local_postgres_uri_template.safe_substitute(
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    port=os.environ["DB_PORT"],
    database=os.environ["DB_DATABASE"]
)
# production_postgres_uri = TBD

class Config:
    DEBUG = False
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = local_postgres_uri

class ProductionConfig(Config):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = production_postgres_uri

config_by_name = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}