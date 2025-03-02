from config.db import db
from sqlalchemy import Column, Integer, String

class AuthUserDTO(db.Model):
    __tablename__ = 'auth_users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(Integer, nullable=False)
