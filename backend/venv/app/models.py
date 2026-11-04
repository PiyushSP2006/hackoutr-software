from sqlalchemy import Column, Integer, String, TIMESTAMP, func, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from .database import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)
    user_aadhar = Column(Integer, unique=True, nullable=False)
    user_number = Column(String, unique=True, nullable=False)
    user_email = Column(String, unique=True, nullable=False)


class Issue(Base):
    __tablename__ = "issues"

    issue_id = Column(Integer, primary_key=True, autoincrement=True)
    issue_type = Column(String, nullable=True)
    issue_detail = Column(String, nullable=True)
    issue_location = Column(JSONB, nullable=False)
    told_at = Column(TIMESTAMP(timezone=True), server_default=func.now())

    submitted_by = Column(
        Integer,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )