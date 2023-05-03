from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from Comment import Comment, CommentManager

app = FastAPI()
comment_manager = CommentManager()

class CreateComment(BaseModel):
    username: str
    hotel_name: str
    room_type: str
    comment_text: str
    ratings: dict

class CommentResponse(BaseModel):
    success: bool
    comments: list

@app.post("/create_comment/")
async def create_comment(comment: CreateComment):
    user = comment.username
    hotel_name = comment.hotel_name
    room_type = comment.room_type
    comment_text = comment.comment_text
    ratings = comment.ratings
    date = datetime.now()
    new_comment = Comment(user, hotel_name, room_type, comment_text, ratings, date)
    comment_manager.add_comment(new_comment)
    return {"success": True, "message": "Comment created successfully"}

@app.get("/get_comments_by_hotel/{hotel_name}")
async def get_comments_by_hotel(hotel_name: str):
    comments = comment_manager.get_comments_by_hotel(hotel_name)
    if comments:
        return {"success": True, "comments": [comment.to_dict() for comment in comments]}
    else:
        raise HTTPException(status_code=404, detail="No comments found for hotel")

@app.get("/get_comments_by_user/{username}")
async def get_comments_by_user(username: str):
    comments = comment_manager.get_comments_by_user(username)
    if comments:
        return {"success": True, "comments": [comment.to_dict() for comment in comments]}
    else:
        raise HTTPException(status_code=404, detail="No comments found for user")

@app.get("/get_aggregated_ratings/{hotel_name}")
async def get_aggregated_ratings(hotel_name: str):
    rating_sum, rating_classification = comment_manager.get_aggregated_ratings(hotel_name)
    if rating_sum and rating_classification:
        return {"success": True, "rating_sum": rating_sum, "rating_classification": rating_classification}
    else:
        raise HTTPException(status_code=404, detail="No comments found for hotel")

@app.get("/get_comments_by_date_range", response_model=CommentResponse)
async def get_comments_by_date_range(start_date: str, end_date: str):
    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
    comments = comment_manager.get_comments_by_date_range(start_date_obj, end_date_obj)
    if comments:
        return {"success": True, "comments": [comment.to_dict() for comment in comments]}
    else:
        raise HTTPException(status_code=404, detail="No comments found within the specified date range.")
