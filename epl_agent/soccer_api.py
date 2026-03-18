import os
import requests
from datetime import date

BASE_URL = "https://api.football-data.org/v4"
FOOTBALL_DATA_TOKEN = os.getenv("FOOTBALL_DATA_TOKEN", "")
HEADERS = {"X-Auth-Token": FOOTBALL_DATA_TOKEN}


def fetch_matches_for_date(target_date: str):
    """Return raw API payload for Premier League matches on a given date."""
    if not FOOTBALL_DATA_TOKEN:
        raise RuntimeError("FOOTBALL_DATA_TOKEN is required (set as env var).")

    url = f"{BASE_URL}/matches?dateFrom={target_date}&dateTo={target_date}&competition=PL"
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()


def fetch_standings():
    """Return raw Premier League standings payload."""
    if not FOOTBALL_DATA_TOKEN:
        raise RuntimeError("FOOTBALL_DATA_TOKEN is required (set as env var).")

    url = f"{BASE_URL}/competitions/PL/standings"
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()


def format_match_info(match: dict) -> str:
    home = match["homeTeam"]["name"]
    away = match["awayTeam"]["name"]
    status = match["status"]
    utc = match["utcDate"]
    score = match.get("score", {})
    full_time = score.get("fullTime", {})

    if status == "SCHEDULED":
        return f"{utc}  {home} vs {away} （未开赛）"
    if status == "FINISHED":
        return f"{utc}  {home} {full_time.get('home')} - {full_time.get('away')} {away}（已结束）"
    return f"{utc}  {home} vs {away} （{status}）"
