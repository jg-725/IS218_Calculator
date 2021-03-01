FROM python:3.7

ADD . .

RUN pip install -r requirements

CMD [ "python", "-m", "unittest", "discover", "-s", "Tests" ]