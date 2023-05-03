from Hotel import *
from HotelCatalog import *

class Cart():
    def __init__(self, user):
        self.__user = user
        self.__room_list = []
        self.__total_price = 0
        self.__payment_status = False
    
    def add(self, room):
        self.__room_list.append(room)
        self.__update()

    def clear_cart(self):
        self.__room_list = []
        self.__update()

    def __update(self):
        self.__total_price = 0
        for room in self.__room_list:
            room_price = room.price 
            self.__total_price += room_price

        return True
    
    @property
    def total_price(self):
        return self.__total_price

    @property
    def room_list(self):
        return self.__room_list

    def show_item(self):
        res = {}
        temp = []
        sum = 0
        for reserved in (self.__room_list):
            sum += reserved.price
            temp.append({"hotel_name":reserved.hotel.hotel_name, "roomtype":reserved.roomtype.roomtype_name, "check_in_date":reserved.check_in_date.strftime("%y-%m-%d"), "check_out_date":reserved.check_out_date.strftime("%y-%m-%d")})
        res.update({"hotel_list": temp})
        res.update({"summary" : sum})
        return res

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

