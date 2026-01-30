# ============================
# Base image (ML safe)
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
    && rm -rf /var/lib/apt/lists/*

# ============================
# Working directory
# ============================
WORKDIR /app

# ============================
# Copy requirements first (Docker layer caching)
# ============================
COPY requirements.txt .

# Upgrade pip, setuptools, wheel first
RUN pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# ============================
# Copy project files
# ============================
COPY demo/ demo/
COPY Models/ Models/

# ============================
# Security: non-root user
# ============================
RUN useradd -m appuser
USER appuser

# ============================
# Gradio port
# ============================
EXPOSE 7860

# ============================
# Run Gradio app
# ============================
CMD ["python", "demo/app.py"]
