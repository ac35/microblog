"""new fields in user model

Revision ID: 767c8b0d74a4
Revises: a1dcccded6fa
Create Date: 2018-06-17 10:23:14.296052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '767c8b0d74a4'
down_revision = 'a1dcccded6fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
