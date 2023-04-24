from Hotel import *
import math

class HotelCatalog():
    def __init__(self):
        self.__hotel_list = []

    def dict_to_list(self, hotel_list):
        res = []
        for key, val in hotel_list.items():
            temp = []
            for hotel in self.__hotel_list:
                if hotel.hotel_name == key:
                    temp.append(hotel)
                    roomtype_list = []
                    for roomtype in hotel.roomtype_list:
                        if roomtype.roomtype_name in val:
                            roomtype_list.append(roomtype)
                    temp.append(roomtype_list)
            res.append(temp)
        return res

    def list_to_dict(self, hotel_list):
        res = {}
        for hotel_room in hotel_list:
            
            hotel = hotel_room[0].hotel_name
            roomtype_list = [x.roomtype_name for x in hotel_room[1]]
            res.update({hotel : roomtype_list})
        return res

    def search_hotel(self, search_text, check_in_date, check_out_date, sleeps, wanted_room):
        res = {}
        for hotel in self.__hotel_list:
            if search_text.lower() in hotel.hotel_name.lower():
                roomtype_list = []
                for roomtype in hotel.roomtype_list:
                    if roomtype.sleeps >= sleeps/wanted_room:
                        count = 0
                        for room in roomtype.room_list: 
                            if room.is_available(check_in_date, check_out_date):
                                count += 1
                        if count >= wanted_room:
                            roomtype_list.append(roomtype.roomtype_name)
                if len(roomtype_list) > 0:
                    res.update({hotel.hotel_name: roomtype_list})
        return res
    
    def add_hotel(self, hotel_info):
        hotel = Hotel(hotel_info["hotel_name"], hotel_info["hotel_type"], hotel_info["address"], hotel_info["map"], hotel_info["policies"], hotel_info["property_facilities"], hotel_info["payment_option"])
        self.__hotel_list.append(hotel)
        return True
    
    def count_hotel_type(self, hotel_list):
        res = {}
        for hotel_room in hotel_list:
            hotel = hotel_room[0]
            if hotel.hotel_type not in res.keys():
                res.update({hotel.hotel_type : 1})
            else:
                res[hotel.hotel_type] += 1
        return res

    def count_payment(self, hotel_list):
        res = {"free_cancel" : 0,
               "pay_at_hotel" : 0,
               "pay_later" : 0,
               "pay_now" : 0,
               "credit_card" : 0
               }
        dict_key = list(res.keys())
        for hotel_room in hotel_list:
            hotel = hotel_room[0]
            for key in dict_key:
                if eval("hotel." + key):
                    res[key] += 1
        return res

    def count_bed(self, hotel_list):
        res = {}
        for hotel_room in hotel_list:
            roomtype_list = hotel_room[1]
            for roomtype in roomtype_list:
                if roomtype.bed_type not in res.keys():
                    res.update({roomtype.bed_type : 1})
                else:
                    res[roomtype.bed_type] += 1
        return res
    
    def count_rating(self, hotel_list):
        res = {}
        for hotel_room in hotel_list:
            hotel = hotel_room[0]
            key = str(math.floor(hotel.total_rating)) + "+"
            print(key)
            if key not in res.keys():
                res.update({key : 1})
            else: 
                print("check")
                res[key] += 1
        return res
    
    def count_hotel_fac(self, hotel_list):
        res = {"swimming_pool" : 0, 
               "internet" : 0, 
               "car_park" : 0, 
               "gym" : 0, 
               "non_smoking" : 0, 
               "spa" : 0, 
               "restaurant" : 0, 
               "pet" : 0
        }
        dict_key = list(res.keys())
        for hotel_room in hotel_list:
            hotel = hotel_room[0]
            for key in dict_key:
                if eval("hotel." + key):
                    res[key] += 1
        return res
    
    def price_filter(self, hotel_list, low, high):
        res = []
        for hotel_room in hotel_list:
            roomtype_list = hotel_room[1]
            for roomtype in roomtype_list:
                if roomtype.price > high or roomtype.price < low:
                    roomtype_list.remove(roomtype)
            if roomtype_list:
                res.append([hotel_room[0], roomtype_list])
        return self.list_to_dict(res)

    def hotel_type_filter(self, hotel_list, attr):
        res = []
        for hotel_room in hotel_list:
            hotel = hotel_room[0]
            if hotel.hotel_type == attr:
                res.append(hotel_room)
        return self.list_to_dict(res)
    
    def payment_fac_filter(self, hotel_list, attr):
        res = []
        search_text = "hotel." + attr
        for hotel_room in hotel_list:
            hotel = hotel_room[0]
            if eval(search_text):
                res.append(hotel_room)
        return self.list_to_dict(res)

    def rating_filter(self, hotel_list, rating):
        res = []
        for hotel_room in hotel_list:
            hotel = hotel_room[0]
            if hotel.total_rating >= rating and hotel.total_rating < rating+1:
                res.append(hotel_room)
        return self.list_to_dict(res)

    def bed_filter(self, hotel_list, bed):
        res = []
        for hotel_room in hotel_list:
            roomtype_list = hotel_room[1]
            temp = []
            for roomtype in roomtype_list: 
                if roomtype.bed_type == bed:
                    temp.append(roomtype)

            if temp:
                res.append([hotel_room[0], temp])
        
        return self.list_to_dict(res)
    
    @property
    def hotel_list(self):
        return self.__hotel_list
    

catalog = HotelCatalog()