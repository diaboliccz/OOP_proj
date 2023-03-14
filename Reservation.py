from RoomReserved import *
class Reservation():
    def __init__(self, room, check_in_date, check_out_date, refundble, price):
        self.__room_list = []
        self.__check_in_date_list = []
        self.__check_out_date_list = []
        self.__refundable_list = []
        self.__price_list = []
        self.__room_reseved_list = []
        self.__status = False
        self.update_list(room, check_in_date, check_out_date, refundble, price)

    def update_list(self, room, check_in_date, check_out_date, refundble, price):
        self.__room_list.append(room)
        self.__check_in_date_list.append(check_in_date)
        self.__check_out_date_list.append(check_out_date)
        self.__refundable_list.append(refundble)
        self.__price_list.append(price)

    def create_reserve_room(self):
        self.__status = True
        for i in len(self.__room_reseved_list):
            self.__room_reseved_list.append(RoomReserved(self.__room_list[i], self.__check_in_date_list[i], self.__check_out_date_list[i]))
        

    def update_room_status(self):
        pass