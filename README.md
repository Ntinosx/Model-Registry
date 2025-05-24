**Project Structure & Summary**

**main.py**
FastAPI app with endpoints:
POST /models: Uploads model file (.pkl) + metadata (name, version, accuracy). Saves file and metadata in PostgreSQL.
GET /models: Returns metadata of all uploaded models.
GET /models/{name}: Returns metadata of a specific model by name.

**models.py**
SQLAlchemy ORM model definitions for the Model metadata table.

**crud.py**
Database functions to create and retrieve model metadata entries.

**database.py**
Database connection setup and session management for PostgreSQL.

**Dockerfile**
Containerizes the FastAPI app:
Uses Python 3.11 slim image.
Installs dependencies from requirements.txt.
Copies app files.
Creates a models/ directory to store uploaded models.
Runs the app using uvicorn on port 8000.

**docker-compose.yml**
Defines two services:

**db:** PostgreSQL container with volume for data persistence and environment variables for user/db setup.
**api:** FastAPI app container that depends on db, exposes port 8000, mounts a local models/ folder for model files, and shares database connection info via environment variables.
FastAPI app with endpoints:

**Build and start containers:**

docker-compose up --build


How to Create a Test Model and Upload
Create a dummy .pkl file using Python:

Create a file create_test_model.py with:

import pickle

dummy_model = {"model": "test"}
with open("test_model.pkl", "wb") as f:
    pickle.dump(dummy_model, f)
print("test_model.pkl created!")


python create_test_model.py

This generates test_model.pkl in the current directory.

Upload the test model using curl:

curl -X POST "http://localhost:8000/models" \
  -F "name=test_model" \
  -F "version=1.0" \
  -F "accuracy=0.95" \
  -F "file=@test_model.pkl"
  
Check uploaded models metadata:

curl http://localhost:8000/models

