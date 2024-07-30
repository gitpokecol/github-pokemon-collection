from unittest.mock import Mock

import pytest

from tests.utils.common import mock_coroutine


@pytest.fixture()
def mock_session():
    session = Mock()
    session.commit = mock_coroutine
    session.close = mock_coroutine
    return session
