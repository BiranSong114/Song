from datetime import date, timedelta
from soccer_api import fetch_matches_for_date, fetch_standings, format_match_info
from nlp_bridge import parse_intent


def query_today_epl() -> str:
    today = date.today().isoformat()
    payload = fetch_matches_for_date(today)
    matches = payload.get("matches", [])
    if not matches:
        return f"{today} 英超今天没有安排比赛。"
    lines = [format_match_info(m) for m in matches]
    return f"{today} 英超比赛：\n" + "\n".join(lines)


def query_tomorrow_epl() -> str:
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    payload = fetch_matches_for_date(tomorrow)
    matches = payload.get("matches", [])
    if not matches:
        return f"{tomorrow} 英超明天没有安排比赛。"
    lines = [format_match_info(m) for m in matches]
    return f"{tomorrow} 英超比赛：\n" + "\n".join(lines)


def query_table_epl() -> str:
    payload = fetch_standings()
    standings = payload.get("standings", [])
    if not standings:
        return "无法获取英超积分榜。"

    table_type = next((x for x in standings if x.get("type") == "TOTAL"), None)
    if not table_type:
        return "未能在结果中找到总积分榜。"

    rows = table_type.get("table", [])
    lines = ["排名  球队  胜 平 负 进球 失球 积分"]
    for row in rows[:10]:
        team = row.get("team", {}).get("name", "未知")
        lines.append(
            f"{row.get('position', '?')}  {team}  {row.get('won', 0)} {row.get('draw', 0)} {row.get('lost', 0)} "
            f"{row.get('goalsFor', 0)} {row.get('goalsAgainst', 0)} {row.get('points', 0)}"
        )

    return "英超积分榜（前10）：\n" + "\n".join(lines)


def agent_handle(user_query: str) -> str:
    intent_data = parse_intent(user_query)
    intent = intent_data.get("intent")

    if intent == "query_matches_today":
        return query_today_epl()
    if intent == "query_matches_tomorrow":
        return query_tomorrow_epl()
    if intent == "query_table":
        return query_table_epl()

    return "抱歉，我还不能理解您的问题，请尝试“英超今天比赛”“英超积分表”等描述。"
