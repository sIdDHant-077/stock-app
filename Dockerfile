# Use the official Python image from Docker Hub
FROM python:3.9-slim
# Set the working directory in the container
WORKDIR /app
# Copy the local project files to the working directory
COPY . /app
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Expose the port the app runs on
EXPOSE 5000
# Ensure the Flask app runs on 0.0.0.0 (accessible from outside the container)
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Command to run the Flask app
CMD ["python", "StockAPI.py"]