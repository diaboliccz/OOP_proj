from Room import Room
class RoomReserved(Room):
    def __init__(self, room, check_in_date, check_out_date , status="pending"):
        super().__init__(room._hotel, room._roomtype, room._id)
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status
        self.__price = (check_out_date - check_in_date) * self._roomtype.price

    @property
    def check_in_date(self):
        return self.__check_in_date
    
    @property
    def check_out_date(self):
        return self.__check_out_date
    
    @property
    def status(self):
        return self.__status
    
    @property
    def price(self):
        return self.__price
    
    @status.setter
    def status(self, value):
        self.__status = value
        return self.__status


    def full_option(self):
        return [self._hotel.hotel_name, self.__check_in_date, self.__check_out_date]