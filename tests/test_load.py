# tests/test_loader.py
import pytest
from unittest.mock import patch, MagicMock
from etl.load import AnimalLoader


@pytest.fixture
def loader():
    return AnimalLoader()


@patch('etl.load.RequestClient.post')
def test_upload_batches_success(mock_post, loader):
    mock_post.return_value = MagicMock(status_code=200)
    animals = [{'id': i} for i in range(5)]
    loader.load_batches(animals)
    assert mock_post.call_count == 1


@patch('etl.load.RequestClient.post')
def test_upload_batches_multiple_batches(mock_post, loader):
    mock_post.return_value = MagicMock(status_code=200)
    animals = [{'id': i} for i in range(150)]
    loader.load_batches(animals)
    assert mock_post.call_count == 2
