import fastapi
from fastapi import logger
import logging
from sqlalchemy.orm import Session

from app import crud
from app import schemas

import uuid

logger.logger.setLevel(logging.INFO)


def create_model(db: Session, new_model: schemas.Model) -> schemas.Model:
    logger.logger.info("Creating model: %s", new_model.model_dump_json())
    existing_db_model = crud.model.get(db=db, id_=new_model.id)
    if existing_db_model is not None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_409_CONFLICT,
            detail=f"model with id {new_model.id} already exists",
        )

    db_model = crud.model.create(db=db, obj_in=new_model)
    return schemas.Model.model_validate(db_model)


def get_model(db: Session, model_id: uuid.UUID) -> schemas.Model:
    logger.logger.info("Getting model: %s", model_id)
    db_model = crud.model.get(db=db, id_=model_id)
    if db_model is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=f"model with id {model_id} not found",
        )
    return schemas.Model.model_validate(db_model)


def get_model_by_name(db: Session, model_name: str) -> schemas.Model:
    logger.logger.info("Getting model: %s", model_name)
    db_model = crud.model.get_by_name(db=db, model_name=model_name)
    if db_model is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=f"model with name {model_name} not found",
        )
    return schemas.Model.model_validate(db_model)


def get_models(db: Session, skip: int = 0, limit: int = 100) -> list[schemas.Model]:
    logger.logger.info("Getting model List...")
    models = crud.model.get_multi(db, skip=skip, limit=limit)
    return [schemas.Model.model_validate(model) for model in models]


def remove_model(db: Session, model_id: uuid.UUID) -> schemas.Model:
    logger.logger.info("Removing model: %s", model_id)
    existing_db_model = crud.model.get(db, id_=model_id)
    if existing_db_model is None:
        raise fastapi.HTTPException(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            detail=f"model with id {model_id} not found",
        )

    return schemas.Model.model_validate(crud.model.remove(db=db, id_=model_id))
