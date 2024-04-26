from pydantic import BaseModel


class UserContributionsByYear(BaseModel):
    user: "User"

    class User(BaseModel):
        contributionsCollection: "ContributionsCollection"

        class ContributionsCollection(BaseModel):
            totalCommitContributions: int


class UserContributionYears(BaseModel):
    user: "User"

    class User(BaseModel):
        contributionsCollection: "ContributionsCollection"

        class ContributionsCollection(BaseModel):
            contributionYears: list[int]
