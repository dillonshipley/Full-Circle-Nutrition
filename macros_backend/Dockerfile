# ==== CONFIGURE =====#
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /macros-backend

# COPY ./requirements.txt .
# COPY ./macros_backend/ .
# COPY ./recipes/ .
# COPY ./ingredients/ .
# COPY ./static/ .
# COPY manage.py .

COPY . .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

# ==== BUILD =======
RUN mkdir ./logs/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ==== RUN =======
EXPOSE 8000
CMD [ "python3.11", "manage.py", "runserver" ]