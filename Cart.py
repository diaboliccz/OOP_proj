from RoomReserved import RoomReserved
class Cart():
    def __init__(self, user):
        self.__user = user
        self.__room_list = []
        self.__total_price = 0
        self.__payment_status = False
    
    def add(self, room):
        self.__room_list.append(room)
        self.__update()

    def clear_cart(self):
        self.__room_list = []
        self.__update()

    def __update(self):
        self.__total_price = 0
        for room in self.__room_list:
            room_price = room.price 
            self.__total_price += room_price

        return True
    
    @property
    def total_price(self):
        return self.__total_price

    @property
    def room_list(self):
        return self.__room_list

    def show_item(self):
        res = []
        for reserved in self.__room_list:
            res.append([reserved.hotel.hotel_name, reserved.roomtype.roomtype_name, reserved.check_in_date, reserved.check_out_date])
        return res
