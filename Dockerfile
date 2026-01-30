# ============================
# Base image (Python 3.11 slim)
# ============================
FROM python:3.11-slim

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
    libgomp1 \
    libblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# ============================
# Working directory
# ============================
WORKDIR /app

# ============================
# Copy requirements first (for caching)
# ============================
COPY requirements.txt .

# ============================
# Upgrade pip, setuptools, wheel
# ============================
RUN python -m pip install --upgrade pip setuptools wheel

# ============================
# Install heavy dependencies separately
# ============================
RUN pip install numpy==1.26.4 pandas==2.0.3 scikit-learn==1.3.2 joblib==1.3.2
RUN pip install numba==0.58.1 shap==0.63.0

# ============================
# Install remaining requirements
# ============================
RUN pip install --no-cache-dir -r requirements.txt --no-deps

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
