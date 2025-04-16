import pytest
from datetime import datetime

from etl.transform import AnimalTransformer


@pytest.fixture
def transformer():
    return AnimalTransformer()


def test_transform_friends(transformer):
    data = {'id': 1, 'friends': 'Dog, Cat, Mouse', 'born_at': None}
    result = transformer.transform(data)
    assert result['friends'] == ['Dog', 'Cat', 'Mouse']


def test_transform_born_at_to_iso(transformer):
    born_at = 1172843933530
    data = {'id': 2, 'friends': '', 'born_at': born_at}
    dt = datetime.utcfromtimestamp(born_at // 1000)
    result = transformer.transform(data)
    assert result['born_at'] == f'{dt.isoformat()}Z'


def test_transform_born_at_none(transformer):
    data = {'id': 3, 'friends': '', 'born_at': None}
    result = transformer.transform(data)
    assert result['born_at'] is None
