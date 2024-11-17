from sqlalchemy import Column, String, Boolean, Float
from sqlalchemy import Column, ForeignKey
from app.db.base_class import Base

class Brand(Base):
    name = Column(String, unique=True, primary_key=True, nullable=False)