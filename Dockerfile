# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy files
COPY main.py /app
COPY hotdog_app.py /app
COPY requirements.txt /app
COPY ms /app/ms

# Install dependencies
RUN pip install -r requirements.txt

# Run the application
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
