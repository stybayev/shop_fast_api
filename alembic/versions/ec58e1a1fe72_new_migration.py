"""New Migration

Revision ID: ec58e1a1fe72
Revises: fd3e4b322ff8
Create Date: 2022-11-19 15:41:06.540293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec58e1a1fe72'
down_revision = 'fd3e4b322ff8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('order_visit_id_fkey', 'order', type_='foreignkey')
    op.drop_column('order', 'visit_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('visit_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('order_visit_id_fkey', 'order', 'visit', ['visit_id'], ['id'])
    # ### end Alembic commands ###