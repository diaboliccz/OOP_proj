hotel_info = {
    "hotel_name": "Hottestel",
    "facility": ["wifi", "parking_zone", "gym", "swimming_pool", "breakfast"],
    "address": "55/28 Thonglor Sukhmvit",
    "map": "13.740257,460.548432",
    "property_facilities": [0,0,0,0,1,1,1,1],
    "paymrnt_option" : [0,1,1,1,0]

}

class Hotel:
    def __init__(self, hotel_name, hotel_type, facility, address, map, policies):
        self.__hotel_name = hotel_name
        self.__hotel_type = hotel_type
        self.__facility = facility
        self.__address = address
        self.__map = map
        self.__total_rating = 0 
        self.__policies = policies
        self.__swimming_pool = False
        self.__internet = False
        self.__car_park = False
        self.__gym = False
        self.__non_smoking = False
        self.__spa = False
        self.__restaurant = False
        self.__pet = False
        self.__free_cancel = False
        self.__pay_at_hotel = False
        self.__pay_later = False
        self.__pay_now = False
        self.__credit_card = False
        self.__property_facilities = [self.__swimming_pool, self.__internet, self.__car_park, self.__gym, self.__non_smoking, self.__spa, self.__restaurant, self.__pet]
        self.__payment_option = [self.__free_cancel, self.__pay_at_hotel, self.__pay_later, self.__pay_now, self.__credit_card]


    def __edit_property_facilities(self, bit):
        pass
    
    def __edit_payment_option(self, bit):
        pass