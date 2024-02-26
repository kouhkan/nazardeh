from flask import request

from src.extensions import db
from src.models import Comment
from . import comment
from .serializers import comment_schema


@comment.route("/", methods=["POST"])
def create_comment():
    data = request.get_json()
    comment_instance = Comment(title=data["title"], comment=data["comment"])
    db.session.add(comment_instance)
    db.session.commit()
    return comment_schema.dump(comment_instance), 201
