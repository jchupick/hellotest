## Introduction

This repository was created specifically to solve the problem presented at https://github.com/marufaytekin/hello-world

The chosen language for this solution was `python`, along with the `Flask` module installed on top of python. `Flask` is a popular framework to create quick web-based API endpoints from an application running in `python`.

## Setup and Prerequisites

### Running Locally
Python and pip need to be installed. For testing and development, both were done within Windows with the Python .exe installer downloaded from their site.

Basic commands to confirm Python and pip are working properly
```
python -V
pip -V
```
### Running within the Docker Framework
The only pre-requsite for this is that the user has Docker installed locally and can connect and download from Docker's hub.
The base Docker image used for this is simplay named `python`

## Run the Application
The application can be run by simply cloning this repository and running the commands listed below. I have provided the how-to to run this both locally and within the `Docker`  framework. Both methods will result in an identical running application. The `Docker` method presents more advantages as most of the application is contained in the Docker image built from the steps below (the very point of Docker). Running the application locally requires the reader to execute a few prerequisite steps, which may need to be different depending on platform.
### Running Locally

Once `python` and `pip` are confirmed to be installed and working, we will need to install 2 python modules `Flask` and `psutil`

```
python -m pip install Flask
python -m pip install psutil
python -m pip install humanize
```

#### Set the Flask application environment variable
##### Windows Powershell
```
$env:FLASK_APP = "hello.py"
```
##### Linux
```
export FLASK_APP=hello.py
```

#### And run the application
```
python -m flask run --port 8080
```

### Running within Docker

```
docker build -t python/flask .
docker run -it --rm -p 8080:8080 --name python_flask python/flask
```

## Test the Application

### Valid endopints
- http://localhost:8080/
- http://localhost:8080/healthz
- http://localhost:8080/healthz-full
- http://localhost:8080/version
- http://localhost:8080/mem
- http://localhost:8080/disk
- http://localhost:8080/help

## Description
Additional information to present within the API was chosen as this information would be useful to someone in an operations group to view given a running application.
The most straightforward and common information would be to present both disk and memory information from the API itself. The module `psutil` was selected to accomplish this.

## CI/CD

This section addresses the question raised in Step 5 of the excersize outlined at https://github.com/marufaytekin/hello-world

### Branching Strategy
There are several what are considered 'standard' branching startegies used and reccommended by Git/GitHub. For this, the 'trunk-based' strategy could easily be used.
  * All Production builds will come from the `master` branch.
  * Bug fixes and enhancements could be done from individual branches from `master`, and referenced or named after the work ticket number (eg. JIRA) that decribes that bug/enhancement. Test environments could be built from this branch, with the code then merged to `master` and deployed to production as desired.
### CI/CD Tools/Services
As I have extensive experience with it, I would choose Jenkins as my CI/CD orchestration tool for build/deploy. It is an industry standard proven to be simple, reliable and extensible.
### CI/CD Stages (Run by Jenkins)
#### Git checkout
Pull desired code (based on branch) from source repository (GitHub, GitLab, BitBucket)
#### Static Code Analysis
Analyze the code at the plain text level. This can catch errors in best practices including potential errors, possible leaks, and some security flaws.
#### Build (If Applicable)
Complie/Link the code base as needed. Interpreted languages do not require this.
#### Package an 'Artifact'
Create and store an immutable build artifact that can be deployed reliably to any environment.
This step could also be a Docker packaging operation.
#### Deploy to Test Environment
Deploy the above artifact to a non-Prod environment
#### Runtime/Security/Penetration Code Analysis
Using industry tools (various available) perform tests against a running environment. These can be code path tests, security, penetraion, and reliability tests given sets of input data.
#### Deploy to Production
Final step to occur conditionally if all of the above steps pass without error.

In a true CI/CD environment, the above could potentially occur by a commit trigger, meaning that an application could be reliably deployed many times throughout the day.

Note that there are multiple tools available to perform the above steps which I have not specifically enumerated.

