#!/bin/bash

# Install uv if not present
pip install uv

# Install dependencies using uv
uv sync

# Start FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000
