"""adding column locator_id to products table

Revision ID: a25819ea0015
Revises: 2c925090317b
Create Date: 2022-04-29 10:14:40.143259

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a25819ea0015'
down_revision = '2c925090317b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('locator_id', postgresql.UUID(as_uuid=True), nullable=False))
    op.create_foreign_key(None, 'products', 'users', ['locator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'locator_id')
    # ### end Alembic commands ###
