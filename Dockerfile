# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (needed for Django, PostgreSQL, GDAL, etc.)
RUN apt-get update && apt-get install -y \
    libpq-dev \
    postgis \
    gdal-bin \
    libgdal-dev \
    libgeos-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for GDAL and GEOS
# ENV GDAL_VERSION=$(gdal-config --version) \
#     GEOS_VERSION=$(geos-config --version) \
#     CPLUS_INCLUDE_PATH=/usr/include/gdal \
#     C_INCLUDE_PATH=/usr/include/gdal

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 8000
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
