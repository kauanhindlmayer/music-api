# Music API

**Description**: This is a simple Python/Flask application intended to provide a way to manage musics, genres, artists, labels, customers, and subscriptions.
The goal of these endpoints is to be simple, well-documented and to provide a base for developers to develop other applications off of.

## Installation

1. Run `docker-compose up` to build and configure the mysql database, make sure to be in the same directory as the docker files.
2. Run `python -m venv .venv` to create the virtual enviroment
3. Run the following commands to activate the virtual enviroment depending on which operating system and command shell you're using:
   - On Unix or MacOS, using the bash shell: `source .venv/bin/activate`
   - On Windows using PowerShell: `.venv\Scripts\Activate.ps1`
4. Run `pip install -r requirements.txt` to install dependencies
5. Run `python run.py` to initiate the API
6. Navigate to http://localhost:5000 in your browser

## How to test the software

1. Install the dependencies with `pip install -r requirements.txt`
2. Run the command `pytest`
3. If you delete the fixtures, or decide to add some of your own, you’ll have to re-generate them, and the way this is done is by running the app, getting an auth_token from the main page of the app. Paste that token in place of the test_auth_token at the top of the test_endpoints.py file, then run the tests.

The Postman collection with all the endpoints can be freely downloaded using the following button: [Run in Postman](https://api.postman.com/collections/23428387-411e9ac6-fb5e-4e5c-9ff9-eb5fa4141d40?access_key=PMAT-01H2RQS5P6JKTT1VSX2N6T7CHF)

## Open source licensing info

1. [LICENSE](LICENSE)
