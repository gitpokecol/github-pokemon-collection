from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship, SQLModel

from src.models.base import DatedAtMixin
from src.models.daily_item import DailyItem
from src.models.user import User


class DailyItemAbtain(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "daily_item_abtain"
    __table_args__ = (UniqueConstraint("user_id", "daily_item_id"),)

    id: int | None = Field(default=None, primary_key=True)
    daily_item_id: int = Field(default=None, foreign_key="daily_item.id")
    daily_item: DailyItem = Relationship(sa_relationship_kwargs={"lazy": "joined"})

    user_id: int = Field(default=None, foreign_key="user.id")
    user: User = Relationship(sa_relationship_kwargs={"lazy": "joined"})
