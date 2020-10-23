FROM python:3.7
RUN python -m pip install psutil
RUN python -m pip install Flask
RUN python -m pip install humanize
WORKDIR /usr/local/sbin
ADD hello.py hello.py
ENV FLASK_APP hello.py
# EXPOSE 8080
ENTRYPOINT [ "python hello.py" ] 
CMD [ "--port", "5000" ]
