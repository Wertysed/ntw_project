from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class UserAdminStorage(Base):
    __tablename__ = "user_admin_storage"

    id = Column(Integer, primary_key=True, index=True) 
    storage_id = Column(Integer, ForeignKey("storage.id"))
    user_admin_id = Column(Integer, ForeignKey("user_admin.id"))


