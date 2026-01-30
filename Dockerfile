# ============================
# Base image (Python 3.10, slim)
# ============================
FROM python:3.10-slim

# ============================
# Environment variables
# ============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ============================
# System dependencies
# ============================
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# ============================
# Working directory
# ============================
WORKDIR /app

# ============================
# Copy requirements first (for caching)
# ============================
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# ============================
# Copy project files
# ============================
COPY demo/ demo/
COPY Models/ Models/

# ============================
# Security: create non-root user
# ============================
RUN useradd -m appuser
USER appuser

# ============================
# Expose Gradio port
# ============================
EXPOSE 7860

# ============================
# Run the Gradio app
# ============================
CMD ["python", "demo/app.py"]
