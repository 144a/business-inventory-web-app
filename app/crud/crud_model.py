from app.crud import base
from app import models
from app import schemas
from sqlalchemy.orm import Session


class CRUDModel(base.CRUDBase[models.Model, schemas.Model, schemas.Model]):
    def get_by_name(self, db: Session, model_name: str) -> models.Model | None:
        return db.query(models.Model).filter(models.Model.name == model_name).all()


model = CRUDModel(models.Model)
