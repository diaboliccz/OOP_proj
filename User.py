from Cart import *
from Reservation import *
from HotelCatalog import *
from Comment import *
from Agoda import agoda


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
    
    def __convert_date(self, date):
        y,m,d = date.split("-")
        return datetime.datetime(int(y), int(m), int(d))

    def add_to_cart(self, hotel_name, roomtype_name, check_in_date, check_out_date):
        for hotel in catalog.hotel_list:
            if(hotel.hotel_name == hotel_name):
                for roomtype in hotel.roomtype_list:
                    if(roomtype.roomtype_name == roomtype_name):
                        roomtype_to_reserve = roomtype

        check_in_date = self.__convert_date(check_in_date)
        check_out_date = self.__convert_date(check_out_date)

        room = self.__get_room(roomtype_to_reserve, check_in_date, check_out_date)
        if(room):
            locked_room = RoomReserved(room, check_in_date, check_out_date)
            self.cart.add(locked_room)
            agoda.add_room(locked_room)
            return True
        else:
            return False

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
    
    def __create_cart(self):
        self.__cart = Cart(self)
      
    def __get_room(self, roomtype, check_in_date, check_out_date):
        for room in roomtype.room_list:
            if room.is_available(check_in_date, check_out_date):
                return room
        return None

    def comment_rating(self, hotel, comment, rating):
        comment = Comment(self, comment, rating)
        return hotel.add_comment(comment)
        
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
