from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db import Base

class RoleOpp(Base):
    __tablename__ = "role_opp"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer, ForeignKey("role.id"))
    opp_id = Column(Integer, ForeignKey("opp.id"))
    status_role_opp_id = Column(Integer, ForeignKey("status_role_opp.id"))

    status_role_opp = relationship("StatusRoleOpp", back_populates="role_opp") 


