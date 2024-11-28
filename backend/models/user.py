from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    hash_password = Column(String)
    role_id = Column(Integer, ForeignKey("role.id"))
    storage_id = Column(Integer, ForeignKey("storage.id"))


    order = relationship("Order",secondary="order_users", back_populates="user")
    role = relationship("Role", back_populates="user")
    storage = relationship("Storage", back_populates="user")



    
