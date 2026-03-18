def parse_intent(user_query: str) -> dict:
    text = user_query.strip().lower()
    if "英超" in text and ("今天" in text or "今日" in text):
        return {"intent": "query_matches_today", "competition": "英超"}
    if "英超积分" in text or "积分表" in text:
        return {"intent": "query_table", "competition": "英超"}
    if "英超" in text and "比赛" in text and "明天" in text:
        return {"intent": "query_matches_tomorrow", "competition": "英超"}
    return {"intent": "unknown"}
