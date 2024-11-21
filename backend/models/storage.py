from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db import Base


class Storage(Base):
    __tablename__ = "storage"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    item = relationship("Item", back_populates="storage")
    shelf = relationship("Shelf", back_populates="storage")
    role = relationship("Role", back_populates="storage")
    
