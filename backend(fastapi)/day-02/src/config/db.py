from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.config.settings import setting
base=declarative_base()
engine=create_engine(setting.DATABASE_URL)
LocalSession=sessionmaker(bind=engine)

def get_db():
    session=LocalSession()
    try:
        yield session
    finally:
        session.close()