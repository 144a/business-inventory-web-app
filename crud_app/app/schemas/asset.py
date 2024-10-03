import pydantic
import datetime


class AssetBase(pydantic.BaseModel):
  id: str

  model_config = pydantic.ConfigDict(extra='ignore')


class Asset(AssetBase):
  description: str
  is_barcode_generated: bool
  created_at: datetime.datetime
  sold_at: datetime.datetime

  model_config = pydantic.ConfigDict(from_attributes=True, extra='ignore')
