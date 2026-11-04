from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

class Issue_submit(BaseModel):
    issue_type:str
    issue_location:dict
    issue_details:str

class Issue_response(Issue_submit):
    pass 

class User_submit(BaseModel):
    userName:str
    userAadhar:int 
    userEmail:EmailStr
    userNumber:int

class User_response(User_submit):
    pass
