from Agoda import agoda

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
    
    def is_available(self, check_in_date, check_out_date):
        temp = []
        for roomreserved in agoda.reservation_list:
            if roomreserved.id == self._id and roomreserved.status != "fail":
                temp.append(roomreserved)

        intersect = 0
        for roomreserved in temp:
            for date in range(roomreserved.check_in_date, roomreserved.check_out_date):
                if date < check_out_date and date >= check_in_date:
                    intersect+=1
                    break
                
        if(intersect == 0):
            return True
        else:
            return False