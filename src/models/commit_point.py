import typing

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from src.models.base import DatedAtMixin

if typing.TYPE_CHECKING:
    from src.models.user import User


class CommitPoint(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "commit_point"
    __table_args__ = (UniqueConstraint("user_id", "year"),)

    id: int | None = Field(default=None, primary_key=True)
    commit_point: int
    year: int

    user_id: int = Field(default=None, foreign_key="user.id", ondelete="CASCADE", index=True)
    user: "User" = Relationship(back_populates="commit_points")
