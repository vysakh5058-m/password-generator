# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app
# RUN apt-get update && apt-get install -y xclip
# RUN apt-get install xsel

# Copy the requirements file into the container at /app

COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container at /app
COPY password-generator.py  ./
COPY templates /app/templates/

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the Flask application
CMD ["python", "password-generator.py"]
