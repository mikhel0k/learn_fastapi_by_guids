from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

from .base import Base

if TYPE_CHECKING:
    from .post import Post


class User(Base):
    username:  Mapped[str] = mapped_column(String(22), unique=True)

    posts: [list["Post"]] = relationship(back_populates="user")
