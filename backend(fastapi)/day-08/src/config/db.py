from sqlalchemy import create_engine
from src.config.settings import settings
from sqlalchemy.orm import sessionmaker,declarative_base

base=declarative_base()
engine=create_engine(settings.DATABASE_URL)
LocalSession=sessionmaker(bind=engine)

def get_db():
    session=LocalSession()
    try:
        yield session
    finally:
        session.close()



