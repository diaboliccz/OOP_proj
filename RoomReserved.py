from Room import Room
class RoomReserved(Room):
    def __init__(self, room, start_date, end_date):
        super.__init__(room)
        self.__startdate = start_date
        self.__end_date = end_date

        