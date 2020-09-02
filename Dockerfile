FROM python
RUN python -m pip install psutil
RUN python -m pip install Flask
WORKDIR /usr/local/sbin
ADD hello.py hello.py
ENV FLASK_APP hello.py
EXPOSE 8080
ENTRYPOINT [ "python" ] 
CMD [ "hello.py" ]
