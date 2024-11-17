import pydantic


class Model(pydantic.BaseModel):
  name: str

  model_config = pydantic.ConfigDict(extra='ignore')

