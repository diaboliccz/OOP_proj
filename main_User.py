import bcrypt
from User import User, UserDatabase, Admin

# create a UserDatabase instance
user_db = UserDatabase()

# create a user
user1 = User("user1", "password748r9932", "user1@gmail.com", "555-5555", "Baba Rahman")

# create a user account
if user_db.create_account(user1):
    print("Account created for user1")
else:
    print("Account creation failed for user1")

# authenticate user with username and password
authenticated_user = user_db.authenticate_user("user1", "password748r9932")
if authenticated_user:
    print("Authentication successful for user1")
else:
    print("Authentication failed for user1")

# set and verify email
user1.set_email_verification_token("123456")
if user1.verify_email("123456"):
    print("Email verified for user1")
else:
    print("Email verification failed for user1")

# log in the user
logged_in_user = user_db.login("user1", "password748r9932")

if logged_in_user:
    print("Logged in user1 successfully")
    # print account information
    print("Username:", logged_in_user._username)
    print("Email:", logged_in_user._email)
    print("Phone Number:", logged_in_user._phone_number)
    print("Full Name:", logged_in_user._full_name)
    # update the user's password
    updated = logged_in_user.update_password("password748r9932", "new_password")
    assert updated is True

    # leave a comment
    comment = "This hotel was great!"
    ratings = {"cleanliness": 6, "facilities": 8, "location": 9, "service": 7, "value_for_money": 6.5}
    result = logged_in_user.leave_comment("Best Hotel", "King Suite", comment, ratings)
    assert result == "Comment successfully added"

    # show the user's comments
    logged_in_user.show_comments()

    # log out the user
    user_db.logout_user(logged_in_user)
    print("Logged out user1 successfully")
else:
    print("Failed to log in user1")

# create an admin
admin = Admin(user_db, "admin", "admin_password", "admin@gmail.com", "555-5555", "Admin Name")

# add a user as the admin
user2 = User("user2", "password", "user2@gmail.com", "555-5555", "Jane Smith")
admin.add_user(user2)
print("User2 added by admin")

# list all users as the admin
all_users = admin.list_users()
print("All users:", [user._username for user in all_users])

# get a specific user as the admin
user1 = admin.get_user("user1")
if user1:
    print("Admin fetched user1 successfully")
else:
    print("Admin failed to fetch user1")

# update the user's email as the admin
admin.update_user_info("user1", {"_email": "new_email@gmail.com"})
print("User1 email updated by admin")

# remove the user as the admin
admin.remove_user("user2")
print("User2 removed by admin")

# list all users as the admin after removing user2
all_users = admin.list_users()
print("All users after removing user2:", [user._username for user in all_users])



password = "password748r9932"
expected_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print("Expected hash:", expected_hash)

stored_hash = expected_hash

# when a user logs in, we can compare their plain text password with the stored hash
login_password = "password748r9932"
if bcrypt.checkpw(login_password.encode('utf-8'), stored_hash):
    print("Login successful!")
else:
    print("Login failed!")
    
