from config.db import db
from sqlalchemy import Column, Integer, String

class CertPermissionDTO(db.Model):
    __tablename__ = 'cert_permissions'

    role_id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
