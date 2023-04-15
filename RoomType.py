from Room import *

class RoomType:
    id = 0
    def __init__(self, hotel, price, sleeps, room_size, bed_type, room_type):
        self.__hotel = hotel
        self.__price = price
        self.__sleeps = sleeps
        self.__room_size = room_size
        self.__bed_type = bed_type
        self.__roomtype_name = room_type
        self.__room_list = []
        RoomType.id += 1

    def add_room(self, count):
        for i in range(count):
            self.__room_list.append(Room(self.__hotel, self))

    @property
    def room_list(self):
        return self.__room_list
    
    @property
    def price(self):
        return self.__price
    
    @property
    def sleeps(self):
        return self.__sleeps
    
    @property
    def roomtype_name(self):
        return self.__roomtype_name
