import fastapi
from fastapi import logger
import logging
from sqlalchemy.orm import Session

from app import crud
from app import schemas

logger.logger.setLevel(logging.INFO)

def create_brand(db: Session, new_brand: schemas.Brand) -> schemas.Brand:
  logger.logger.info('Creating Brand: %s', new_brand.model_dump_json())
  existing_db_brand = crud.brand.get(db=db, id_=new_brand.name)
  if existing_db_brand is not None:
    raise fastapi.HTTPException(status_code=fastapi.status.HTTP_409_CONFLICT,
                                detail=f'Brand with name {new_brand.name} already exists')

  db_brand = crud.brand.create(db=db, obj_in=new_brand)
  return schemas.brand.model_validate(db_brand)

def get_brand(db: Session, brand_name: str) -> schemas.Brand:
  logger.logger.info('Getting Brand: %s', brand_name)
  db_brand = crud.brand.get(db=db, id_=brand_name)
  if db_brand is None:
    raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                detail=f'Brand with name {brand_name} not found')
  return schemas.Brand.model_validate(db_brand)

def get_brands(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.Brand]:
    logger.logger.info('Getting Brand List...')
    brands = crud.brand.get_multi(db, skip=skip, limit=limit)
    return [schemas.Brand.model_validate(brand) for brand in brands]
    
def remove_brand(db: Session, brand_name: str) -> schemas.Brand:
  logger.logger.info('Removing Brand: %s', brand_name)
  existing_db_brand = crud.brand.get(db, id_=brand_name)
  if existing_db_brand is None:
    raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                detail=f'Brand with name {brand_name} not found')

  return schemas.Brand.model_validate(crud.brand.remove(db=db, id_=brand_name))

