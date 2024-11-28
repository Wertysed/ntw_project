from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    count = Column(Integer)
    order_id = Column(Integer, ForeignKey("orders.id"))
    status_order_item_id = Column(Integer, ForeignKey("status_order_item.id"))

    status_order_item = relationship("StatusOrderItem", back_populates="order_item")
    order_asso = relationship("Order", back_populates="order_item")
    item_asso = relationship("Item", back_populates="order_item")

     
    



