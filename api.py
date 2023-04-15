from typing import Optional
from fastapi import FastAPI
from ins import *

app = FastAPI()

@app.get("/")
def hi():
    return {"hello" : "world"}

# {
#     "user_name": "boomoioi",
#     "hotel_name": "Hottestel",
#     "roomtype": "Delux",
#     "check_in_date": 1,
#     "checl_out_date" : 2
# }


class User(BaseModel):
    username: str
    password: str
    level: Optional[str] = "normal"

class Data(BaseModel):
    user_name: str
    hotel_name: str
    roomtype: str
    check_in_date: int
    check_out_date: int

@app.post("/add_to_cart/")
def read_item(data: Data) -> dict:
    # user_name = data["user_name"]
    # hotel_name = data["hotel_name"]
    # roomtype_name = data["roomtype"]
    # check_in_date =  data["check_in_date"]
    # check_out_date = data["check_out_date"]
    if hotel.hotel_name == hotel_name:
        for i in range(len(hotel.roomtype_list)):
            if hotel.roomtype_list[i].roomtype == roomtype_name:
                if user.add_to_cart(hotel.roomtype_list[i], check_in_date, check_out_date):
                    return {"status": "Success"}

    return {"status": "Fail"}

@app.post("/view_cart/")
def view_cart():
    return{"Room": [[x.hotel.hotel_name, x.roomtype.roomtype ,x.check_in_date, x.check_out_date, x.price] for x in user.cart.room_list]}


@app.post("/login")
def login(user: User):
    return {"echo": user}
# @app.post("/login")
# def login(user: User):
#     return {"echo": user}