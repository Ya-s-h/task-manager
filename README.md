# Task Manager API

A Unix-inspired task management service that mimics core process operations like `ls` and `fork` through RESTful APIs.

## 🚀 Overview
This project is a backend service that manages "tasks" in a Unix-like fashion. It allows clients to

-**List all tasks** – analogous to `ls`
-**Create new tasks** – analogous to `fork`

## 🧩 Features

 - Create, read, update, and delete tasks.
 - Mark tasks as completed.
 - List all tasks with their statuses.

## 🛠️ Tech Stack

- **Language*: Python
- **Framework*: Flask
- **Database*: MongoDB

## 📦 Installation
1. **Clone the repositoy**

   ```bash
   git clone https://github.com/Ya-s-h/task-manager.git
   cd task-manager
   ```

2. **Set up a virtual environment (optional but recommende)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencis**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Server**
    ```bash
    uvicorn main:app --reload
    ```
    

## 📚 API Documentation
### List All asks

- **Endpoint**: `GET /tasks`
- **Description**: Retrieves a list of all tasks.
- **Response**:

  
```json
  [
    {
      "id": 1,
      "name": "Sample Task",
      "status": "running",
      "created_at": "2025-04-22T19:32:26"
    },
    ...
  ]
 ```

### Create a New Task

- **Endpoint**: `POST /tasks`
- **Description**: Creates a new task.
- **Request Body**:

  
```json
  {
    "name": "New Task"
  }
 ```


- **Response**:

  
```json
  {
    "id": 2,
    "name": "New Task",
    "status": "pending",
    "created_at": "2025-04-22T19:35:00"
  }
 ```

### Get Task Details

- **Endpoint**: `GET /tasks/{task_id}`
- **Description**: Retrieves details of a specific ask.
- **Response**:

  
```json
  {
    "id": 2,
    "name": "New Task",
    "status": "pending",
    "created_at": "2025-04-22T19:35:00"
  }
 ```

### Delete a Task

- **Endpoint**: `DELETE /tasks/{task_id}`
- **Description**: Deletes a specific task.
- **Response**:

  
```json
  {
    "message": "Task deleted successfully."
  }
 ```

### Update Task Status
- **Endpoint**: `PUT /tasks/{task_id}/status`
- **Description**: Updates a specific task status.
- **Request Body**:

  
```json
  {
    "status": "success"
  }
 ```

- **Response**:

  
```json
  {
    "id": 2,
    "name": "New Task",
    "status": "success",
    "created_at": "2025-04-22T19:35:00",
    "updated_at": "2025-04-22T19:40:00"
  }
 ```
### Reset a Task

- **Endpoint**: `POST /tasks/{task_id}/reset`
- **Description**: Reset a specific task's status.
- **Response**:

  
```json
  {
    "id": 2,
    "name": "New Task",
    "status": "pending",
    "created_at": "2025-04-22T19:35:00",
    "updated_at": "2025-04-22T19:45:00"
  }
 ```
## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📝 Notes

- Ensure that **MongoDB** is running locally before starting the application.
- The valid task statuses are:

  ```
  ['pending', 'running', 'success', 'failure']
  ```

- Allowed status transitions:
  - `pending` ➝ can transition to `running`
  - `running` ➝ can transition to `success` or `failure`
  - `success` ➝ no further transitions allowed
  - `failure` ➝ no further transitions allowed

---

For more details on the challenge, refer to the original article by Ankit Gupta: [Take-Home Challenge: Build a Unix-Inspired Task Manager API (Tech Agnostic)](https://www.linkedin.com/pulse/take-home-challenge-build-unix-inspired-task-manager-api-ankit-guptajym4c/) 
