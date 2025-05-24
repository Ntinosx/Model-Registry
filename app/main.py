from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from database import SessionLocal, engine, Base
import models
import crud
import shutil

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/models")
async def upload_model(
    name: str = Form(...),
    version: str = Form(...),
    accuracy: float = Form(...),
    file: UploadFile = File(...)
):
    db = SessionLocal()
    try:
        filename = f"models/{name}_{version}.pkl"
        with open(filename, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        model = crud.create_model(db, name, version, accuracy, filename)
        return JSONResponse(content={"message": "Model uploaded", "model_id": model.id})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.get("/models")
def get_all_models():
    db = SessionLocal()
    models_list = crud.get_all_models(db)
    db.close()
    return models_list

@app.get("/models/{name}")
def get_model_by_name(name: str):
    db = SessionLocal()
    model = crud.get_model_by_name(db, name)
    db.close()
    if not model:
        raise HTTPException(status_code=404, detail="Model not found")
    return model
