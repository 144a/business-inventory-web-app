import pydantic
import datetime


class AssetBase(pydantic.BaseModel):
  id: str

  model_config = pydantic.ConfigDict(extra='ignore')


class Asset(AssetBase):
  model_id = str
  type: str
  serial_number: str
  hours_state = str
  is_working = bool
  description: str
  is_fixed_asset: bool
  is_barcode_generated: bool
  created_at: datetime.datetime
  sold_at: datetime.datetime
  initial_cost: float
    
  
  model_config = pydantic.ConfigDict(from_attributes=True, extra='ignore')


