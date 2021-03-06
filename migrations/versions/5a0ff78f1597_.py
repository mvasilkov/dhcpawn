"""empty message

Revision ID: 5a0ff78f1597
Revises: 2c998c3f8312
Create Date: 2015-05-02 12:24:12.279699

"""

# revision identifiers, used by Alembic.
revision = '5a0ff78f1597'
down_revision = '2c998c3f8312'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('range',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=255), nullable=True),
    sa.Column('min', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),
    sa.Column('max', sqlalchemy_utils.types.ip_address.IPAddressType(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('subnet_id', sa.Integer(), nullable=True),
    sa.Column('range_id', sa.Integer(), nullable=True),
    sa.Column('options', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['range_id'], ['range.id'], ),
    sa.ForeignKeyConstraint(['subnet_id'], ['subnet.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'IP', sa.Column('host_id', sa.Integer(), nullable=True))
    op.add_column(u'IP', sa.Column('range_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'IP', 'host', ['host_id'], ['id'])
    op.create_foreign_key(None, 'IP', 'range', ['range_id'], ['id'])
    op.add_column(u'group', sa.Column('options', sa.Text(), nullable=True))
    op.add_column(u'host', sa.Column('options', sa.Text(), nullable=True))
    op.add_column(u'subnet', sa.Column('options', sa.Text(), nullable=True))
    op.add_column(u'subnet', sa.Column('range_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'subnet', 'range', ['range_id'], ['id'])
    op.drop_column(u'subnet', 'routers')
    op.drop_column(u'subnet', 'broadcast_address')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'subnet', sa.Column('broadcast_address', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column(u'subnet', sa.Column('routers', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'subnet', type_='foreignkey')
    op.drop_column(u'subnet', 'range_id')
    op.drop_column(u'subnet', 'options')
    op.drop_column(u'host', 'options')
    op.drop_column(u'group', 'options')
    op.drop_constraint(None, 'IP', type_='foreignkey')
    op.drop_constraint(None, 'IP', type_='foreignkey')
    op.drop_column(u'IP', 'range_id')
    op.drop_column(u'IP', 'host_id')
    op.drop_table('pool')
    op.drop_table('range')
    ### end Alembic commands ###
