from Cart import Cart
from RoomReserved import RoomReserved
from Reservation import Reservation
reservation_list = []

class Account():
    def __init__(self, username, password, email, phone_number):
        self._username = username
        self._password = password
        self._email = email
        self._phone_number = phone_number

class User(Account):
    def __init__(self, username, password, email, phone_number, full_name):  
        super().__init__(username, password, email, phone_number)
        self.__full_name = full_name
        self.__reservations = []
        self.__create_cart()
    
    def add_to_cart(self, roomtype, check_in_date, check_out_date):
        room = self.__get_room(roomtype, check_in_date, check_out_date)
        if(room):
            locked_room = RoomReserved(room, check_in_date, check_out_date)
            reservation_list.append(locked_room)
            self.cart.add(locked_room)
            return "Success"
        else:
            return "Sorry room full"

    def check_out(self):
        makepayment = 1
        if(makepayment == 1):
            for room in self.cart.room_list:
                room.status = "success"
            self.__reservations.append(Reservation(self.cart.room_list, 1))
            self.cart.clear_cart()
            return True
        else:
            return False

    def login(self):
        if self._username == self._username and self._password == self._password:
            return 'User login successful!'
        else:
            return 'Login failed..'  
    
    def __create_cart(self):
        self.__cart = Cart(self)
      
    def __get_room(self, roomtype, check_in_date, check_out_date):
        for room in roomtype.room_list:
            temp = []
            for roomreserved in reservation_list:
                if roomreserved.id == room.id and roomreserved.status != "fail":
                    temp.append(roomreserved)

            intersect = 0
            for roomreserved in temp:
                for date in range(roomreserved.check_in_date, roomreserved.check_out_date):
                    if date < check_out_date and date >= check_in_date:
                        intersect+=1
                        break
                    
            if(intersect == 0):
                return room
                    
        return None 

    @property
    def cart(self):
        return self.__cart
    
    @property
    def reservations(self):
        return self.__reservations

class Admin(Account):
    def __init__(self, username, password, email, phone_number, name):  
        super().__init__(username, password, email, phone_number)
        self.__name = name
