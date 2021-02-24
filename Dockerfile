FROM python:3.9.1

ADD src /src

CMD [ "python", "-m","unittest", "/tests/CalculatorTests.py" ]