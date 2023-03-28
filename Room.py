class Room:
    def __init__ (self, hotel, roomtype):
        self._id = 1
        self._hotel = hotel
        self._roomtype = roomtype

    @property
    def id(self):
        return self._id