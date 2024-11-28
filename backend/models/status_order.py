from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class StatusOrder(Base):
    __tablename__ = "status_order"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    order = relationship("Order", back_populates="status_order")
