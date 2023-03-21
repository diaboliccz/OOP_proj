from Room import Room
class RoomReserved(Room):
    def __init__(self, Room, date):
        super.__init__(Room._id)
        self.date = date

        