import pytest
from mypackage.core import add


@pytest.mark.integration
def test_integration_flow():
    result = add(a=10, b=5)
    assert result == 15
