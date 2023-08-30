from sqlalchemy import Column, TEXT, INT, BIGINT, DATETIME, INTEGER
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    name = Column(TEXT, nullable=False)
    age = Column(INT, nullable=False)
    created_at = Column(DATETIME, nullable=False, default=datetime.now)
    update_time = Column(DATETIME, onupdate=datetime.now, default=datetime.now)


