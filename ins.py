from Cart import *
from HotelCatalog import *
from Hotel import *
from RoomType import *
from Room import *
from RoomReserved import *
from Reservation import *
from User import *
from Agoda import agoda
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

hotel_info = {
    "hotel_name": "Hottestel",
    "hotel_type" : "Apartment",
    "address": "55/28 Thonglor Sukhmvit",
    "map": "13.740257,460.548432",
    "policies": "NO good",
    "property_facilities": [0,0,0,0,1,1,1,1],
    "payment_option" : [0,1,1,1,0]
}

room_type_info ={
    "price" : 1593.50,
    "sleeps" : 2,
    "room_size" : "300 square feet",
    "bed" : "KingSize",
    "room_type" : "Delux"
}

#Hotel initialize
catalog = HotelCatalog()
catalog.add_hotel(hotel_info)
catalog.hotel_list[0].add_room_type(room_type_info)
catalog.hotel_list[0].add_room(0, 2)

print(catalog.search_hotel('Hot', 12, 15, 1, 1))

#User initialize
user = User(username = 'boomoioi', password = "maibok", email = "1@kmitl.ac.th", phone_number = "0626250119", full_name = "Nanthakorn Nanthawisit")
user.add_to_cart(catalog.hotel_list[0].roomtype_list[0], 12, 15)
user.add_to_cart(catalog.hotel_list[0].roomtype_list[0], 12, 18)
user.add_to_cart(catalog.hotel_list[0].roomtype_list[0], 10, 11)
user.add_to_cart(catalog.hotel_list[0].roomtype_list[0], 10, 11)

# print(user.cart.show_item())
# print(agoda.get_status())
# user.check_out()
# print(agoda.get_status())

# print([[x.hotel.hotel_name, x.roomtype.roomtype ,x.check_in_date, x.check_out_date, x.price] for x in user.cart.room_list])