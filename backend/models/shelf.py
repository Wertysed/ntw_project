from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Shelf(Base):
    __tablename__ = "shelf"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    storage_id = Column(Integer, ForeignKey("storage.id"))

    storage = relationship("Storage", back_populates="shelf")
    box = relationship("Box", back_populates="shelf")


