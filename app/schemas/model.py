import pydantic
import uuid
from app import enums

class Model(pydantic.BaseModel):
    id: uuid.UUID
    type: str
    name: str
    description: str

    model_config = pydantic.ConfigDict(extra="ignore")

class ModelTags(pydantic.BaseModel):
    id: uuid.UUID
    sub_model: str
    brand: str
    display_type: enums.DisplayTypeEnum
    is_display_hd: bool
    is_display_240p: bool
    equipment_type: str
    operational_hours: int
    head_count: int
    supports_sdi: bool
    supports_composite: bool
    supports_component: bool
    supports_svideo: bool
    supports_RGB: bool
    supports_RGBHV: bool
    
    model_config = pydantic.ConfigDict(extra="ignore")