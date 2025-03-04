from saludtech.config.db import db
import uuid
from datetime import datetime

class ClinicalResult(db.Model):
    __tablename__ = "clinical_results"
    
    id = db.Column(db.String, primary_key=True)
    patient = db.Column(db.String, nullable=False)
    result = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
