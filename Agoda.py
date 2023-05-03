class Agoda():
    def __init__(self):
        self.__reservation_list = []

    def add_room(self, room):
        self.__reservation_list.append(room)

    @property 
    def reservation_list(self):
        return self.__reservation_list
    
    def get_status(self):
        temp = [] 
        for room in self.__reservation_list:
            temp.append(room.status)

        return temp

    
agoda = Agoda()
