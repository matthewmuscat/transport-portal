"""empty message

Revision ID: f16052e671d9
Revises: bbff8a326f63
Create Date: 2018-05-27 00:16:52.265666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f16052e671d9'
down_revision = 'bbff8a326f63'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('kpm_trucks', 'model',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('mr_trucks', 'model',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('mr_trucks', 'model',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('kpm_trucks', 'model',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
