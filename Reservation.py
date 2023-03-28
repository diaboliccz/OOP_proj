from RoomReserved import *
from RoomType import *
from Hotel import *
class Reservation(RoomReserved,RoomType,Hotel):
    def __init__(self, room_list, date):
        self.__room_reserved_list = room_list
        self.__date_pay = date
        self.__hotel_name = Hotel.hotel_name
       

    
    def booked_list(self):
        temp = [self.__date_pay]
        for room in self.__room_reserved_list:
            temp.append([room.hotel.hotel_name, room.check_in_date, room.check_out_date, room.price, room.status])

        return temp

    
    @property
    def room_reserved_list(self):
        return self.__room_reserved_list
    
    @property
    def date_pay(self):
        return self.__date_pay
    

    
    