from src.dependencies.users import get_username


async def test_get_username__inputs_upper_lower_mixed_username__returns_lowercase_username():
    # given
    username = "User NaMe"

    # when
    gotten = await get_username(username)

    # then
    assert gotten == "user name"
