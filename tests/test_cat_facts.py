import pytest
from jsonschema import validate
from clients.cat_facts_client import CatFactsClient
from schemas.fact_schema import fact_schema

@pytest.fixture(scope="module")
def client():
    return CatFactsClient()

def test_get_random_fact(client):
    response = client.get_random_fact()
    assert response.status_code == 200
    data = response.json()
    
    # Validate the response against the schema
    validate(instance=data, schema=fact_schema)
    
    assert "fact" in data
    assert len(data["fact"]) > 0

def test_get_facts(client):
    response = client.get_facts()
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)

@pytest.mark.parametrize("limit", [0, 1, 20])
def test_get_facts_with_limit(client, limit):
    response = client.get_facts(limit=limit)
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
    assert len(data["data"]) == limit

def test_get_breeds(client):
    response = client.get_breeds()
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert isinstance(data["data"], list)
