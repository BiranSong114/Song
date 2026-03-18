# 英超赛程查询 Agent

这是一个演示级别的 Python Agent，用于查询英超（Premier League）当日/隔日比赛和积分榜。

## 快速开始

1. 准备依赖

```bash
pip install requests
```

2. 设置环境变量（需要在 https://www.football-data.org/ 注册一个 token）

```bash
export FOOTBALL_DATA_TOKEN=your_token_here
```

3. 执行

```bash
python epl_agent/app.py
```

4. 示例交互

- 英超今天比赛
- 英超积分表
- 英超明天比赛

## 代码结构

- `soccer_api.py`：对 `football-data.org` 的 API 封装
- `nlp_bridge.py`：简单意图解析（可替换成 LLM）
- `agent.py`：业务调度
- `app.py`：控制台交互入口

## 扩展建议

- 支持按球队查询（如“阿森纳英超赛程”）
- 支持指定日期查询
- 支持爬取实时直播事件（红黄牌、换人等）
- 结合 `FastAPI` 提供 HTTP 服务
