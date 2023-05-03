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
    
    def booked_list(self):
        temp = [self.__date_pay]
        sum = 0 
        for room in self.__room_reserved_list:
            sum += room.price
            temp.append([room.hotel.hotel_name, room.check_in_date, room.check_out_date])
        temp.append(sum)
        return temp