# Crowd Source Main API 
A social media application inspired by reddit.

Users create "Projects", which acts as a dashboard for conversations regarding a particular project. Posts can be made within that project regarding different features/aspects of that particular project

## Build
- ### 1. Setup python environment
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

- ### 2. Run the project
    ```bash
    # If developing, add --reload for live reloading
    uvicorn main:get_app
    ```