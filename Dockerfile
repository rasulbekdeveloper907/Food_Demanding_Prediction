FROM python:3.12-slim

# =====================
# Environment
# =====================
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# =====================
# System dependencies
# =====================
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    git \
    curl \
    libgomp1 \
    libblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# =====================
# Workdir
# =====================
WORKDIR /app

# =====================
# Python tooling
# =====================
RUN python -m pip install --upgrade pip setuptools wheel

# =====================
# Requirements
# =====================
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# =====================
# Project files
# =====================
COPY demo/ demo/
COPY Models/ Models/

# =====================
# Non-root user
# =====================
RUN useradd -m appuser
USER appuser

# =====================
# Runtime
# =====================
EXPOSE 7860

CMD ["python", "demo/app.py"]
