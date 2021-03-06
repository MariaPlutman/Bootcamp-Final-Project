"""empty message

Revision ID: 3066193a420b
Revises: 
Create Date: 2020-09-01 20:40:24.679944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3066193a420b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('request',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('client_id', sa.String(length=50), nullable=False),
    sa.Column('school_name', sa.String(length=50), nullable=True),
    sa.Column('school_id', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('problem', sa.String(length=100), nullable=False),
    sa.Column('status', sa.String(length=100), nullable=False),
    sa.Column('message', sa.String(length=100), nullable=False),
    sa.Column('project', sa.String(length=100), nullable=False),
    sa.Column('r_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=300), nullable=True),
    sa.Column('password', sa.String(length=500), nullable=True),
    sa.Column('name', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('request')
    # ### end Alembic commands ###
