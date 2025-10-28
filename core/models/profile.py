from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

from .base import Base
from .mixin import UserRelationshipMixin

if TYPE_CHECKING:
    from .user import User


class Profile(UserRelationshipMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"
    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]
