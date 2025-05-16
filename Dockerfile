#Use python:3.9-slim as the base image.
FROM python:3.9-slim

WORKDIR /app

#Install dependencies listed in requirements.txt.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the image.
COPY app.py .

#Expose port 5000.
EXPOSE 5000

#Set the command to run the Flask application.
CMD ["python", "app.py"]