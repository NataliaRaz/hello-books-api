"""add authors table and FK on books

Revision ID: 211e01d146d5
Revises: c988bf444a73
Create Date: 2025-05-06 21:48:57.995406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '211e01d146d5'
down_revision = 'c988bf444a73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'author', ['author_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('book', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('author_id')

    op.drop_table('author')
    # ### end Alembic commands ###
