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

@app.get("/show_hotel_data/")
def show_hotel_data():
    return catalog.show_hotel_data(catalog.hotel_list)

@app.post("/add_hotel/")
def add_hotel(hotel_info: dict):
    return catalog.add_hotel(hotel_info)

@app.post("/add_roomtype")
def add_roomtype(data: dict):
    index_hotel = data["index_hotel"]
    data.pop("index")
    return catalog.hotel_list[index_hotel].add_roomtype(data)

@app.post("/add_room/")
def add_room(data: dict):
    index_hotel = data["index_hotel"]
    index_roomtype = data["index_roomtype"]
    count = data["count"]
    return catalog.hotel_list[index_hotel].add_room(index_roomtype, count)