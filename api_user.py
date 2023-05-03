from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from User import User, UserDatabase, Admin
from Comment import Comment
app = FastAPI()
user_db = UserDatabase()

# Pydantic models for request bodies
class CreateUser(BaseModel):
    username: str
    password: str
    email: str
    phone_number: str
    full_name: str

class Login(BaseModel):
    username: str
    password: str

class UpdatePassword(BaseModel):
    old_password: str
    new_password: str

class LeaveComment(BaseModel):
    hotel_name: str
    room_type: str
    comment_text: str
    ratings: dict

@app.post("/create_account/")
async def create_account(user: CreateUser):
    new_user = User(user.username, user.password, user.email, user.phone_number, user.full_name)
    if user_db.create_account(new_user):
        return {"success": True, "message": "Account created successfully"}
    else:
        raise HTTPException(status_code=400, detail="Account creation failed")

@app.post("/login/")
async def login(credentials: Login):
    user = user_db.authenticate_user(credentials.username, credentials.password)
    if user:
        return {"success": True, "message": "Logged in successfully", "username": user._username}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/update_password/")
async def update_password(username: str, password_data: UpdatePassword):
    user = user_db.get_user(username)
    if user:
        success = user.update_password(password_data.old_password, password_data.new_password)
        if success:
            return {"success": True, "message": "Password updated successfully"}
        else:
            raise HTTPException(status_code=401, detail="Invalid old password")
    else:
        raise HTTPException(status_code=404, detail="User not found")

@app.post("/leave_comment/")
async def leave_comment(username: str, comment_data: LeaveComment):
    user = user_db.get_user(username)
    if user:
        result = user.leave_comment(
            comment_data.hotel_name,
            comment_data.room_type,
            comment_data.comment_text,
            comment_data.ratings,
        )
        # add this line to ensure the comment was actually added to the user
        print(user._comments)
        return {"success": True, "message": result}
    else:
        raise HTTPException(status_code=404, detail="User not found")




@app.get("/show_comments/{username}")
async def show_comments(username: str):
    user = user_db.get_user(username)
    if user:
        comments = [comment.to_dict() for comment in user._comments]
        if comments:
            return {"success": True, "comments": comments}
        else:
            raise HTTPException(status_code=404, detail="No comments found for user")
    else:
        raise HTTPException(status_code=404, detail="User not found")

