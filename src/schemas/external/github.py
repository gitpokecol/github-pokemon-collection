from pydantic import BaseModel


class UserContributionsByYear(BaseModel):
    user: "User | None"

    class User(BaseModel):
        contributionsCollection: "ContributionsCollection"

        class ContributionsCollection(BaseModel):
            totalCommitContributions: int


class UserContributionYears(BaseModel):
    user: "User | None"

    class User(BaseModel):
        contributionsCollection: "ContributionsCollection"

        class ContributionsCollection(BaseModel):
            contributionYears: list[int]
