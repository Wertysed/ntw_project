from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class StatusOrderItem(Base):
    __tablename__ = "status_order_item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    order_item = relationship("OrderItem", back_populates="status_order_item")

