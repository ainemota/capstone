"""empty message

Revision ID: f9aee1cb46d7
Revises: 
Create Date: 2022-05-03 23:51:03.817353

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f9aee1cb46d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('addresses',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('CEP', sa.String(), nullable=False),
    sa.Column('number', sa.String(length=8), nullable=True),
    sa.Column('complement', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('address_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('locator_id', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('address_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['address_id'], ['addresses.id'], ),
    sa.ForeignKeyConstraint(['locator_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.String(length=15), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('locator_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['locator_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rooms_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('rooms_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['rooms_id'], ['rooms.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rooms_categories')
    op.drop_table('products')
    op.drop_table('rooms')
    op.drop_table('users')
    op.drop_table('categories')
    op.drop_table('addresses')
    # ### end Alembic commands ###