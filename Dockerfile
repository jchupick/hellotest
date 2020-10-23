FROM python:3.7
RUN python -m pip install psutil
RUN python -m pip install Flask
RUN python -m pip install humanize
WORKDIR /usr/local/sbin
ADD hello.py hello.py
ENV FLASK_APP hello.py
EXPOSE 5000
ENTRYPOINT [ "python", "-m", "flask", "run" ] 
#CMD [ "--port", "5001" ]
