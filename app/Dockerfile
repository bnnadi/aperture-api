FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code
COPY . .


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make the wait-for-db.sh script executable
RUN chmod +x /app/wait-for-db.sh

# Expose port 5000 to the outside world
EXPOSE 5001

# Run Flask app
CMD [ "flask", "run", "--host=0.0.0.0"]

