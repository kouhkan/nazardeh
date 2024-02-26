from marshmallow import fields

from src.extensions import ma
from src.models import Comment
from src.models.comment import CommentStatus


class CommentsSchema(ma.SQLAlchemyAutoSchema):
    status = fields.Enum(CommentStatus)

    class Meta:
        model = Comment

    id = ma.auto_field()
    title = ma.auto_field()
    comment = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()


comment_schema = CommentsSchema()
