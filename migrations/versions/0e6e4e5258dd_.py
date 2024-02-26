"""empty message

Revision ID: 0e6e4e5258dd
Revises: 
Create Date: 2024-02-26 22:24:36.459011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e6e4e5258dd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=False),
    sa.Column('comment', sa.String(length=1024), nullable=False),
    sa.Column('status', sa.Enum('APPROVE', 'PEND', name='commentstatus'), server_default='PEND', nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_comments_comment'), ['comment'], unique=False)
        batch_op.create_index(batch_op.f('ix_comments_id'), ['id'], unique=False)
        batch_op.create_index(batch_op.f('ix_comments_title'), ['title'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('comments', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_comments_title'))
        batch_op.drop_index(batch_op.f('ix_comments_id'))
        batch_op.drop_index(batch_op.f('ix_comments_comment'))

    op.drop_table('comments')
    # ### end Alembic commands ###
