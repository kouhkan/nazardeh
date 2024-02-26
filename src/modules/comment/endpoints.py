from flask import request

from . import comment
from .crud import generate_comment
from .serializers import comment_schema


@comment.route("/", methods=["POST"])
def create_comment():
    data = request.get_json()
    comment_instance = generate_comment(data["title"], data["comment"])
    return comment_schema.dump(comment_instance), 201
