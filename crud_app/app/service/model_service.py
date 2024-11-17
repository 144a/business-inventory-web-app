import fastapi
from fastapi import logger
import logging
from sqlalchemy.orm import Session

from app import crud
from app import schemas

logger.logger.setLevel(logging.INFO)

def get_user(db: Session, brand_name: str) -> schemas.Brand:
  logger.logger.info('Getting Brand: %s', brand_name)
  db_brand = crud.brand.get(db=db, id_=brand_name)
  if db_brand is None:
    raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                detail=f'User with id {brand_name} not found')
  return schemas.Brand.model_validate(db_brand)

def get_brand_list(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.Brand]:
    logger.logger.info('Getting Brand List...')
    brands = crud.brand.get_multi(db, skip=skip, limit=limit)
    return [schemas.Brand.model_validate(brand) for brand in brands]
    
def remove_brand(db: Session, brand_name: str) -> schemas.Brand:
  logger.logger.info('Removing Brand: %s', brand_name)
  existing_db_brand = crud.brand.get(db, id_=brand_name)
  if existing_db_brand is None:
    raise fastapi.HTTPException(status_code=fastapi.status.HTTP_404_NOT_FOUND,
                                detail=f'User with id {brand_name} not found')

  return schemas.Brand.model_validate(crud.brand.remove(db=db, id_=brand_name))

