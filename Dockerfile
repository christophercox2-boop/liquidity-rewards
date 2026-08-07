FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt tzdata
COPY track_rewards.py .
COPY live ./live
CMD ["python", "live/monitor.py"]
