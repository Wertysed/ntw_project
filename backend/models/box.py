from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Box(Base):
    __tablename__ = "box"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    item_id = Column(Integer, ForeignKey("item.id"))
    count = Column(Integer)
    qr_code = Column(String)
    level = Column(Integer)
    shelf_id = Column(Integer, ForeignKey("shelf.id"))

    item = relationship("Item", back_populates="box")
    shelf = relationship("Shelf", back_populates="box")
