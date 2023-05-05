from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import datetime
from ins import *

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "localhose:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
#     "check_in_date": "12-4-2023",
#     "check_out_date" : "15-4-2023",
#     "sleeps": 2,
#     "room" : 1
# }



@app.post("/add_to_cart/")
def add_to_cart(data: dict) -> dict:
    hotel_name = data["hotel_name"]
    roomtype_name = data["roomtype"]
    check_in_date = data["check_in_date"]
    check_out_date = data["check_out_date"]
    wanted_room = data["wanted_room"]
    username = data["username"]
    user = account_list.find_user(username)
    if user.add_to_cart(hotel_name, roomtype_name, check_in_date, check_out_date, wanted_room):
        return {"status": "Success"}
    else:
        return {"status": "Fail"}
    
@app.post("/check_out/")
def check_out(data: dict) -> dict:
    username = data["username"]
    user = account_list.find_user(username)
    if user.check_out():
        return {"status" : "Success"}
    else:
        return {"status" : "Fail"}


@app.post("/view_cart/")
def view_cart(data: dict) -> dict:
    username = data["username"]
    user = account_list.find_user(username)
    return user.cart.show_item()

@app.post("/search/")
def search_hotel(data: dict): 
    search_text = data["search_text"]
    check_in_date = data["check_in_date"]
    check_out_date = data["check_out_date"]
    sleeps = data["sleeps"]
    wanted_room = data["wanted_room"]
    return catalog.search_hotel(search_text, check_in_date, check_out_date, sleeps, wanted_room)

@app.post("/price_filter/")
def price_filter(data: dict): 
    hotel_list = data["hotel_list"]
    min = data["min"]
    max = data["max"]
    hotel_list = catalog.dict_to_list(hotel_list)
    return catalog.price_filter(hotel_list, min, max)

@app.post("/hotel_type_filter/")
def hotel_type_filter(data: dict): 
    hotel_list = data["hotel_list"]
    attr = data["attr"]
    hotel_list = catalog.dict_to_list(hotel_list)
    return catalog.hotel_type_filter(hotel_list, attr)

@app.post("/bed_filter/")
def bed_filter(data: dict): 
    hotel_list = data["hotel_list"]
    attr = data["attr"]
    hotel_list = catalog.dict_to_list(hotel_list)
    return catalog.bed_filter(hotel_list, attr)

@app.post("/payment_fac_filter/")
def payment_fac_filter(data: dict): 
    hotel_list = data["hotel_list"]
    attr = data["attr"]
    hotel_list = catalog.dict_to_list(hotel_list)
    return catalog.payment_fac_filter(hotel_list, attr)

@app.post("/rating_filter/")
def rating_filter(data: dict): 
    hotel_list = data["hotel_list"]
    attr = data["attr"]
    hotel_list = catalog.dict_to_list(hotel_list)
    return catalog.rating_filter(hotel_list, attr)

@app.post("/create_comment/")
def create_comment(data: dict):
    hotel_name = data["hotel_name"]
    comment = data["comment"]
    rating = data["rating"]
    username = data["username"]
    user = account_list.find_user(username)
    if(user.comment_rating(hotel_name, comment, rating)):
        return {"status" : True}
    else:
        return {"status" : False}
    

@app.post("/roomtype_info/")
def roomtype_info(data: dict) -> dict:
    hotel_name = data["hotel_name"]
    roomtype_list = data["roomtype_list"]
    print(hotel_name, roomtype_list)
    return {"result" : catalog.get_roomtype_info(hotel_name, roomtype_list)}

@app.post("/get_history_list/")
def get_history_list(data: dict) -> dict:
    username = data["username"]
    user = account_list.find_user(username)
    return user.get_history_list()

@app.post("/get_history_detail/")
def get_history_detail(data: dict) -> dict:
    id = data["id"]
    return account_list.get_history(id)

@app.post("/refund/")
def refund(data: dict) -> dict:
    id = data["id"]
    return account_list.refund(id)
