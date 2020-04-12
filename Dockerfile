FROM python:3.7

# prevent __pycache__ folders from appearing everywhere 
ENV PYTHONDONTWRITEBYTECODE=True

WORKDIR /web
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "manage.py", "run"]