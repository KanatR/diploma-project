# 1. Start with a lightweight Python base image
FROM python:3.9-slim

# 2. Set the folder inside the container where we will work
WORKDIR /code

# 3. Copy requirements and install them
# We copy this first to use Docker's cache speed
COPY ./app/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 4. Copy the rest of the application code
COPY ./app /code/app

# 5. Command to run the app when the container starts
# host 0.0.0.0 is required for Docker containers
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]