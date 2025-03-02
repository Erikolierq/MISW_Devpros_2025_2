"""Data Transfer Objects (DTO) para mapear la entidad ClinicalResult con la base de datos (SQLAlchemy)."""

from sqlalchemy import Column, Integer, String
from config.db import db

class ClinicalResultDTO(db.Model):
    __tablename__ = 'clinical_results'

    id = Column(Integer, primary_key=True)
    patient = Column(String(100), nullable=False)
    result = Column(String(200), nullable=False)
