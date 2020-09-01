## Setup and Prerequisites

* Python and pip need to be installed. For testing and development, both were done within Windows with the Python .exe installer downloaded from their site.

```
python -V
pip -V
```

Once `python` and `pip` are confirmed to be installed and working, we will need to install the `python Flask` module.

```
python -m pip install Flask
```

```
$env:FLASK_APP = "hello.py"
export FLASK_APP=hello.py

python -m flask run
python -m flask run --port 9080
```

## The Docker part

```
docker build -t python/flask .
docker run -it --rm --name python_flask python/flask
```
