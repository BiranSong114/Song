from agent import agent_handle


def main():
    print("英超查询 Agent 已启动 (输入 q/quit/exit 退出)")
    while True:
        q = input("你：").strip()
        if q.lower() in ("q", "quit", "exit"):
            print("退出。再见！")
            break
        answer = agent_handle(q)
        print("Agent：\n" + answer + "\n")


if __name__ == "__main__":
    main()
