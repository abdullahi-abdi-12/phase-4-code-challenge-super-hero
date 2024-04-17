"""message

Revision ID: f32f7b7f0ce3
Revises: b978a70ef1ff
Create Date: 2024-04-16 09:04:26.055760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f32f7b7f0ce3'
down_revision = 'b978a70ef1ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hero_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('power_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_hero_powers_hero_id_heroes'), 'heroes', ['hero_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_hero_powers_power_id_powers'), 'powers', ['power_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hero_powers', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_hero_powers_power_id_powers'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_hero_powers_hero_id_heroes'), type_='foreignkey')
        batch_op.drop_column('power_id')
        batch_op.drop_column('hero_id')

    # ### end Alembic commands ###
