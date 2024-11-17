from app.crud import base
from app import models
from app import schemas


class CRUDModel(base.CRUDBase[models.Model, schemas.Model,
                                     schemas.Model]):
  pass


model = CRUDModel(models.Model)
