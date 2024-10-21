# Step 1: Use a base image with Python
FROM python:3.9-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install the dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the Python script into the container
COPY s3chunked.py .

# Step 7: Define the command to run the script
CMD ["python", "s3chunked.py"]
