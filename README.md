## Setup

* Pythin and pip need to be installed. Both were done within Windows with the Python .exe installer downloaded from their site.

python -V
pip -V
 
python -m pip install Flask

$env:FLASK_APP = "hello.py"

python -m flask run
python -m flask run --port 9080
