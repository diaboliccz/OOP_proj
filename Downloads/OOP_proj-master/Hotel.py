from RoomType import *

class Hotel:
    def __init__(self, hotel_name, hotel_type, address, map, policies, property_list, payment_list):
        self.__roomtype_list = []
        self.__hotel_name = hotel_name
        self.__hotel_type = hotel_type
        self.__address = address
        self.__map = map
        self.__total_rating = 0 
        self.__policies = policies
        self.__swimming_pool = False
        self.__internet = False
        self.__car_park = False
        self.__gym = False
        self.__non_smoking = False
        self.__spa = False
        self.__restaurant = False
        self.__pet = False
        self.__free_cancel = False
        self.__pay_at_hotel = False
        self.__pay_later = False
        self.__pay_now = False
        self.__credit_card = False
        self.__property_facilities = [self.__swimming_pool, self.__internet, self.__car_park, self.__gym, self.__non_smoking, self.__spa, self.__restaurant, self.__pet]
        self.__payment_option = [self.__free_cancel, self.__pay_at_hotel, self.__pay_later, self.__pay_now, self.__credit_card]
        self.__edit_payment_option(payment_list)
        self.__edit_property_facilities(property_list)


    def __edit_property_facilities(self, property_list):
        for i in range(len(property_list)):
            self.__property_facilities[i] = property_list[i]

    
    def __edit_payment_option(self, payment_list):
        for i in range(len(payment_list)):
            self.__payment_option[i] = payment_list[i]
    
    def add_room_type(self, room_type_info):
        self.__roomtype_list.append(RoomType(self, room_type_info["price"], room_type_info["sleeps"], room_type_info["room_size"], room_type_info["bed"], room_type_info["room_type"]))

    def add_room(self, index, count):
        self.__roomtype_list[index].add_room(count)

    @property
    def hotel_name(self):
        return self.__hotel_name
    
    @property
    def roomtype_list(self):
        return self.__roomtype_list

