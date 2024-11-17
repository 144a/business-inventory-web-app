import fastapi
from fastapi import logger
import logging
from sqlalchemy.orm import Session

from app import crud
from app import schemas

logger.logger.setLevel(logging.INFO)

def get_brand_list(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.Brand]:
    logger.logger.info('Getting Brand List...')
    brands = crud.brand.get_multi(db, skip=skip, limit=limit)
    return [schemas.Brand.model_validate(brand) for brand in brands]
    
    
    