**Project Structure & Summary**                                                                                               

| File/Folder            | Description                                                                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **main.py**            | FastAPI app with endpoints: POST /models: Upload model file + metadata (name, version, accuracy), GET /models: Return metadata of all uploaded models. GET /models/{name}: Return metadata of a specific model.                      |
| **models.py**          | SQLAlchemy ORM definitions for the Model metadata table.                                                                                                                                                                           |
| **crud.py**            | Database helper functions to create and retrieve model metadata.                                                                                                                                                                     |
| **database.py**        | PostgreSQL database connection setup and session management.                                                                                                                                                                         |
| **Dockerfile**         | Builds the FastAPI app container: Uses Python 3.11 slim image. Installs dependencies. Copies app files. Creates models/ directory. Runs the app on port 8000 using uvicorn.                                                        |
| **docker-compose.yml** | Defines two services: **db**: PostgreSQL container with persistent volume and env setup. **api**: FastAPI container depending on db, exposing port 8000, sharing a local models folder.                                              |

---------

| Requirement         | Details                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| **Python**          | Python 3.11 (if running locally outside Docker)                                                   |
| **Docker**          | Docker installed and running                                                                      |
| **Docker Compose**  | Compose plugin                                                                                    |
| **Git**             | Git CLI installed (to clone the repository)                                                       |
| **cURL (optional)** | To test the API from the command line, you can use curl. Alternatively, use Postman or browser.   |

-------------------
**How to run Locally**

| Step                     | Command                                                                                  |
| ------------------------ | ---------------------------------------------------------------------------------------- |
| Clone the repository     | git clone https://github.com/Ntinosx/Model-Registry.git cd Model-Registry                |
| Build and start services | docker-compose up --build -d                                                             |
| Access API docs          | Open browser at (http://localhost:8000/docs)                                             |  
| Stop services            | docker-compose down                                                                      |

-----------

API USAGE 

| Action             | Command Example                                                                                                                  |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Upload a model     | curl -X POST "http://localhost:8000/models" -F "name=test_model" -F "version=1.0" -F "accuracy=0.95" -F "file=@test_model.pkl"   |
| List all models    | curl http://localhost:8000/models                                                                                                |
| Get model by name  | curl http://localhost:8000/models/test_model                                                                                     |
| Non-existing model | curl http://localhost:8000/models/nonexistent_model (returns 404)                                                                |

**Example Local Test Workflow**

| Step                                  | Command                                                                                                                          |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Create test model file                | python3 model_registry/test_model_creation_script.py                                                                             |
| Upload test model to API              | curl -X POST "http://localhost:8000/models" -F "name=test_model1" -F "version=1.0" -F "accuracy=0.9" -F "file=@test_model.pkl"   |
| Check uploaded model                  | curl http://localhost:8000/models/test_model1                                                                                    |
| Check non-existing model (expect 404) | curl http://localhost:8000/models/nonexistent_model                                                                              |

---------------------------

**CI/CD Pipeline**

| Stage             | Description                                                                                                                                                                                                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Trigger**       | Runs on every push or pull request to the main branch.                                                                                                                                                                                               |
| **Build & Start** | Uses docker-compose.yml and the Dockerfile to spin up the PostgreSQL (db) and FastAPI (api) containers.                                                                                                                                              |
| **Test API**      | Runs Python scripts that create test_model1-2.pkl.Uploads the models using the POST /models endpoint. Sends GET requests to:Retrieve the uploaded model (/models/{name}) and (/models/).Verify that a non-existing model returns a 404.              |
| **Archive Logs**  | Collects Docker Compose logs from the test run.Uploads the logs as GitHub Action artifacts for later troubleshooting.                                                                                                                                |
| **Clean Up**      | Shuts down and removes all Docker containers to leave the environment clean after the run.                                                                                                                                                           |

