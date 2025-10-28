from typing import TYPE_CHECKING

from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base
from .mixin import UserRelationshipMixin


if TYPE_CHECKING:
    from .user import User


class Post(UserRelationshipMixin, Base):
    _user_back_populates = "posts"
    title:  Mapped[str] = mapped_column(String(100))
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
