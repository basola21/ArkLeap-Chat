# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV IN_DOCKER true

# Install Poetry
RUN pip install poetry

# Set the working directory
WORKDIR /app

# Copy only the pyproject.toml and poetry.lock files to the container
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry config virtualenvs.create false && poetry install --no-dev

# Copy the rest of the application code to the container
COPY . /app/

