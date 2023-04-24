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
#     "check_out_date" : 2
# }

# {
#     "search_text": "Hot",
#     "check_in_date": 1,
#     "check_out_date" : 2,
#     "sleeps": 2,
#     "room" : 1
# }



@app.post("/add_to_cart/")
def add_to_cart(data: dict) -> dict:
    hotel_name = data["hotel_name"]
    roomtype_name = data["roomtype"]
    check_in_date = data["check_in_date"]
    check_out_date = data["check_out_date"]
    if user.add_to_cart(hotel_name, roomtype_name, check_in_date, check_out_date):
        return {"status": "Success"}
    else:
        return {"status": "Fail"}

@app.get("/view_cart/")
def view_cart():
    return user.cart.show_item()

@app.post("/search/")
def search_hotel(data: dict): 
    search_text = data["search_text"]
    check_in_date = data["check_in_date"]
    check_out_date = data["check_out_date"]
    sleeps = data["sleeps"]
    wanted_room = data["room"]
    return catalog.search_hotel(search_text, check_in_date, check_out_date, sleeps, wanted_room)
    