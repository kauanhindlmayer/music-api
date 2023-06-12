# Music API

**Description**: This is a simple Python/Flask application intended to provide a way to manage musics, genres, artists, labels, customers, and plans.
The goal of these endpoints is to be simple, well-documented and to provide a base for developers to develop other applications off of.

## Installation

1. Run `docker build -t docker-mysql .` to build a Docker image using the dockerfile in the current directory
2. Run `docker run -p 3306:3306 --name mysql-container -e MYSQL_ROOT_PASSWORD=1234 -d docker-mysql` to run a Docker container from the specified image
3. Run `docker exec -it mysql-container mysql -uroot -p1234` to lauch the MySQL client inside the container
4. Run `CREATE DATABASE music` to create a new database named `music`
5. Run `pip install requirements.txt` to install dependencies
6. Run python main.py
7. Navigate to http://localhost:5000 in your browser

## How to test the software

1. Install the dependencies with `pip install requirements.txt`
2. Run the command `pytest tests`
3. If you delete the fixtures, or decide to add some of your own, you’ll have to re-generate them, and the way this is done is by running the app, getting an auth_token from the main page of the app. Paste that token in place of the test_auth_token at the top of the test_endpoints.py file, then run the tests.

The Postman collection with all the endpoints can be freely downloaded using the following button: [Run in Postman](https://github.com/username/project/tests)

## Open source licensing info

1. [LICENSE](LICENSE)
