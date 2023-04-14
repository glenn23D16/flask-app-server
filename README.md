# Flask App Server

This project contains a simple Flask web application that runs on a DigitalOcean server. The application is configured to be automatically updated via GitHub Actions on each push to the `main` branch.

## Requirements

- Python 3.8+
- Flask
- DigitalOcean server

## Installation

1. Clone the repository:

```
git clone https://github.com/glenn23D16/flask-app-server.git
cd flask-app-server
```


2. Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate
```


3. Install the required dependencies:

```
pip install -r requirements.txt
```


## Running the Application Locally

1. Set the Flask app environment variable:

```
export FLASK_APP=app.py
```

2. Run the Flask application:

```
flask run
```


The application should now be running at `http://164.90.225.30`.

## Deployment

The application is automatically deployed to the DigitalOcean server using GitHub Actions whenever there's a push to the `main` branch. The deployment process is defined in the `.github/workflows/main.yml` file.
