# Use the official Python 3.11 image as the base image
FROM python:3.11

# Set the working directory in the Docker container
WORKDIR /home/apps/ztm_scrappers/

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y -q python3-dev default-libmysqlclient-dev build-essential

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade pip
RUN pip install --upgrade pip

# Copy the contents of your local directory to the Docker image
COPY . /home/apps/ztm_scrappers/

# Install Python packages from requirements.txt
RUN pip install -r requirements.txt

# Make sure the start.sh script is executable
RUN chmod +x start.sh

# Specify the entry point command to run your application
CMD ["./start.sh"]
