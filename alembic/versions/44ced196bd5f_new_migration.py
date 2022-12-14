"""New Migration

Revision ID: 44ced196bd5f
Revises: b7a85401827a
Create Date: 2022-11-19 16:03:33.321872

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '44ced196bd5f'
down_revision = 'b7a85401827a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('order', 'created_at')
    op.drop_column('order', 'expiration_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('expiration_data', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    op.add_column('order', sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
