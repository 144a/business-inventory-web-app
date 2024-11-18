from sqlalchemy import Column, String, UUID
from app.db.base_class import Base


class Model(Base):
    id = Column(UUID, unique=True, primary_key=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
