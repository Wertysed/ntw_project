from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    storage_id = Column(Integer, ForeignKey("storage.id"))

    opp = relationship("Opp", secondary="role_opp", back_populates="role")
    storage = relationship("Storage", back_populates="role")


