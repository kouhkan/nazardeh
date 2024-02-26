"""Application extensions."""

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app=None)
migrate = Migrate(app=None, db=db)


__all__ = [db, migrate]
