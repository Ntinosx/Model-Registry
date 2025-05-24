 **Project Structure & Summary**

| File/Folder            | Description                                                                                                                                                                                                                          |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **main.py**            | FastAPI app with endpoints: POST /models: Upload model file + metadata (name, version, accuracy), GET /models: Return metadata of all uploaded models. GET /models/{name}: Return metadata of a specific model.                      |
| **models.py**          | SQLAlchemy ORM definitions for the `Model` metadata table.                                                                                                                                                                           |
| **crud.py**            | Database helper functions to create and retrieve model metadata.                                                                                                                                                                     |
| **database.py**        | PostgreSQL database connection setup and session management.                                                                                                                                                                         |
| **Dockerfile**         | Builds the FastAPI app container: Uses Python 3.11 slim image. Installs dependencies. Copies app files. Creates `models/` directory. Runs the app on port 8000 using uvicorn.                                                        |
| **docker-compose.yml** | Defines two services: **db**: PostgreSQL container with persistent volume and env setup. **api**: FastAPI container depending on db, exposing port 8000, sharing a local models folder.                                              |




**CI/CD Pipeline**


| Stage             | Description                                                                                                                                                                                                                                          |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Trigger**       | Runs on every push or pull request to the `main` branch.                                                                                                                                                                                             |
| **Build & Start** | Uses `docker-compose.yml` and the `Dockerfile` to spin up the PostgreSQL (`db`) and FastAPI (`api`) containers.                                                                                                                                      |
| **Test API**      | Runs Python scripts that create test_model1-2.pkl.Uploads the models using the `POST /models` endpoint. Sends GET requests to:Retrieve the uploaded model (`/models/{name}`) and (/models/).Verify that a non-existing model returns a 404.          |
| **Archive Logs**  | Collects Docker Compose logs from the test run.Uploads the logs as GitHub Action artifacts for later troubleshooting.                                                                                                                            |
| **Clean Up**      | Shuts down and removes all Docker containers to leave the environment clean after the run.                                                                                                                                                           |



**How to Build and Start Containers manually**

  docker-compose up --build
