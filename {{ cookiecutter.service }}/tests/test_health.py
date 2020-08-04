import pytest

from {{ cookiecutter.python_package }} import methods
import tests


@pytest.mark.asyncio
async def test_health():
    method = methods.Health()
    client = tests.client()
    resp, status = await client.request(method)
    assert status == 204
