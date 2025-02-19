## Django Authentication System with Docker

<p>This is a Django authentication system fully containerized using Docker. It provides user registration, login, logout, and authentication management using Django's built-in authentication system. The application is designed to be deployable and scalable with ease using PostgreSQL as the database.</p>


## Features
 * User Authentication (Register, Login, Logout)
 * Django Admin Panel
 * PostgreSQL Integration
 * Dockerized for Easy Deployment

 ## Tech Stack
   * Backend: Django
   * Database: PostgreSQL 14
   * Containerization: Docker & Docker Compose

## Getting started
<h1>Prerequisites</h1>
<h3>Ensure you have the following installed:</h3>

 * Python3
 * Django 
 * Docker
 * Docker compose

 ## Usage
 1. CLone the Repo
 `git clone https://github.com/alexander784/django_auth-with-docker.git` 
 2. Build and Run  the conatiners
 `docker-compose up --build -d`

 3. Apply migrations
 `docker-compose exec web python manage.py migrate`
 4. Access the App
 * Web App: http://127.0.0.1:8000

 ## Project Structure


`├── auth  `                    
`│   ├── settings.py    `       
`│   ├── urls.py     `          
`│   ├── wsgi.py      `         
`│   ├── asgi.py       `        
`├── ruhusa/           `
`│   ├── models.py      `       
`│   ├── views.py        `      
`│   ├── urls.py          `     
`├── templates/            `   
`├── docker-compose.yml     `   
`├── Dockerfile              `  
`├── requirements.txt         `
`├── manage.py                `

## Docker Configuration
  ## Dockerfile
`FROM python:3.10`</br>
`WORKDIR /code`</br>
`COPY requirements.txt .`</br>
`RUN pip install --no-cache-dir -r requirements.txt`</br>
`COPY . .`</br>
`CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]`</br>

## Docker-compose

`version: '3.10.12'`</br>
`services:`</br>
 ` web:`</br>
  `  build: .`</br>
   ` command: python manage.py runserver 0.0.0.0:8000`</br>
    `volumes:`</br>
     ` - .:/code`</br>
    `ports:`</br>
     ` - "8000:8000"`</br>
   ` depends_on:`</br>
     ` - db`</br>
 ` db:`</br>
   ` image: postgres:14`</br>
   ` environment:`</br>
      `- POSTGRES_HOST_AUTH_METHOD=trust`</br>
    `volumes:`</br>
    `  - postgres_data:/var/lib/postgresql/data/`</br>
`volumes:`</br>
  `postgres_data:`</br>


## Running the Docker cont

`sudo docker-compose up -d` -Start the containers. </br>
`sudo docker-compose down`- Stop and remove containers </br>
`docker-compose exec web python manage.py migrate` - Apply MIgrations </br>
`docker-compose logs -f` View container log </br>



## License
This project is licensed under the MIT License. See LICENSE for details.

## Author
## Alexander Nyaga.


          


 




