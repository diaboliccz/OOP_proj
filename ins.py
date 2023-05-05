from User import *
from HotelCatalog import catalog


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
hotel_info_4 = {
    "hotel_name": "Jay Starh",
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
catalog.add_hotel(hotel_info_4)
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
catalog.hotel_list[3].add_room_type(room_type_info)
catalog.hotel_list[3].add_room(0, 12) 
catalog.hotel_list[0].add_room(2, 7)

account_list.register(username = 'boomoioi', password = "maibok", email = "1@kmitl.ac.th", phone_number = "0626250119", full_name = "Nanthakorn Nanthawisit")
account_list.register(username = 'jay', password = "maibok", email = "2@kmitl.ac.th", phone_number = "0626250119", full_name = "Nanthakorn Nanthawisit")
user = account_list.find_user("jay")
user.add_to_cart("Hottestel", "Deluxe", "2023-12-10", "2023-12-13", 2)
user.check_out()
user.comment_rating("Hottestel", "test", 9)
user.comment_rating("Hottestel", "test", 1)
user.comment_rating("Hottestel", "test", 3)
user.comment_rating("Hottestel", "test", 7)
print(user.get_history_list())
# print(catalog.hotel_list[0].comment_list)