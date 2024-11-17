import datetime
from sqlalchemy import Column, DateTime, String, Boolean, Float
from sqlalchemy import Column, Enum, ForeignKey
from crud_app.app.db.base_class import Base


class Asset(Base):
  id = Column(String, primary_key=True, index=True, nullable=False)
  # model_id = Column(String, ForeignKey('model.id'), nullable=True)
  # type = Column(String, ForeignKey('assetType.type'), nullable=True)
  serial_number = Column(String, nullable=True)
  hours_state = Column(String, nullable=True)
  is_working = Column(Boolean, default=False, nullable=False)
  is_fixed_asset = Column(Boolean, default=False, nullable=False)
  description = Column(String, nullable=False)
  is_barcode_generated = Column(Boolean, unique=False, default=False, nullable=False)
  created_at = Column(
      DateTime,
      default=datetime.datetime.now(),
  )
  sold_at = Column(DateTime, nullable=True)
  initial_cost = Column(Float, default=0, nullable=False)
