from sqlalchemy import UniqueConstraint
from sqlmodel import Field, SQLModel

from src.models.base import DatedAtMixin


class CommitPoint(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "commit_point"
    __table_args__ = (UniqueConstraint("user_id", "year"),)

    id: int | None = Field(default=None, primary_key=True)
    commit_point: int
    year: int
    user_id: int = Field(default=None, foreign_key="user.id")
