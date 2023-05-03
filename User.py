from Cart import Cart
from Reservation import Reservation
from Comment import *
from RoomReserved import RoomReserved
from HotelCatalog import *
from Agoda import Agoda
from datetime import datetime
from verification import *
import bcrypt ,uuid



class Account:
    def __init__(self, username, password, email, phone_number):
        self._username = username
        self._password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self._email = email
        self._phone_number = phone_number

class User(Account):
    def __init__(self, username, password, email, phone_number, full_name):
        super().__init__(username, password, email, phone_number)
        self._username = username  
        self._password = self._password
        self._email = email
        self._phone_number = phone_number
        self._full_name = full_name
        self._comments = []
        self.__comment_manager = CommentManager()
    def set_email_verification_token(self, token):
        self.__email_verification_token = token
    def verify_email(self, token):
        if token == self.__email_verification_token:
            self.__email_verified = True
            return True
        else:
            return False
    
    def update_password(self, old_password, new_password):
        if bcrypt.checkpw(old_password.encode('utf-8'), self._password):
            self._password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            return True
        else:
            return False
    
   
    def leave_comment(self, hotel_name, room_type, comment_text, ratings):
        comment_manager = CommentManager()
        comment_date = datetime.now()
        comment = Comment(self._username, hotel_name, room_type, comment_text, ratings, comment_date)
        comment_manager.add_comment(comment)
        return "Comment successfully added"


    '''def show_comments(self):
        for comment in self.__comment_manager.get_comments_by_user(self._username):  # Change this line
            print(comment)
    '''
    


class UserDatabase:
    def __init__(self):
        self.__users = []

    def add_user(self, user):
        self.__users.append(user)

    def remove_user(self, username):
        user = self.get_user(username)
        if user is not None:
            self.__users.remove(user)

    def get_user(self, username):
        for user in self.__users:
            if user._username == username:
                return user
        return None

   

    def login(self, username, password):
        user = self.get_user(username)
        if user is not None and bcrypt.checkpw(password.encode('utf-8'), user._password):
            return user
        else:
            return None

    def create_account(self, user):
        if self.get_user(user._username) is None:
            self.add_user(user)
            user.set_email_verification_token(str(uuid.uuid4()))
            return True
        else:
            return False

    def authenticate_user(self, username, password):
        user = self.get_user(username)
        if user and bcrypt.checkpw(password.encode('utf-8'), user._password):
            return user
        else:
            return None

    def authenticate_user_with_token(self, token):
        user = self.get_user_by_token(token)
        if user:
            return user
        else:
            return None

    def get_user_by_token(self, token):
        for user in self.__users:
            if getattr(user, '_email_verification_token', None) == token:
                return user
        return None

    def logout_user(self, user):
        user.set_email_verification_token(None)

    @property
    def get_all_users(self):
        return self.__users
    

class Admin(Account):
    def __init__(self, user_database, username, password, email, phone_number, name):  
        super().__init__(username, password, email, phone_number)
        self.__name = name
        self.__user_database = user_database
        

    def add_user(self, user):
        self.__user_database.add_user(user)

    def remove_user(self, username):
        self.__user_database.remove_user(username)

    def update_user_info(self, username, updated_info):
        user = self.__user_database.get_user(username)
        if user is not None:
            for key, value in updated_info.items():
                if hasattr(user, key):
                    setattr(user, key, value)
                else:
                    print(f"Warning: Invalid attribute '{key}'")
        else:
            print(f"User '{username}' not found")

    

    
    def list_users(self):
        return self.__user_database.get_all_users

   
    def get_user(self, username):
        return self.__user_database.get_user(username)
    
