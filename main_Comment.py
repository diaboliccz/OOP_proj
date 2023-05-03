from datetime import datetime
from Comment import Comment, CommentManager

# Test case 1: Create a comment and verify its properties
comment1 = Comment("user1", "hotel1", "room1", "Great hotel!", {"cleanliness": 9, "facilities": 8, "location": 10, "service": 9, "value_for_money": 8}, datetime.now())
assert comment1.user == "user1"
assert comment1.hotel_name == "hotel1"
assert comment1.room_type == "room1"
assert comment1.content == "Great hotel!"
assert comment1.ratings == {"cleanliness": 9, "facilities": 8, "location": 10, "service": 9, "value_for_money": 8}
assert comment1.average_rating == 8.8

# Test case 2: Create a comment manager, add a comment, and get comments by hotel
comment_manager = CommentManager()
comment_manager.add_comment(comment1)
assert comment_manager.get_comments_by_hotel("hotel1") == [comment1]
assert comment_manager.get_comments_by_hotel("hotel2") is None

# Test case 3: Get comments by user
assert comment_manager.get_comments_by_user("user1") == [comment1]
assert comment_manager.get_comments_by_user("user2") == []

# Test case 4: Get rating classification
assert comment_manager.get_rating_classification(9.5) == "Exceptional"
assert comment_manager.get_rating_classification(8.8) == "Excellent"
assert comment_manager.get_rating_classification(7.5) == "Very Good"
assert comment_manager.get_rating_classification(6.5) == "Good"
assert comment_manager.get_rating_classification(5.5) == "Below Expectation"


comment2 = Comment("user2", "hotel1", "room2", "Terrible hotel!", {"cleanliness": 2, "facilities": 1, "location": 5, "service": 1, "value_for_money": 1}, datetime.now())
comment_manager.add_comment(comment2)
comment_manager = CommentManager()
comment_manager.add_comment(comment1)
comment_manager.add_comment(comment2)
print(comment_manager)

# Test case 5: Get aggregated ratings
rating_sum, rating_classification = comment_manager.get_aggregated_ratings("hotel1")
print("actual rating_sum:", rating_sum)


assert rating_sum == {'overall': 5.4, 'cleanliness': 5.5, 'facilities': 4.5, 'location': 7.5, 'service': 5.0, 'value_for_money': 4.5}

assert rating_classification == {"overall": "Below Expectation", "cleanliness": "Below Expectation", "facilities": "Below Expectation", "location": "Very Good", "service": "Below Expectation", "value_for_money": "Below Expectation"}

print("All test cases passed!")
