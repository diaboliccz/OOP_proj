from Hotel import *

class HotelCatalog():
    def __init__(self):
        self.__hotel_list = []

    def search_hotel(self, search_text, check_in_date, check_out_date, sleeps, wanted_room):
        res = []
        for hotel in self.__hotel_list:
            if search_text in hotel.hotel_name:
                roomtype_list = []
                for roomtype in hotel.roomtype_list:
                    if roomtype.sleeps >= sleeps/wanted_room:
                        count = 0
                        for room in roomtype.room_list: 
                            if room.is_available(check_in_date, check_out_date):
                                count += 1
                        if count >= wanted_room:
                            roomtype_list.append(roomtype)

                if len(roomtype_list) > 0:
                    res.append([hotel, roomtype_list])
        return res
    
    def add_hotel(self, hotel_info):
        hotel = Hotel(hotel_info["hotel_name"], hotel_info["hotel_type"], hotel_info["address"], hotel_info["map"], hotel_info["policies"], hotel_info["property_facilities"], hotel_info["payment_option"])
        self.__hotel_list.append(hotel)
        return True
    
    @property
    def hotel_list(self):
        return self.__hotel_list