from main import get_temperature
from unittest.mock import patch
import pytest

values = [
    (62, -14.235004, -14.235004, 16),
    (32, 56.1304, 106.3468, 0),
    (95, 7.1195, 34.8450, 35),
    (-4, 41.8781, 87.6298, -20)
]


@pytest.mark.parametrize("temperature, lat, lng, expected", values)
def test_get_temperature_by_lat_lng(temperature, lat, lng, expected):
    temperature = {
        "currently": {
            "temperature": temperature
        }
    }

    mock_get_patcher = patch('main.requests.get')
    mock_get = mock_get_patcher.start()
    mock_get.return_value.json.return_value = temperature   
    response = get_temperature(lat, lng)
    mock_get_patcher.stop()
    assert response == expected
