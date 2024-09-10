FROM python:latest

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the first directory
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Run Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

