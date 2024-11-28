from fastapi import FastAPI, Body, Depends
from db import Base, engine, get_db
from models.storage import Storage
from models.item import Item
from models.shelf import Shelf
from models.box import Box
from models.role import Role
from models.opp import Opp
from models.user_admin import UserAdmin
from models.user_admin_storage import UserAdminStorage
from models.role_opp import RoleOpp
from models.order import Order
from models.status_order import StatusOrder
from models.status_role_opp import StatusRoleOpp
from models.order_item import OrderItem
from models.user import User
from models.order_user import OrderUser
from models.status_order_item import StatusOrderItem

from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()



@app.get("/hello")
def hello(id: int, name: str, db: Session = Depends(get_db)):

     
    

    
        
    

    

       

    
    
    return {"msg": "success"}
