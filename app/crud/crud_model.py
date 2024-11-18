from app.crud import base
from app import models
from app import schemas
from sqlalchemy.orm import Session


class CRUDModel(base.CRUDBase[models.Model, schemas.Model,
                                     schemas.Model]):
  def get_by_name(self, db: Session) -> models.TermsAndConditions | None:
    return (db.query(models.Model.name).first())

model = CRUDModel(models.Model)
