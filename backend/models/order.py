from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    status_order_id = Column(Integer, ForeignKey("status_order.id"))

    item = relationship("Item",secondary="order_item", back_populates="order")
    status_order = relationship("StatusOrder", back_populates="order")
    order_item = relationship("OrderItem", back_populates="order_asso")
    user = relationship("User", secondary="order_users", back_populates="order")
