# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional but good practice)
EXPOSE 8080

# Run the bot
CMD ["python3", "bot.py"]
