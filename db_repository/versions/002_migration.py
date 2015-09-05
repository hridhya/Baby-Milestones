from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
baby = Table('baby', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('babyname', String(length=64)),
    Column('birthdate', String(length=64)),
    Column('gender', String(length=64)),
    Column('user_id', Integer),
)

milestones = Table('milestones', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('milestonedate', String(length=64)),
    Column('title', String(length=64)),
    Column('baby_id', Integer),
    Column('details', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['baby'].create()
    post_meta.tables['milestones'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['baby'].drop()
    post_meta.tables['milestones'].drop()
