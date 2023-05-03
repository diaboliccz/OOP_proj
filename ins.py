from Cart import *
from Hotel import *
from RoomType import *
from Room import *
from RoomReserved import *
from Reservation import *
from User import *
from HotelCatalog import *
from Agoda import Agoda
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import datetime


hotel_info = {
    "hotel_name": "Hottestel",
    "hotel_type" : "Apartment",
    "address": "55/28 Thonglor Sukhmvit",
    "map": "13.740257,460.548432",
    "policies": "NO good",
    "property_facilities": [0,0,0,0,1,1,1,1],
    "payment_option" : [0,1,1,1,0]
}
hotel_info_2 = {
    "hotel_name": "coldbutHot",
    "hotel_type" : "Apartment",
    "address": "55/28 Thonglor Sukhmvit",
    "map": "13.740257,460.548432",
    "policies": "NO good",
    "property_facilities": [0,0,0,0,1,1,1,1],
    "payment_option" : [0,1,1,1,0]
}
hotel_info_3 = {
    "hotel_name": "Hot1testel",
    "hotel_type" : "Home",
    "address": "55/28 Thonglor Sukhmvit",
    "map": "13.740257,460.548432",
    "policies": "NO good",
    "property_facilities": [0,0,0,0,1,1,1,1],
    "payment_option" : [1,1,1,1,0]
}

room_type_info ={
    "price" : 1593.50,
    "sleeps" : 2,
    "room_size" : "300 square feet",
    "bed" : "KingSize",
    "room_type" : "Deluxe"
}
room_type_info_2 ={
    "price" : 200.50,
    "sleeps" : 2,
    "room_size" : "300 square feet",
    "bed" : "3.5 feet",
    "room_type" : "Standard"
}
room_type_info_3 ={
    "price" : 20000.50,
    "sleeps" : 2,
    "room_size" : "300 square feet",
    "bed" : "KingSize",
    "room_type" : "Premium"
}




#Hotel initialize
catalog.add_hotel(hotel_info)
catalog.add_hotel(hotel_info_2)
catalog.add_hotel(hotel_info_3)
catalog.hotel_list[0].add_room_type(room_type_info)
catalog.hotel_list[0].add_room_type(room_type_info_2)
catalog.hotel_list[0].add_room_type(room_type_info_3)
catalog.hotel_list[0].add_room(0, 2)
catalog.hotel_list[0].add_room(1, 5)
catalog.hotel_list[0].add_room(2, 7)
catalog.hotel_list[1].add_room_type(room_type_info)
catalog.hotel_list[1].add_room(0, 2)
catalog.hotel_list[2].add_room_type(room_type_info)
catalog.hotel_list[2].add_room(0, 2) 

search_res = catalog.search_hotel('Hot', datetime.datetime(2023, 4, 12), datetime.datetime(2023, 4, 15), 2, 1)
print(search_res)
res = catalog.dict_to_list(search_res)

print(catalog.count_bed(res))
print(catalog.bed_filter(res, "3.5 feet"))

#User initialize
user = User(username = 'boomoioi', password = "maibok", email = "1@kmitl.ac.th", phone_number = "0626250119", full_name = "Nanthakorn Nanthawisit")
user.add_to_cart('Hottestel', "Deluxe", datetime.datetime(2023, 4, 12), datetime.datetime(2023, 4, 15))
user.add_to_cart('Hottestel', "Deluxe", datetime.datetime(2023, 4, 12), datetime.datetime(2023, 4, 15))
# user.add_to_cart('Hottestel', "Deluxe", datetime.datetime(2023, 4, 1), datetime.datetime(2023, 4, 5))
# user.add_to_cart('Hottestel', "Deluxe", datetime.datetime(2023, 4, 12), datetime.datetime(2023, 4, 15))

# print(user.cart.show_item())
# print(agoda.get_status())
# user.check_out()
# print(agoda.get_status())
# print(user.cart.show_item())