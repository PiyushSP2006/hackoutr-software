from fastapi import APIRouter,Depends
from ..database import get_db
from sqlalchemy.orm import Session 

from .. import schemas,models

router=APIRouter()

@router.post("/submit_issue")
def submit_issue_home(issue:schemas.Issue_submit,db:Session=Depends(get_db)):
    new_issue=models.Issue(
        issue_type=issue.issue_type,
        issue_location=issue.issue_location,
        issue_detail=issue.issue_details,
        submitted_by=1
    )

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return {"issue":issue}