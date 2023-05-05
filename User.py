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

    def update_item(self):
        for room in self.__room_list:
            room.update()
        self.__update()

    def __update(self):
        self.__total_price = 0
        for room in self.__room_list:
            if room.status != "fail":
                room_price = room.price 
                self.__total_price += room_price
        return True
    
    def show_item(self):
        self.update_item()
        res = {}
        temp = []
        for reserved in (self.__room_list):
            temp.append({"hotel_name":reserved.hotel.hotel_name, "roomtype":reserved.roomtype.roomtype_name, "check_in_date":reserved.check_in_date.strftime("%y-%m-%d"), "check_out_date":reserved.check_out_date.strftime("%y-%m-%d"), "status" : reserved.status})
        res.update({"hotel_list": temp})
        res.update({"summary" : self.__total_price})
        return res

    def not_empty(self):
        for room in self.__room_list:
            if room.status != "fail":
                return True
        return False

    @property
    def total_price(self):
        return self.__total_price

    @property
    def room_list(self):
        return self.__room_list

class Account():
    def __init__(self, username, password, email, phone_number):
        self._username = username
        self._password = password
        self._email = email
        self._phone_number = phone_number

    @property
    def username(self):
        return self._username
    
    @property
    def email(self):
        return self._email

class User(Account):
    def __init__(self, username, password, email, phone_number, full_name):  
        super().__init__(username, password, email, phone_number)
        self.__full_name = full_name
        self.__reservations = []
        self.__create_cart()

    def add_to_cart(self, hotel_name, roomtype_name, check_in_date, check_out_date, wanted_room):
        roomtype = catalog.get_roomtype(hotel_name, roomtype_name)
        if(roomtype):
            room_list = agoda.get_room(roomtype, check_in_date, check_out_date, wanted_room)
            if room_list:
                locked_list = agoda.make_locked_room(room_list, check_in_date, check_out_date)
                for locked_room in locked_list:
                    self.cart.add(locked_room)
                return True
        return False

    def check_out(self):
        if self.cart.not_empty():
            reservation = agoda.check_out(self.cart.room_list, self.cart.total_price)
            self.cart.clear_cart()
            self.__reservations.append(reservation)
            return True
        else:
            return False
    
    def __create_cart(self):
        self.__cart = Cart(self)

    def comment_rating(self, hotel_name, comment, rating):
        return catalog.add_comment(self, hotel_name, comment, rating)
        
    def get_history_list(self):
        res = []
        for reservation in self.__reservations:
            res.append({"id":reservation.id, "date_pay": reservation.date_pay.strftime("%y-%m-%d"), "total":reservation.price, "refundable":reservation.refundable, "cancel" : reservation.cancel})
        return {"result" : res}

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

class AccountList():
    def __init__(self):
        self.__account_list = []

    def __is_unique(self, username, email):
        for user in self.__account_list:
            if user.username == username or user.email == email:
                return False
        return True

    def register(self, username, password, email, phone_number, full_name):
        if(self.__is_unique):
            user = User(username, password, email, phone_number, full_name)
            self.__account_list.append(user)
            return True
        else:
            return False
        
    def get_history(self, id):
        for account in self.__account_list:
            if(isinstance(account, User)):
                for reservation in account.reservations:
                    if reservation.id == id:
                        return reservation.show_item()
        return {"status" : "Not Found"}
        
    def refund(self, id):
        for account in self.__account_list:
            if(isinstance(account, User)):
                for reservation in account.reservations:
                    if reservation.id == id:
                        return reservation.refund()
        return {"status" : "Not Found"}

    def find_user(self, username):
        for user in self.__account_list:
            if user.username == username:
                return user
        return False
    
account_list = AccountList()