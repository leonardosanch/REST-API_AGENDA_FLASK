"""adding login table

Revision ID: 1c5b8c038b45
Revises: ca1f83395bf1
Create Date: 2023-09-28 21:35:18.713382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c5b8c038b45'
down_revision = 'ca1f83395bf1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario', sa.String(length=50), nullable=True),
    sa.Column('clave', sa.String(length=250), nullable=True),
    sa.Column('nivel', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('login')
    # ### end Alembic commands ###
