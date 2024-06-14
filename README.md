# Chat Application API Documentation

## Overview

This API provides endpoints for managing chat rooms and messages. It allows users to create, update, read, and search within chat rooms and messages. The API is built using Django Rest Framework and PostgreSQL, and it is containerized using Docker.

## Table of Contents

1. [API Endpoints](#api-endpoints)
2. [Setup and Running the API](#setup-and-running-the-api)
3. [Testing the API](#testing-the-api)

# API Endpoints

## Chat Rooms

- **Create Chat Room**

  - **URL:** `/api/chatrooms/`
  - **Method:** `POST`
  - **Description:** Create a new chat room.
  - **Request Body:**
    ```json
    {
      "name": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "number": "integer",
      "name": "string",
      "created_at": "datetime"
    }
    ```

- **Update Chat Room**

  - **URL:** `/api/chatrooms/{number}/`
  - **Method:** `PUT`
  - **Description:** Update details of an existing chat room.
  - **Request Body:**
    ```json
    {
      "name": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "number": "integer",
      "name": "string",
      "created_at": "datetime"
    }
    ```

- **Read Chat Room**
  - **URL:** `/api/chatrooms/{number}/`
  - **Method:** `GET`
  - **Description:** Retrieve details of a specific chat room.
  - **Response:**
    ```json
    {
      "number": "integer",
      "name": "string",
      "created_at": "datetime"
    }
    ```

## Messages

- **Create Message**

  - **URL:** `/api/messages/`
  - **Method:** `POST`
  - **Description:** Create a new message within a chat room.
  - **Request Body:**
    ```json
    {
      "chat_room": "integer",
      "content": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "number": "integer",
      "chat_room": "integer",
      "content": "string",
      "created_at": "datetime"
    }
    ```

- **Update Message**

  - **URL:** `/api/messages/{number}/`
  - **Method:** `PUT`
  - **Description:** Update content of an existing message.
  - **Request Body:**
    ```json
    {
      "content": "string"
    }
    ```
  - **Response:**
    ```json
    {
      "number": "integer",
      "chat_room": "integer",
      "content": "string",
      "created_at": "datetime"
    }
    ```

- **Read Message**

  - **URL:** `/api/messages/{number}/`
  - **Method:** `GET`
  - **Description:** Retrieve details of a specific message within a chat room.
  - **Response:**
    ```json
    {
      "number": "integer",
      "chat_room": "integer",
      "content": "string",
      "created_at": "datetime"
    }
    ```

- **Search Messages**
  - **URL:** `/api/messages/{chat_room_id}/search?q=query`
  - **Method:** `GET`
  - **Description:** Search messages within a specific chat room by partial match of the message content.
  - **Response:**
    ```json
    [
      {
        "number": "integer",
        "chat_room": "integer",
        "content": "string",
        "created_at": "datetime"
      }
    ]
    ```

## Setup and Running the API

### Prerequisites

- Docker
- Docker Compose
- Poetry

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/basola21/ArkLeap-Chat.git
   cd chatapp
   ```

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory and add the following:

   ```env
   IN_DOCKER=True
   POSTGRES_DB=chatapp
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=postgres
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   ```

3. **Install Dependencies:**

   ```bash
   poetry install

   ```

4. **Run the Application with Docker:**

   ```bash
   docker-compose up

   ```

5. **Access the API Documentation:**
   - Defualt UI: [http://localhost:8000/api/](http://localhost:8000/api/)

## Testing the API

### Running Tests

Run the tests using Django's test framework:

```bash
poetry run python manage.py test

```
