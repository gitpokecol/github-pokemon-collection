from tests.integration import value


class GithubAPIFake:
    async def get_user_total_contributions(self, *, username: str) -> dict[int, int]:
        return value.user_total_contributions

    async def get_user_contributions_by_year(self, *, username: str, year: int) -> int:
        return value.user_total_contributions[year]
