import pytest
from sqlalchemy.orm import Session
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from app import schemas
from app.service import model_service
import uuid

@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def model_schema():
    return schemas.Model(id=uuid.uuid4(), type="Monitor", name="Testmodel", description="Test Monitor")

@pytest.fixture
def mock_crud():
    with patch("app.crud.model") as mocked_crud:
        yield mocked_crud

def test_create_model_success(mock_db, model_schema, mock_crud):
    mock_crud.get.return_value = None
    mock_crud.create.return_value = model_schema

    result = model_service.create_model(mock_db, model_schema)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=model_schema.id)
    mock_crud.create.assert_called_once_with(db=mock_db, obj_in=model_schema)
    assert result == model_schema

def test_create_model_conflict(mock_db, model_schema, mock_crud):
    mock_crud.get.return_value = model_schema

    with pytest.raises(HTTPException) as exc_info:
        model_service.create_model(mock_db, model_schema)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=model_schema.id)
    assert exc_info.value.status_code == 409
    assert "already exists" in exc_info.value.detail

def test_get_model_success(mock_db, model_schema, mock_crud):
    mock_crud.get.return_value = model_schema

    result = model_service.get_model(mock_db, model_schema.id)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=model_schema.id)
    assert result == model_schema

def test_get_model_not_found(mock_db, model_schema, mock_crud):
    mock_crud.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        model_service.get_model(mock_db, model_schema.id)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=model_schema.id)
    assert exc_info.value.status_code == 404
    assert "not found" in exc_info.value.detail

def test_get_models(mock_db, mock_crud):
    mock_crud.get_multi.return_value = [schemas.Model(id=uuid.uuid4(), type="Monitor", name="Testmodel1", description="Test Monitor1"), schemas.Model(id=uuid.uuid4(), type="Monitor", name="Testmodel2", description="Test Monitor2")]

    result = model_service.get_models(mock_db, skip=0, limit=100)

    mock_crud.get_multi.assert_called_once_with(mock_db, skip=0, limit=100)
    assert len(result) == 2
    assert result[0].name == "Testmodel1"
    assert result[1].name == "Testmodel2"

def test_remove_model_success(mock_db, model_schema, mock_crud):
    mock_crud.get.return_value = model_schema
    mock_crud.remove.return_value = model_schema

    result = model_service.remove_model(mock_db, model_schema.id)

    mock_crud.get.assert_called_once_with(mock_db, id_=model_schema.id)
    mock_crud.remove.assert_called_once_with(db=mock_db, id_=model_schema.id)
    assert result == model_schema

def test_remove_model_not_found(mock_db, model_schema, mock_crud):
    mock_crud.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        model_service.remove_model(mock_db, model_schema.id)

    mock_crud.get.assert_called_once_with(mock_db, id_=model_schema.id)
    assert exc_info.value.status_code == 404
    assert "not found" in exc_info.value.detail