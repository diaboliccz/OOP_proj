class Cart():
    def __init__(self, payment):
        self.__room_list = []
        self.__check_in_date_list = []
        self.__check_out_date_list = []
        self.__total_price = 0
        self.__status = False
        self.__payment = payment
        
    def add_room(self, room, check_in_date, check_out_date):
        pass

    def checkout(self):
        pass
    
    def reserve_room(self):
        pass
