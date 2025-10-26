FROM python:3.11-slim

WORKDIR /usr/src/app

COPY app ./app
COPY seed_db.py ./seed_db.py

RUN pip install --no-cache-dir -r app/requirements.txt

RUN python seed_db.py

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]