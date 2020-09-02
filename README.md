## Setup and Prerequisites

#### Python and pip need to be installed. For testing and development, both were done within Windows with the Python .exe installer downloaded from their site.

Basic commands to confirm pythin and pip are working properly
```
python -V
pip -V
```
### Running Locally

Once `python` and `pip` are confirmed to be installed and working, we will need to install 2 python modules `Flask` and `psutil`

```
python -m pip install Flask
python -m pip install psutil
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
