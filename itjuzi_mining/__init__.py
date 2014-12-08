import settings
from models import DeclarativeBase
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

engine = create_engine(URL(**settings.DATABASE))
DeclarativeBase.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
