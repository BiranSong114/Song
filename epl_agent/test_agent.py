import os
import pytest
from datetime import date

from agent import query_today_epl, query_tomorrow_epl, query_table_epl

@pytest.mark.skipif(not os.getenv("FOOTBALL_DATA_TOKEN"), reason="Missing FOOTBALL_DATA_TOKEN")
def test_query_functions_exist():
    # 只要不抛异常即通过（依赖真实 API）
    _ = query_today_epl()
    _ = query_tomorrow_epl()
    _ = query_table_epl()
