from unittest.mock import AsyncMock

import pytest


@pytest.fixture()
def mock_session():
    session = AsyncMock()
    return session
