# Use official Python image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the FastAPI app with Uvicorn (using app.py)
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]