from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    article = Column(Integer, unique=True)
    description = Column(String)
    total_count = Column(Integer)
    storage_id = Column(Integer, ForeignKey("storage.id"))

    storage = relationship("Storage", back_populates="item")
    box = relationship("Box", back_populates="item")


