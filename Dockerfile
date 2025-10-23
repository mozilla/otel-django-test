# ---- base python image ----
FROM python:3.13-slim

# set work directory
WORKDIR /app

# install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy django project code
COPY . .

# set environment variables
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=todolist_project.settings

# run migrations & start django server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
