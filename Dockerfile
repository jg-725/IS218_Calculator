FROM python:3.9.1

ADD . .

RUN pip install -r requirements

CMD [ "python", "-m", "unittest", "discover", "-s", "tests" ]