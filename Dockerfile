FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt tzdata
COPY track_rewards.py scan_markets.py launcher.py ./
# scan_markets.py was missing from the image the whole 1.0 era — monitor.py
# imports it inside a silent try/except, so golf discovery quietly never ran
# in production. It ships now.
COPY live ./live
COPY v2 ./v2
# the two race tables the map scores against, as a last-resort fallback:
# the monitor prefers the CDN, then the daily copy on main, then these
COPY data/silver_senate_races.csv data/silver_gov_races.csv ./data/
# one container, both versions: 1.0 keeps the public port and forwards
# /v2/* to the read-only 2.0 process (see launcher.py and v2/DESIGN.md)
CMD ["python", "launcher.py"]
