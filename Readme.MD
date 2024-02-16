# Todo List Full Stack Project

This is a full-stack Todo List project that allows users to manage their todo items. The project is divided into dedicated backend and frontend. The project utilizes Django Rest Framework for the backend, PostgreSQL as the database, and ReactJS for the frontend. The entire application environment is containerized using Docker.

### Installation

To install and run the project, follow these steps:

1. Make sure you have Docker and Docker Compose installed and running on your system. For instructions on how to install Docker, please refer to the [official Docker installation documentation](https://docs.docker.com/engine/install/).

2. Clone the project repository.

3. Navigate to the `frontend` folder and create a `.env` file with the following values:
```
REACT_APP_API_HOST=http://localhost:8001
REACT_APP_ENVIRONMENT=development
```
4. Navigate back to the root directory of the project.

5. Run the command `docker-compose up`. This will start the project and run three containers: one for the backend Python server, one for the frontend React application, and one for the PostgreSQL database.

6. Access the backend API from Postman or any other client at `http://localhost:8001`, and the frontend application from the browser at `http://localhost:3000`.

### Tests and coverage
The backend project is 97% covered by test cases. To run the testcases, 
- Ensure the all containers are up and running.
- Go to the backend container by issuing this command from the project root directory `docker-compose exec -it backend sh`
- Now run the command `python manage.py test`

To see the test coverage report, run the tests with coverage and see the report. Do the following steps,
- Ensure the all containers are up and running.
- Go to the backend container by issuing this command from the project root directory `docker-compose exec -it backend sh`
- Now run the command `coverage run manage.py test`
- Now run the command `coverage report`

### Creating Admin User

To create the first admin user:

1. Ensure all containers are running.
2. Open a new terminal tab and navigate to the root directory of the project.
3. Enter the command `docker-compose exec -it backend sh` to access the backend container.
4. Inside the container, run `python manage.py createsuperuser` and follow the prompts to create the admin user.

### Django Admin Panel

The Django Admin Panel can be accessed at `/admin`. Log in with the admin user credentials to manage users and create additional users, it can be regular user or admin user.

## Backend APIS:
The backend APIs include JWT authentication. Here are the available endpoints:

### Authentication and User APIs

- `/auth/register` (POST): Register a new account and returns the JWT Access and Refresh Tokens. Provide Email, Username and Password in the payload. 
- `/auth/login` (POST): Login with user credentials and returns the JWT Access and Refresh Tokens. Provide Username and Password in the payload.

Sample Response for both Register and Login Endpoints is,
```
{
    "user": {
        "username": "shamsul2",
        "email": "shamsul2@gmail.com",
        "superuser_status": false
    },
    "token": {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODE1Mzg5NSwiaWF0IjoxNzA4MDY3NDk1LCJqdGkiOiI3M2QwZjk3YTdmNDE0OGE4OWIwMTM1MWFhNjlhZmIwMCIsInVzZXJfaWQiOjZ9.KmjQ8DddNi8WlhAj6_vF_6wmIIr4Q3ukxa5nUYr5lJo",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA4MDcxMDk1LCJpYXQiOjE3MDgwNjc0OTUsImp0aSI6IjhiNGQ4NjA0M2Q2ZjQ0NzRhODc4YWE4YzZjYmZkMWEwIiwidXNlcl9pZCI6Nn0.H-ayL4QRxT0-ExJm6FrSpsVBHU2L2dwhGTeSGZMsE8E"
    }
}
```
- `/token/refresh` (POST): Refresh the JWT token.
Provide Refresh Token in the payload.
- `/auth/users` (GET): Get a list of users (open to admin user only).
- `/auth/users/username` (DELETE): Delete a user (open to admin user only).



### Todo APIs

All Todo APIs are open to authenticated users only:

- `/todos` (GET, POST): Create and get a list of todos for the authenticated user. Provide a Todo Title and Description in the payload.

    POST method sample response,
```
{
    "id": 8,
    "title": "first todo",
    "description": "first description",
    "done": false,
    "created_at": "2024-02-16T07:13:05.878240Z",
    "updated_at": "2024-02-16T07:13:05.878253Z"
}
```

GET method sample response
```
[
    {
        "id": 8,
        "title": "first todo",
        "description": "first description",
        "done": false,
        "created_at": "2024-02-16T07:13:05.878240Z",
        "updated_at": "2024-02-16T07:13:05.878253Z"
    }
]
```


- `/todos/id` (GET, PUT, DELETE): Get, update, or delete a specific todo item.

### Features

- User signup and login functionality. Frontend uses local storage in the browser to access the logged in user and determines if a user is signed in.
- Regular users can perform standard CRUD operations on their todo items.
- Admin users have additional privileges to delete users through the frotnend, once an admin user logs in, they will see *Manage Users* Menu on the navigation bar. This is not visible when a regular user logs in.
- Additionally, Admin users can visit the Django Admin and create additional admin or regular users.
