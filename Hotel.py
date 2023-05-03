import datetime
from dateutil.rrule import rrule, DAILY

class Agoda:
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

class Hotel:
    def __init__(self, hotel_name, hotel_type, address, map, policies, property_list, payment_list):
        self.__roomtype_list = []
        self.__hotel_name = hotel_name
        self.__hotel_type = hotel_type
        self.__address = address
        self.__map = map
        self.__total_rating = 0 
        self.__policies = policies
        self.__swimming_pool = property_list[0]
        self.__internet = property_list[1]
        self.__car_park = property_list[2]
        self.__gym = property_list[3]
        self.__non_smoking = property_list[4]
        self.__spa = property_list[5]
        self.__restaurant = property_list[6]
        self.__pet = property_list[7]
        self.__free_cancel = payment_list[0]
        self.__pay_at_hotel = payment_list[1]
        self.__pay_later = payment_list[2]
        self.__pay_now = payment_list[3]
        self.__credit_card = payment_list[4]
        
        self.__comment_list = []
    
    def __update_rating(self):
        sum = 0
        for comment in self.__comment_list:
            sum += comment.rating
        sum /= len(self.__comment_list)
        self.__total_rating = sum

    def add_comment(self, comment):
        self.__comment_list.append(comment)
        self.__update_rating()
        return True

    def add_room_type(self, room_type_info):
        self.__roomtype_list.append(RoomType(self, room_type_info["price"], room_type_info["sleeps"], room_type_info["room_size"], room_type_info["bed"], room_type_info["room_type"]))

    def add_room(self, index, count):
        self.__roomtype_list[index].add_room(count)

    @property
    def total_rating(self):
        return self.__total_rating

    @property
    def hotel_name(self):
        return self.__hotel_name
    
    @property
    def roomtype_list(self):
        return self.__roomtype_list
    
    @property
    def hotel_type(self):
        return self.__hotel_type
    
    @property 
    def payment_option(self):
        return self.__payment_option
    
    @property
    def property_facilities(self):
        return self.__property_facilities

    @property
    def swimming_pool(self):
        return self.__swimming_pool
    
    @property
    def internet(self):
        return self.__internet
    
    @property
    def car_park(self):
        return self.__car_park
    
    @property
    def gym(self):
        return self.__gym

    @property
    def non_smoking(self):
        return self.__non_smoking
    
    @property
    def spa(self):
        return self.__spa
    
    @property
    def restaurant(self):
        return self.__restaurant
    
    @property
    def pet(self):
        return self.__pet
    
    @property
    def free_cancel(self):
        return self.__free_cancel
    
    @property 
    def pay_at_hotel(self):
        return self.__pay_at_hotel
    
    @property
    def pay_later(self):
        return self.__pay_later
    
    @property
    def pay_now(self):
        return self.__pay_now
    
    @property
    def credit_card(self):
        return self.__credit_card

class RoomType:
    id = 0
    def __init__(self, hotel, price, sleeps, room_size, bed_type, room_type):
        self.__hotel = hotel
        self.__price = price
        self.__sleeps = sleeps
        self.__room_size = room_size
        self.__bed_type = bed_type
        self.__roomtype_name = room_type
        self.__room_list = []
        RoomType.id += 1

    def add_room(self, count):
        for i in range(count):
            self.__room_list.append(Room(self.__hotel, self))

    @property
    def room_list(self):
        return self.__room_list
    
    @property
    def price(self):
        return self.__price
    
    @property
    def sleeps(self):
        return self.__sleeps
    
    @property
    def roomtype_name(self):
        return self.__roomtype_name
    
    @property
    def bed_type(self):
        return self.__bed_type
    
    @property
    def roomtype_info(self):
        return {"sleeps" : self.__sleeps,
                "bed" : self.__bed_type,
                "price" : self.__price,
                "room_size" : self.__room_size
                }

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
            for date in rrule(DAILY, dtstart=roomreserved.check_in_date, until=roomreserved.check_out_date):
                if date < check_out_date and date >= check_in_date:
                    intersect+=1
                    break
                
        if(intersect == 0):
            return True
        else:
            return False
        
class Reservation():
    def __init__(self, room_list, date):
        self.__room_reserved_list = room_list
        self.__date_pay = date

    @property
    def room_reserved_list(self):
        return self.__room_reserved_list
    
    @property
    def date_pay(self):
        return self.__date_pay
    
    def booked_list(self):
        temp = [self.__date_pay]
        sum = 0 
        for room in self.__room_reserved_list:
            sum += room.price
            temp.append([room.hotel.hotel_name, room.check_in_date, room.check_out_date])
        temp.append(sum)
        return temp
    
class RoomReserved(Room):
    def __init__(self, room, check_in_date, check_out_date , status="pending"):
        super().__init__(room.hotel, room.roomtype, room.id)
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status
        self.__price = (check_out_date - check_in_date).days * self._roomtype.price

    @property
    def check_in_date(self):
        return self.__check_in_date
    
    @property
    def check_out_date(self):
        return self.__check_out_date
    
    @property
    def status(self):
        return self.__status
    
    @property
    def price(self):
        return self.__price
    
    @status.setter
    def status(self, value):
        self.__status = value
        return self.__status



agoda = Agoda()