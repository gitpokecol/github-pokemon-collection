from sqlmodel import Field, Relationship, SQLModel

from models.pokemon import Pokemon


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=True)
    commit_point: int = Field(nullable=False)
    pokemons: list[Pokemon] = Relationship(sa_relationship_kwargs={"lazy": "join"})
