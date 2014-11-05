import sqlalchemy

def upgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    images = sqlalchemy.Table('images', meta, autoload=True)
    parent_id = sqlalchemy.Column('parent_id',
                                     sqlalchemy.String(36))
    images.create_column(parent_id)


def downgrade(migrate_engine):
    meta = sqlalchemy.MetaData()
    meta.bind = migrate_engine

    images = sqlalchemy.Table('images', meta, autoload=True)
    images.columns['parent_id'].drop()
