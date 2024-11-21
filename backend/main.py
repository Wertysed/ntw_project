from fastapi import FastAPI, Body, Depends
from db import Base, engine, get_db
from models.storage import Storage
from models.item import Item
from models.shelf import Shelf
from models.box import Box
from models.role import Role
from models.opp import Opp
from models.role_opp import RoleOpp
from models.status_role_opp import StatusRoleOpp
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()



@app.get("/hello")
def hello(id: int, name: str, db: Session = Depends(get_db)):
    #    new_opp = Opp(name=name)
    #    new_role = Role(name=(name+" role"), storage_id=1)
    #    new_status = StatusRoleOpp(name=(name+" status"))
    #
    #    db.add(new_opp)
    #    db.add(new_role)
    #    db.add(new_status)
    #
    #    db.commit()
    #
    #    db.refresh(new_opp)
    #    db.refresh(new_role)
    #    db.refresh(new_status)
    #
    #    new_role_opp = RoleOpp(role_id=1, opp_id=1, status_role_opp_id=1)
    #    db.add(new_role_opp)
    #    db.commit()
    #    db.refresh(new_role_opp)
    #
    role_opp = db.query(Role).all()
    
    for role in role_opp:
        for opp in role.opp:
            role_dd = db.query(RoleOpp).filter_by(role_id=role.id, opp_id=opp.id).first()
            print(role.name, opp.name, role_dd.status_role_opp.name)

    return {"msg": "success"}
