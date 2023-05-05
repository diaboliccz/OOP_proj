import datetime
from dateutil.rrule import rrule, DAILY

class Agoda():
    def __init__(self):
        self.__reservation_list = []

    def add_room(self, room):
        self.__reservation_list.append(room)

    def __convert_date(self, date):
        y,m,d = date.split("-")
        return datetime.datetime(int(y), int(m), int(d))
    
    def get_room(self, roomtype, check_in_date, check_out_date, wanted_room):
        check_in_date = self.__convert_date(check_in_date)
        check_out_date = self.__convert_date(check_out_date)
        room_list = []
        for room in roomtype.room_list:
            if room.is_available(check_in_date, check_out_date):
                room_list.append(room)
                if(len(room_list) >= wanted_room):
                    return room_list
        return None

    def make_locked_room(self, room_list, check_in_date, check_out_date):
        check_in_date = self.__convert_date(check_in_date)
        check_out_date = self.__convert_date(check_out_date)
        locked_list = []
        for room in room_list:
            locked_room = RoomReserved(room, check_in_date, check_out_date)
            locked_list.append(locked_room)
            self.reservation_list.append(locked_room)
        return locked_list

    def check_out(self, room_list, price):
        success_room = []
        refund_able = True
        for room in room_list:
            if room.status != "fail":
                if not room.hotel.free_cancel:
                    refund_able = False
                success_room.append(room)
                room.status = "success"
        return Reservation(success_room, price, refund_able)

    @property 
    def reservation_list(self):
        return self.__reservation_list
    
    def get_status(self):
        temp = [] 
        for room in self.__reservation_list:
            temp.append(room.status)

        return temp

class Hotel():
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
    def comment_list(self):
        return self.__comment_list

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
    
    @property
    def address(self):
        return self.__address

class RoomType():
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

class Room():
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
    ID = 0
    def __init__(self, room_list, price, refundable):
        self.__id = Reservation.ID
        Reservation.ID += 1
        self.__room_reserved_list = room_list
        self.__price = price
        self.__refundable = refundable
        self.__cancel = False
        self.__date_pay = datetime.datetime.now()

    @property
    def cancel(self):
        return self.__cancel

    @property
    def refundable(self):
        return self.__refundable

    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price

    @property
    def room_reserved_list(self):
        return self.__room_reserved_list
    
    @property
    def date_pay(self):
        return self.__date_pay
    
    
    def show_item(self):
        res = {}
        temp = []
        for reserved in (self.__room_reserved_list):
            temp.append({"hotel_name":reserved.hotel.hotel_name, "roomtype":reserved.roomtype.roomtype_name, "check_in_date":reserved.check_in_date.strftime("%y-%m-%d"), "check_out_date":reserved.check_out_date.strftime("%y-%m-%d"), "price" : reserved.price})
        res.update({"hotel_list": temp})
        res.update({"summary" : self.__price})
        res.update({"refund" : self.__refundable})
        res.update({"cancel": self.__cancel})
        return res
    
    def refund(self):
        self.__cancel = True
        for room in self.__room_reserved_list:
            room.cancel()
        return {"status" : "Success"}
    
class RoomReserved(Room):
    def __init__(self, room, check_in_date, check_out_date , status="pending"):
        super().__init__(room.hotel, room.roomtype, room.id)
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status
        self.__created_date = datetime.datetime.now()
        self.__price = (check_out_date - check_in_date).days * self._roomtype.price

    def update(self):
        print((datetime.datetime.now() - self.created_date).seconds)
        if (datetime.datetime.now() - self.created_date).seconds > 10:
            self.__status = "fail"

    def cancel(self):
        self.__status = "fail"

    @property
    def created_date(self):
        return self.__created_date

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