from models import MLModel
from sqlalchemy.orm import Session

def create_model(db: Session, name: str, version: str, accuracy: float, file_path: str):
    db_model = MLModel(name=name, version=version, accuracy=accuracy, file_path=file_path)
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

def get_all_models(db: Session):
    return db.query(MLModel).all()

def get_model_by_name(db: Session, name: str):
    return db.query(MLModel).filter(MLModel.name == name).first()
