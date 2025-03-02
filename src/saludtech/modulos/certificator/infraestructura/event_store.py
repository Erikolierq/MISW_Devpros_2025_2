from datetime import datetime
from sqlalchemy import Column, Integer, String, JSON, DateTime, Boolean
from config.db import db

class EventStore(db.Model):
    __tablename__ = 'cert_event_store'

    id = Column(Integer, primary_key=True)
    event_name = Column(String(100), nullable=False)
    event_data = Column(JSON, nullable=False)
    event_version = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    processed = Column(Boolean, default=False)

class EventStoreRepository:
    def __init__(self, session):
        self.session = session

    def save_event(self, event):
        # Similar a item_valor, para guardar eventos con event_name, event_data, etc.
        pass

    def mark_event_processed(self, event_id: int):
        pass

    def is_event_processed(self, event):
        pass
