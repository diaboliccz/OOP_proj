class Comment():
    def __init__(self, user, comment, rating):
        self.__user = user 
        self.__comment = comment
        self.__rating = rating

    @property
    def user(self):
        return self.__user
    
    @property
    def comment(self):
        return self.__comment
    
    @property
    def rating(self):
        return self.__rating
    
    