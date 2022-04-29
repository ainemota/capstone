"""empty message

Revision ID: 2c925090317b
Revises: 
Create Date: 2022-04-29 10:02:03.621161

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2c925090317b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.Column('city', sa.String(length=20), nullable=True),
    sa.Column('street', sa.String(length=20), nullable=True),
    sa.Column('number', sa.String(length=8), nullable=True),
    sa.Column('complement', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=15), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('address_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('users')
    op.drop_table('addresses')
    # ### end Alembic commands ###
