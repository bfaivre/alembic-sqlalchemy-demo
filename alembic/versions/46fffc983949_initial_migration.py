"""Initial migration.

Revision ID: 46fffc983949
Revises: 
Create Date: 2020-09-24 21:54:46.153463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '46fffc983949'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Fv',
    sa.Column('FvId', sa.Integer(), nullable=False),
    sa.Column('Name', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('FvId'),
    sa.UniqueConstraint('Name', name='AK__Name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Fv')
    # ### end Alembic commands ###