from sqlalchemy import Column, String, UUID, ForeignKey, Enum, Boolean, Integer
from app.db.base_class import Base
from app import enums


class Model(Base):
    id = Column(UUID, unique=True, primary_key=True, index=True, nullable=False)
    type = Column(String, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class ModelTags():
    id  = Column(UUID, ForeignKey('model.id'), unique=True, primary_key=True, index=True, nullable=False)
    sub_model = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    display_type = Column(Enum(enums.DisplayTypeEnum), nullable=True)
    is_display_hd = Column(Boolean, nullable=True)
    is_display_240p = Column(Boolean, nullable=True)
    equipment_type = Column(String, nullable=True)
    operational_hours = Column(Integer, nullable=True)
    head_count = Column(Integer, nullable=True)
    supports_sdi = Column(Boolean, nullable=True)
    supports_composite = Column(Boolean, nullable=True)
    supports_component = Column(Boolean, nullable=True)
    supports_svideo = Column(Boolean, nullable=True)
    supports_RGB = Column(Boolean, nullable=True)
    supports_RGBHV = Column(Boolean, nullable=True)