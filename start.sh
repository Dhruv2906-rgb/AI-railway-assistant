#!/bin/bash
set -e

echo "Starting FastAPI..."

uvicorn backend.main:app \
    --host 0.0.0.0 \
    --port 8000 &

echo "Waiting for FastAPI..."
sleep 3

echo "Starting Streamlit..."

streamlit run frontend/app.py \
    --server.address 0.0.0.0 \
    --server.port ${PORT:-8501}