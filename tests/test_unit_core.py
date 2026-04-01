import pytest
from mypackage.core import add


@pytest.fixture
def test_add():
    assert add(2, 3) == 5
