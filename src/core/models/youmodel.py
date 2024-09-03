from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class YouModel(Base):

    title: Mapped[str] = mapped_column(String(length=255))