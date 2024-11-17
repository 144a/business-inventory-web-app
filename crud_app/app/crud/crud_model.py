from app.crud import base
from app import models
from app import schemas


class CRUDBrand(base.CRUDBase[models.Brand, schemas.Brand,
                                     schemas.Brand]):
  pass


asset = CRUDBrand(models.Asset)
