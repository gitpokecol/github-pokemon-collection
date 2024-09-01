from datetime import date

from sqlalchemy import Integer, UniqueConstraint
from sqlmodel import Field, SQLModel

from src.models.base import DatedAtMixin
from src.pokemons.item_type import ItemType
from src.utils import utc_now_date


class DailyItem(SQLModel, DatedAtMixin, table=True):
    __tablename__: str = "daily_item"
    __table_args__ = (UniqueConstraint("created_date"),)

    id: int | None = Field(default=None, primary_key=True)
    created_date: date = Field(default_factory=utc_now_date)
    type: ItemType = Field(sa_type=Integer)
