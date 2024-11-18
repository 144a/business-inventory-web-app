import pydantic
import datetime


class Asset(pydantic.BaseModel):
  id: str
  #model_id: str
  #type: str
  serial_number: str
  hours_stat: str
  is_working: bool
  description: str
  is_fixed_asset: bool
  is_barcode_generated: bool
  created_at: datetime.datetime
  sold_at: datetime.datetime
  initial_cost: float
    
  
  model_config = pydantic.ConfigDict(from_attributes=True, extra='ignore')


