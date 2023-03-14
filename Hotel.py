hotel_info = {
    "hotel_name": "Hottestel",
    "facility": ["wifi", "parking_zone", "gym", "swimming_pool", "breakfast"],
    "address": "55/28 Thonglor Sukhmvit",
    "map": "13.740257,460.548432",
    "policies": ["no_smoking", "no_pet", "no_noise"]

}

class Hotel:
    def __init__(self, hotel_name, facility, address, map, policies):
        self.__hotel_name = hotel_name
        self.__facility = facility
        self.__address = address
        self.__map = map
        self.__policies = policies
