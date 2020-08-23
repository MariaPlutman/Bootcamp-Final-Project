"""empty message

Revision ID: d3a927ad3dc1
Revises: 
Create Date: 2020-08-23 18:35:39.655496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3a927ad3dc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('citizen_id', sa.String(length=9), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('school_sign', sa.String(length=6), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('citizen_id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=100), nullable=False),
    sa.Column('message', sa.Text(length=2000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('request')
    op.drop_table('project')
    op.drop_table('client')
    # ### end Alembic commands ###
