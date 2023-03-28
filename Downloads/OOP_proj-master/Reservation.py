from RoomReserved import *
class Reservation():
    def __init__(self, room_list, date):
        self.__room_reserved_list = room_list
        self.__date_pay = date

    @property
    def room_reserved_list(self):
        return self.__room_reserved_list
    
    @property
    def date_pay(self):
        return self.__date_pay