import pytest
from unittest.mock import patch, MagicMock
from etl.extract import AnimalExtractor


@pytest.fixture
def extractor():
    return AnimalExtractor()


@patch('requests.get')
def test_fetch_all_animal_ids(mock_get, extractor):
    mock_get.side_effect = [
        MagicMock(status_code=200, json=lambda: {"items": [{'id': 1}, {'id': 2}]}),
        MagicMock(status_code=200, json=lambda: {"items": []})]
    ids = extractor.fetch_animals_ids()
    assert ids == [1, 2]


@patch('requests.get')
def test_fetch_animal_detail_success(mock_get, extractor):
    mock_get.return_value = MagicMock(status_code=200, json=lambda: {'id': 1, 'name': 'Dog'})
    animal = extractor.get_animal_detail(1)
    assert animal['name'] == 'Dog'


# This will take a time because it will retries multiple times.
@patch('requests.get')
def test_fetch_animal_detail_failure(mock_get, extractor):
    mock_get.return_value = MagicMock(status_code=500)
    animal = extractor.get_animal_detail(1)
    assert animal is None
