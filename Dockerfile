# Base image
FROM python:3.9-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add mariadb-dev \
    && apk add --no-cache mariadb-connector-c-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk add --no-cache --virtual .build-deps \
        build-base \
        linux-headers \
        gcc \
        libc-dev \
        python3-dev \
        libffi-dev \
        openssl-dev \
        libxml2-dev \
        libxslt-dev \
    && apk add --no-cache --virtual .runtime-deps \
        mariadb-connector-c \
        libffi-dev \
        libxslt \
        libpq \
        libxml2 \
        openssl \
    && pip install --upgrade pip
    

RUN pip install mysqlclient  


# Set working directory
WORKDIR /code

# Copy requirements file
COPY requirements.txt /code/

RUN python -m venv env
RUN source env/bin/activate

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/

# Set the entrypoint script
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
