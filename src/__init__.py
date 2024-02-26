"""Register Flask app."""

from flask import Flask


def create_app(config=None):
    """Application factory."""
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    _register_configurations(app, config)
    _register_extensions(app)
    _register_modules(app)

    return app


def _register_configurations(app: Flask, config: None):
    from src.config import get_config_from_environment_variable

    app.config.from_object(config or get_config_from_environment_variable())


def _register_extensions(app: Flask):
    from src.extensions import __all__ as extensions

    for extension in extensions:
        extension.init_app(app)


def _register_modules(app: Flask):
    from src.modules import __all__ as modules

    for module in modules:
        app.register_blueprint(module)
