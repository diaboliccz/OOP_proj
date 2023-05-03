from datetime import datetime

class Comment:
    def __init__(self, user, hotel_name, room_type, comment, ratings, date):
        self.__user = user
        self.__hotel_name = hotel_name
        self.__room_type = room_type
        self.__comment = comment
        self.__ratings = ratings
        self.__date = date

    def to_dict(self):
        return {
            "username": self._username,
            "hotel_name": self._hotel_name,
            "room_type": self._room_type,
            "comment_text": self._comment_text,
            "ratings": self._ratings,
            "comment_date": self._comment_date.isoformat(),
        }
    def __str__(self):
        return f"{self.__average_rating:.1f} | {self.__user} | Hotel: {self.__hotel_name} | Room Type: {self.__room_type}| {self.__comment}  | ({self.__date:%Y-%m-%d}) reviewed"
   

    @property
    def hotel_name(self):
        return self.__hotel_name

    @property
    def date(self):
        return self.__date

    @property
    def user(self):
        return self.__user

    @property
    def hotel(self):
        return self.__hotel

    @property
    def room_type(self):
        return self.__room_type

    @property
    def content(self):
        return self.__comment


    @property
    def ratings(self):
        return self.__ratings

    @property
    def average_rating(self):
        return sum(self.__ratings.values()) / len(self.__ratings)

class CommentManager:
    def __init__(self):
        self.__comments = []


    def __str__(self):
        result = ""
        for comment in self.__comments:
            result += f"{comment.average_rating:.1f}  | {comment.user} | Hotel: {comment.hotel_name} | Room Type: {comment.room_type}| {comment.content}  | ({comment.date:%Y-%m-%d}) reviewed\n"
        return result
    def add_comment(self, comment):
        self.__comments.append(comment)

    def get_comments_by_hotel(self, hotel_name):
        comments_by_hotel = []
        for comment in self.__comments:
            if comment.hotel_name == hotel_name:
                comments_by_hotel.append(comment)
        if len(comments_by_hotel) > 0:
            return comments_by_hotel
        else:
            return None

    def get_comments_by_user(self, username):
        comments_by_user = []
        for comment in self.__comments:
            if comment.user == username:
                comments_by_user.append(comment)
        return comments_by_user

    
    def get_rating_classification(self,average_rating):
        if average_rating > 9:
            return "Exceptional"
        elif average_rating>= 8:
            return "Excellent"
        elif average_rating >= 7:
            return "Very Good"
        elif average_rating >= 6:
            return "Good"
        else:
            return "Below Expectation"

    def get_aggregated_ratings(self, hotel_name):
        comments = self.get_comments_by_hotel(hotel_name)
        num_comments = len(comments)

        if num_comments == 0:
            return None

        # Calculate the average rating for each comment
        comment_ratings = []
        for comment in comments:
            comment_ratings.append(comment.average_rating)

        # Calculate the overall rating as the average of the comment ratings
        overall_rating = sum(comment_ratings) 

        # Calculate the rating sum and classification
        rating_sum = {
            "overall": overall_rating,
            "cleanliness": 0,
            "facilities": 0,
            "location": 0,
            "service": 0,
            "value_for_money": 0
        }
        rating_classification = {}
        for comment in comments:
            for key in rating_sum.keys():
                rating_sum[key] += comment.ratings.get(key, 0)

        for key in rating_sum.keys():
            rating_sum[key] /= num_comments
            rating_classification[key] = self.get_rating_classification(rating_sum[key])
        
        rating_classification["overall"] = self.get_rating_classification(overall_rating)

        return rating_sum, rating_classification
