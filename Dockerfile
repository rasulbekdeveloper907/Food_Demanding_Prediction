FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
    build-essential gcc curl git libgomp1 libblas-dev liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip setuptools wheel

# Oldin og'ir dependencies
RUN pip install numpy==1.26.4 pandas==2.0.3 scikit-learn==1.3.2 joblib==1.3.2
RUN pip install numba==0.58.1 shap==0.61.0

# Qolgan dependencies
RUN pip install --no-cache-dir -r requirements.txt --no-deps

COPY demo/ demo/
COPY Models/ Models/

RUN useradd -m appuser
USER appuser

EXPOSE 7860

CMD ["python", "demo/app.py"]
