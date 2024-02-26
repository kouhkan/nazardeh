"""Comments CRUD"""
from src.extensions import db
from src.models import Comment


def generate_comment(title: str, comment: str) -> Comment:
    comment = Comment(title=title, comment=comment)

    db.session.add(comment)
    db.session.commit()

    return comment
