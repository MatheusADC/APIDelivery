import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    body = {
        "data": {
            "name": "joazinho",
            "address": "rua do limao",
            "cupom": False,
            "items": [
                { "item": "Refrigerante", "quantidade": 2 },
                { "item": "pizza", "quantidade": 3 }
            ]
        }
    }
    registry_order_validator(body)

def test_registry_order_validator_with_errors():
    body_with_error = {
        "data": {
            "name": "joazinho",
            "address": "rua do limao",
            "cupom": "error",
            "items": [
                { "item": "Refrigerante", "quantidade": 2 },
                { "item": "pizza", "quantidade": 3 }
            ]
        }
    }
    with pytest.raises(Exception):
        registry_order_validator(body_with_error)

# pytest -s -v src/validators/registry_order_validator_test.py