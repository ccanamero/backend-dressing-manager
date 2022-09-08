FROM python:3.10-slim

## Install dependencies
RUN pip install "poetry==1.1.4"
COPY poetry.lock pyproject.toml ./
RUN poetry export -o requirements.txt
RUN pip install -r requirements.txt

# Setup project
COPY ./dressings_manager_service /dressings_manager_service

# Run server
CMD ["uvicorn", "dressings_manager_service.entrypoint.app:app", "--host", "0.0.0.0", "--port", "8000"]
