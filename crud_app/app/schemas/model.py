import pydantic


class Brand(pydantic.BaseModel):
  name: str

  model_config = pydantic.ConfigDict(extra='ignore')

