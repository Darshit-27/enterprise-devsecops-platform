FROM python:3.11-slim

# Create non-root user
RUN useradd -m appuser

WORKDIR /app

# Copy only required files
COPY app/ /app

# Install dependencies (pinned)
RUN pip install --no-cache-dir flask==2.2.5

# Switch to non-root user
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
