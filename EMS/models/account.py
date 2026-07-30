from sqlalchemy import Column,String
from database import Base
class Account(Base):
    __tablename__="accounts"
    username = Column(String,primary_key=True)
    password = Column(String)
    email = Column(String, unique=True, nullable=False)

