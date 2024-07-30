from typing import List
from sqlalchemy import (ForeignKey, String)
from sqlalchemy.orm import (Mapped, mapped_column, relationship)

from sqlalchemy.ext.declarative import declarative_base

import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'user_table'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    hashed_password: Mapped[str] = mapped_column(String(255))

    todos: Mapped[List["Todo"]] = relationship(back_populates="user")

class Todo(Base):
    __tablename__ = 'todo_table'

    id: Mapped[str] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String(255))
    text: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[str] = mapped_column(ForeignKey("user_table.id"))

    user: Mapped["User"] = relationship(back_populates="todos")