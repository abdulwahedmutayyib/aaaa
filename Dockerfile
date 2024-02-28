# Use a base image with Python, OpenCV, and Pillow installed
FROM python:3.8-slim

# Install additional dependencies
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY requirements.txt .
COPY video_player.py .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port used by the application (if applicable)
# EXPOSE 8080

# Run the video player application
CMD ["python", "video_player.py"]

