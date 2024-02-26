"""Comment model"""
import datetime as dt
import enum

from sqlalchemy import Column, Integer, String, Enum, DateTime

from src.extensions import db


class CommentStatus(enum.Enum):
    APPROVE = 1
    PEND = 2

    def __str__(self):
        return self.value


class Comment(db.Model):
    __tablename__ = "comments"
    id = Column(Integer(), nullable=False, primary_key=True, index=True)
    title = Column(String(length=64), nullable=False, index=True)
    comment = Column(String(length=1024), nullable=False, index=True)
    status = Column(Enum(CommentStatus), nullable=False, server_default="PEND")
    created_at = Column(
        DateTime(timezone=True),
        nullable=False,
        unique=False,
        default=dt.datetime.utcnow(),
    )
    updated_at = Column(
        DateTime(timezone=True),
        nullable=False,
        unique=False,
        default=dt.datetime.utcnow,
        onupdate=dt.datetime.utcnow,
    )
