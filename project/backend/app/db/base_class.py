 """
 Declarative base class for SQLAlchemy models.
 """

 from typing import Any

 from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column


 class Base(DeclarativeBase):
     """Base class implementing id/created_at columns by default."""

     id: Mapped[int] = mapped_column(primary_key=True, index=True)

     @declared_attr.directive
     def __tablename__(cls) -> str:  # type: ignore[override]
         return cls.__name__.lower()

     def __repr__(self) -> str:  # pragma: no cover - debugging helper
         attrs = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items() if not k.startswith("_"))
         return f"{self.__class__.__name__}({attrs})"
