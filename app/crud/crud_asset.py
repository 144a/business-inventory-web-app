from app.crud import base
from app import models
from app import schemas


class CRUDAsset(base.CRUDBase[models.Asset, schemas.Asset,
                                     schemas.Asset]):
  pass


asset = CRUDAsset(models.Asset)
