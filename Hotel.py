from RoomType import *
from Comment import CommentManager
class Hotel:
    def __init__(self, hotel_name, hotel_type, address, map, policies, property_list, payment_list):
        
        self.__reviews = []
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
        
    

    
    def add_room_type(self, room_type_info):
        self.__roomtype_list.append(RoomType(self, room_type_info["price"], room_type_info["sleeps"], room_type_info["room_size"], room_type_info["bed"], room_type_info["room_type"]))

    def add_room(self, index, count):
        self.__roomtype_list[index].add_room(count)
    def get_comments(self, comment_manager):
        comments = comment_manager.get_comments_by_hotel(self.hotel_name)
        comments.sort(key=lambda x: x.date, reverse=True)
        return comments
    def add_review(self, user, rating, comment):
        self.__total_rating = (self.__total_rating * len(self.__reviews) + rating) / (len(self.__reviews) + 1)
        self.__reviews.append({"user": user, "rating": rating, "comment": comment})
        self.__comment_manager.add_comment(self.hotel_name, user, rating, comment)


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
    