"""empty message

Revision ID: 196249230a82
Revises: a4c9cba14570
Create Date: 2022-09-22 05:37:44.919575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '196249230a82'
down_revision = 'a4c9cba14570'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Duty', sa.Column('dog_id', sa.Integer(), nullable=True))
    op.drop_constraint('Duty_dog_id_id_fkey', 'Duty', type_='foreignkey')
    op.create_foreign_key(None, 'Duty', 'Dog', ['dog_id'], ['id'])
    op.drop_column('Duty', 'dog_id_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Duty', sa.Column('dog_id_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Duty', type_='foreignkey')
    op.create_foreign_key('Duty_dog_id_id_fkey', 'Duty', 'Dog', ['dog_id_id'], ['id'])
    op.drop_column('Duty', 'dog_id')
    # ### end Alembic commands ###