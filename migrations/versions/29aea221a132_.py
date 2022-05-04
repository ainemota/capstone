"""empty message

Revision ID: 29aea221a132
Revises: f9aee1cb46d7
Create Date: 2022-05-04 00:21:55.001938

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '29aea221a132'
down_revision = 'f9aee1cb46d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rentals',
    sa.Column('rental_id', sa.Integer(), nullable=False),
    sa.Column('lessee_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('lease_price_unit', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['lessee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('rental_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rentals')
    # ### end Alembic commands ###
