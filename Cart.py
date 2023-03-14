class Cart():
    def __init__(self, reservation, cart):
        self.__reservation = reservation
        self.__payment = cart

    def checkout(self):
        if self.__payment.make_payment():
            self.__reservation.create_reserve_room()
