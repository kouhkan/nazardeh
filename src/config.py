"""Application's configuration."""

import os

from dotenv import load_dotenv

load_dotenv()


class Base:
    """Base Configuration Object."""

    DEBUG = False
    TESTING = False
    _DB_USER = os.getenv("DB_USER")
    _DB_PASS = os.getenv("DB_PASS")
    _DB_HOST = os.getenv("DB_HOST")
    _DB_PORT = os.getenv("DB_PORT")
    _DB_NAME = os.getenv("DB_NAME")
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{_DB_USER}:{_DB_PASS}@{_DB_HOST}:{_DB_PORT}/{_DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class Development(Base):
    """Development Configuration Object."""

    DEBUG = True


class Testing(Base):
    """Testing Configuration Object."""

    DEBUG = True
    TESTING = True


class Production(Base):
    """Production Configuration Object."""

    pass


def get_config_from_environment_variable():
    """Get configuration object name from `CONF` env var and get lookup configuration object with the name."""
    config_name = os.getenv("CONF", "base")
    return {
        "base": Base,
        "dev": Development,
        "testing": Testing,
        "prod": Production,
    }.get(config_name.lower(), Base)
