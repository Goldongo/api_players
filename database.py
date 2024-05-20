from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

IP_ADDRESS = "54.221.47.71"
PORT = "3306"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://usuario:contraseña@{IP_ADDRESS}:{PORT}/db_players"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
