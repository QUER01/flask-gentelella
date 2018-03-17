from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config


db = SQLAlchemy()
engine = create_engine(
    'postgresql+psycopg2://'+Config.POSTGRES_USER+':'+Config.POSTGRES_PW+'@'+Config.POSTGRES_URL+'/'+Config.POSTGRES_DB,
    convert_unicode=True,
    echo=True
)
#engine = create_engine(
#    'sqlite:///database.db',
#    convert_unicode=True,
#    echo=True
#)

db.session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base()
Base.query = db.session.query_property()


def create_database():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.
    Base.metadata.create_all(bind=engine)
