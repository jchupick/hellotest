FROM python
RUN python -m pip install Flask
ADD hello.py /hello.py
ENV FLASK_APP hello.py
EXPOSE 5000
CMD python -m flask run
