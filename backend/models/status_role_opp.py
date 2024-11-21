from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class StatusRoleOpp(Base):
    __tablename__ = "status_role_opp"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    role_opp = relationship("RoleOpp", back_populates="status_role_opp")


