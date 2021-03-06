FROM python:3

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY api.py ./
COPY test.py ./

EXPOSE 8000
