FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir requests cryptography tzdata
COPY track_rewards.py .
COPY live ./live
CMD ["python", "live/monitor.py"]
