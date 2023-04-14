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

## Assignment Report

**Components of the Solution**

*GitHub Actions*: GitHub Actions is a continuous integration and continuous deployment (CI/CD) platform that automates tasks like code testing, building, and deployment. In this solution, it was used to deploy the Flask app to the Digital Ocean server. The workflow was triggered each time a push was made to the repository's main branch.

*Bash*: Bash is a Unix shell scripting language used to execute commands and automate tasks. In this solution, Bash was used within the GitHub Actions workflow to manage SSH keys, transfer files, and restart the Flask app server on the remote Digital Ocean server.

*Digital Ocean*: Digital Ocean is a cloud service provider offering virtual servers called droplets. In this assignment, a droplet was used to host the Flask app server. The Flask app server was set up using a systemd service to run automatically and securely on the server.

**Problems Encountered and Solutions**

*Changing the default Flask port*: By default, Flask runs on port 5000, but this assignment required port 80. The FLASK_RUN_PORT environment variable was set to 80, and the systemd service file was updated to ensure the Flask app ran on the correct port.

*SSH key management*: To securely access the Digital Ocean server and deploy the Flask app, private SSH keys were used. Initially, there were issues with creating and using the SSH key within the GitHub Actions workflow. The problem was solved by creating a private key within the workflow and ensuring proper permissions were set.

*File paths and environment variables*: There were issues with file paths and environment variables in the systemd service file, causing the Flask app server to fail to start. To fix this, the working directory and environment variables were correctly set in the service file, ensuring the Flask app server started successfully.

**Optional Notes**

During the process of solving this assignment, I learned the importance of carefully setting up and managing the CI/CD pipeline. Additionally, I gained valuable experience in configuring a Flask app server to run in a production environment using a cloud service provider like Digital Ocean.