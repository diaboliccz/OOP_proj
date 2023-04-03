import datetime
class Comment():
    def __init__(self, user,hotel, comment,rating):
        self.__user = user 
        self.__hotel = hotel
        self.__comment = comment
        self.__rating = rating
        self.__comment_date = datetime.datetime.now()
    @property
    def user(self):
        return self.__user
    @property
    def hotel(self):
        return self.__hotel
    @property
    def comment(self):
        return self.__comment
    @property
    def rating(self):
        return self.__rating
    @property
    def comment_date(self):
        return self.__comment_date
    def __str__(self):
        return f"{self.user.full_name} | ({self.__comment_date}) --> {self.__comment} | Rating : {self.__rating}"
    