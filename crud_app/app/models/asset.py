import datetime
from sqlalchemy import Column, DateTime, String, Boolean
from app.db.base_class import Base


class Asset(Base):
  id = Column(String, primary_key=True, index=True, nullable=False)
  asset_type = Column(String, nullable=False, index=True)
  description = Column(String, nullable=True, index=True)
  is_barcode_generated = Column(Boolean, unique=False, default=False, nullable=False)
  created_at = Column(
      DateTime,
      default=datetime.datetime.now(),
  )
  sold_at = Column(DateTime, nullable=True)
