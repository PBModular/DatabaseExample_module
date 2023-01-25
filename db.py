from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.types import String


class Base(DeclarativeBase):
    pass


class Test(Base):
    __tablename__ = "testing"

    id: Mapped[int] = mapped_column(primary_key=True)
    info: Mapped[str] = mapped_column(String(30))

    def __repr__(self):
        return f"Test(id={self.id}, info={self.info})"
