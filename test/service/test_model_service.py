import pytest
from sqlalchemy.orm import Session
from unittest.mock import MagicMock, patch
from fastapi import HTTPException
from app import schemas
from app.service import model_service


@pytest.fixture
def mock_db():
    return MagicMock()

@pytest.fixture
def brand_schema():
    return schemas.Brand(name="TestBrand")

@pytest.fixture
def mock_crud():
    with patch("app.crud.brand") as mocked_crud:
        yield mocked_crud

def test_create_brand_success(mock_db, brand_schema, mock_crud):
    mock_crud.get.return_value = None
    mock_crud.create.return_value = brand_schema

    result = model_service.create_brand(mock_db, brand_schema)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=brand_schema.name)
    mock_crud.create.assert_called_once_with(db=mock_db, obj_in=brand_schema)
    assert result == brand_schema

def test_create_brand_conflict(mock_db, brand_schema, mock_crud):
    mock_crud.get.return_value = brand_schema

    with pytest.raises(HTTPException) as exc_info:
        model_service.create_brand(mock_db, brand_schema)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=brand_schema.name)
    assert exc_info.value.status_code == 409
    assert "already exists" in exc_info.value.detail

def test_get_brand_success(mock_db, brand_schema, mock_crud):
    mock_crud.get.return_value = brand_schema

    result = model_service.get_brand(mock_db, brand_schema.name)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=brand_schema.name)
    assert result == brand_schema

def test_get_brand_not_found(mock_db, brand_schema, mock_crud):
    mock_crud.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        model_service.get_brand(mock_db, brand_schema.name)

    mock_crud.get.assert_called_once_with(db=mock_db, id_=brand_schema.name)
    assert exc_info.value.status_code == 404
    assert "not found" in exc_info.value.detail

def test_get_brands(mock_db, mock_crud):
    mock_crud.get_multi.return_value = [schemas.Brand(name="Brand1"), schemas.Brand(name="Brand2")]

    result = model_service.get_brands(mock_db, skip=0, limit=100)

    mock_crud.get_multi.assert_called_once_with(mock_db, skip=0, limit=100)
    assert len(result) == 2
    assert result[0].name == "Brand1"
    assert result[1].name == "Brand2"

def test_remove_brand_success(mock_db, brand_schema, mock_crud):
    mock_crud.get.return_value = brand_schema
    mock_crud.remove.return_value = brand_schema

    result = model_service.remove_brand(mock_db, brand_schema.name)

    mock_crud.get.assert_called_once_with(mock_db, id_=brand_schema.name)
    mock_crud.remove.assert_called_once_with(db=mock_db, id_=brand_schema.name)
    assert result == brand_schema

def test_remove_brand_not_found(mock_db, brand_schema, mock_crud):
    mock_crud.get.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        model_service.remove_brand(mock_db, brand_schema.name)

    mock_crud.get.assert_called_once_with(mock_db, id_=brand_schema.name)
    assert exc_info.value.status_code == 404
    assert "not found" in exc_info.value.detail