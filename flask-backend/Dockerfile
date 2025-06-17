# Use the official Python image
FROM python:3-alpine

# Set working directory
WORKDIR /flask

# Copy requirements to working directory and install libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app folder to working directory
COPY . ./app

# Set envirornment variables for Flask app
ENV FLASK_APP=./app/flask_app.py

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=8071"]
