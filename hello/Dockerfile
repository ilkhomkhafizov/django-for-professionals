# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# Set work folder 
WORKDIR /dfp

# Install dependencies
COPY Pipfile Pipfile.lock /dfp/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /dfp/
