# Stage 1wq1: Build and serve the static website using Nginx
FROM nginx:alpine AS website

# Set working directory and copy website files
WORKDIR /usr/share/nginx/html
COPY index.html .
COPY styles.css .
COPY script.js .

# Expose port 80 for Nginx
EXPOSE 80

# Stage 2: Set up the environment to run Selenium tests
FROM python:3.9-slim AS selenium-tests

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    chromium-driver \
    && apt-get clean

# Install Python dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Selenium test script
COPY testwebsite.py /app/

# Command to run Selenium tests
CMD ["python3", "testwebsite.py"]
