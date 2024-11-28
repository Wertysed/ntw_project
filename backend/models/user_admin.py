from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base



class UserAdmin(Base):
    __tablename__ = 'user_admin'

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)
    hash_password = Column(String)

    storage  = relationship("Storage", secondary="user_admin_storage", back_populates="user_admin")




