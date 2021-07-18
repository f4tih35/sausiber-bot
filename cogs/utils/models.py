from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Entry(Base):
    __tablename__ = "entries"
    id = Column(Integer, primary_key=True, unique=True)
    gid = Column(String(250), nullable=False, unique=True)
    title = Column(String(250))
    content = Column(String(250))
    url = Column(String(250))