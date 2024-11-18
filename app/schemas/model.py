import pydantic
import uuid


class Model(pydantic.BaseModel):
  id: uuid.UUID
  type: str
  name: str
  description: str

  model_config = pydantic.ConfigDict(extra='ignore')

