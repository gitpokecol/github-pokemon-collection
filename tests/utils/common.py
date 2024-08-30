def mock_coroutine(return_value=None):
    async def coroutine(*args, **kwargs):
        return return_value

    return coroutine
