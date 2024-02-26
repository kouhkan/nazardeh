"""Application extensions."""
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app=None)
ma = Marshmallow(app=None)
migrate = Migrate(app=None, db=db)

__all__ = [db, ma, migrate]
