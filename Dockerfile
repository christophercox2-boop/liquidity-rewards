FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt tzdata
COPY track_rewards.py .
COPY live ./live
# the two race tables the map scores against, as a last-resort fallback:
# the monitor prefers the CDN, then the daily copy on main, then these
COPY data/silver_senate_races.csv data/silver_gov_races.csv ./data/
CMD ["python", "live/monitor.py"]
