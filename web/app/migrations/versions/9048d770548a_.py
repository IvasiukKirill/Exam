"""empty message

Revision ID: 9048d770548a
Revises: 
Create Date: 2023-01-25 11:43:28.699006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9048d770548a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('confers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('time', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_confers'))
    )
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tocken', sa.String(length=100), nullable=False),
    sa.Column('id_conf', sa.String(length=250), nullable=False),
    sa.Column('time', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tokens'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tokens')
    op.drop_table('confers')
    # ### end Alembic commands ###
