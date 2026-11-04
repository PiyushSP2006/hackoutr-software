from fastapi import APIRouter,Depends
from ..database import get_db
from sqlalchemy.orm import Session 

from .. import schemas,models

router=APIRouter()

@router.post("/user/create_user")
def create_new_user(User_submit:schemas.User_submit,db:Session=Depends(get_db)):
    new_user=models.User(
        user_name=User_submit.userName,
        user_aadhar=User_submit.userAadhar,
        user_email=User_submit.userEmail,
        user_number=User_submit.userNumber
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"issue":new_user}