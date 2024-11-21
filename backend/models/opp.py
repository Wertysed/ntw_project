from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class Opp(Base):
    __tablename__ = "opp"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    role = relationship("Role", secondary="role_opp", back_populates="opp")
