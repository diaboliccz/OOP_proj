class Room:
    id_cnt = 0
    def __init__ (self, hotel, roomtype, id=None):
        if(id == None):
            self._id = Room.id_cnt 
            Room.id_cnt += 1
        else:
            self._id = id
        self._hotel = hotel
        self._roomtype = roomtype

    @property
    def id(self):
        return self._id
    
    @property
    def roomtype(self):
        return self._roomtype
    
    @property
    def hotel(self):
        return self._hotel