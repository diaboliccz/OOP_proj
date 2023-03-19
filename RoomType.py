room_type_info ={
    "price" : 1593.50,
    "sleeps" : 2,
    "room_size" : "300 square feet",
    "bed" : "KingSize",
    "room_type" : "Delux"
}


class RoomType:
    def __init__(self, price, sleeps, room_size, bed, room_type):
        self.__price = price
        self.__sleeps = sleeps
        self.__room_size = room_size
        self.__bed = bed
        self.__room_type = room_type