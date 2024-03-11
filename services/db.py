from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database

db_name = "casino"
url = f"mysql+mysqldb://root@localhost/{db_name}"

if not database_exists(url):
    create_database(url)

engine = create_engine(url, echo=True)
session = Session(bind=engine, autocommit=False, autoflush=True)
