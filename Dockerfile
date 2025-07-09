# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
# Removed netcat-traditional as it's no longer needed for wait-for-it.sh
RUN apt-get update && apt-get install -y libpq-dev gcc

# Copy requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/
# Removed chmod for wait-for-it.sh as we're not using it anymore

# Expose port 8000
EXPOSE 8000

# Default command to run the application
# The waiting and migration logic will be in docker-compose.yml
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]