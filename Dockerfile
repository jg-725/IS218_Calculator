FROM python:3

ADD src /src

CMD [ "python", "tests/CalculatorTests.py"]