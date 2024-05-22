from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:Ut3c9208@database-1.c4lofrzrpfew.us-east-1.rds.amazonaws.com:3306/api_players"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Cambia esto a tu URL de base de datos

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
