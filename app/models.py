from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class MLModel(Base):
    __tablename__ = "mlmodels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    version = Column(String)
    accuracy = Column(Float)
    file_path = Column(String)
    registered_at = Column(DateTime(timezone=True), server_default=func.now())
