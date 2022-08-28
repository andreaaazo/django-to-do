FROM python

# Stop creating py cache
ENV PYTHONDONTWRITEBYCODE 1

ENV PYTHONUNBUFFERED 1

# Working directory
WORKDIR /django-to-do

# Copy pipenv
COPY Pipfile Pipfile.lock /django-to-do/

# Run pip
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /django-to-do/
