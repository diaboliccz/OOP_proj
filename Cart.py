from RoomReserved import RoomReserved
class Cart():
    def __init__(self, user):
        self.__user = user
        self.__room_list = []
        self.__total_price = 0
        self.__payment_status = False
    
    def add(self, room):
        self.__room_list.append(room)

    @property
    def room_list(self):
        return self.__room_list

