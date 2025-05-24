 **Project Structure & Summary**

| File/Folder            | Description                                                                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **main.py**            | FastAPI app with endpoints: POST /models: Upload model file + metadata (name, version, accuracy), GET /models: Return metadata of all uploaded models. GET /models/{name}: Return metadata of a specific model.                      |
| **models.py**          | SQLAlchemy ORM definitions for the `Model` metadata table.                                                                                                                                                                           |
| **crud.py**            | Database helper functions to create and retrieve model metadata.                                                                                                                                                                     |
| **database.py**        | PostgreSQL database connection setup and session management.                                                                                                                                                                         |
| **Dockerfile**         | Builds the FastAPI app container: Uses Python 3.11 slim image. Installs dependencies. Copies app files. Creates `models/` directory. Runs the app on port 8000 using uvicorn.                                                        |
| **docker-compose.yml** | Defines two services: **db**: PostgreSQL container with persistent volume and env setup. **api**: FastAPI container depending on db, exposing port 8000, sharing a local models folder.                                              |


** How to Build and Start Containers**
docker-compose up --build


**CI/CD Pipeline**
 This project uses GitHub Actions to automate testing and deployment.

Pipeline Overview
On every push or pull request to the main branch, the workflow: 

**Builds & starts services**
Uses the Dockerfile and docker-compose.yml to spin up the db and api containers.

 **Tests the API**
Runs a Python script that creates test_model.pkl.
Uploads the test model using the POST /models endpoint.
 Sends GET requests to:
Check the uploaded model (/models/{name}).
Verify the system handles non-existing models (expects a 404).

 **Archives logs**
Collects Docker Compose logs.
Uploads logs as artifacts for troubleshooting.

**Cleans up**
Shuts down all Docker containers to leave a clean environment.
