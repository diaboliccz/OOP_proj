from User import *
from Cart import *
from Hotel import *
from RoomType import *
from Room import *
from RoomReserved import *

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

hotel = Hotel(hotel_info["hotel_name"], hotel_info["hotel_type"], hotel_info["address"], hotel_info["map"], hotel_info["policies"], hotel_info["property_facilities"], hotel_info["payment_option"])
hotel.add_room_type(room_type_info)
hotel.add_room(0, 3)
user = User(username = 'boomoioi', password = "maibok", email = "1@kmitl.ac.th", phone_number = "0626250119", full_name = "Nanthakorn Nanthawisit")

user.add_to_cart(hotel.roomtype_list[0], 12, 15)
user.add_to_cart(hotel.roomtype_list[0], 12, 18)
user.add_to_cart(hotel.roomtype_list[0], 10, 11)

for room in user.cart.room_list:
    print(room.full_option())

print(user.cart.total_price)
user.check_out()
print(user.cart.room_list)
print(user.reservations[0].room_reserved_list)