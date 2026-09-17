from openai import OpenAI
import time

# 【配置区】
client = OpenAI(
    api_key="从.env读取密钥",
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)
MODEL_NAME = "glm-5.3-flash"
# 系统固定提示词：强制要求只输出纯净HTML，不带任何多余解释、代码块标记
SYSTEM_PROMPT = "你是网页前端工程师。只输出完整纯HTML代码，不要```html、```标记，不要任何文字解释、前言后语，直接返回完整网页代码。"

# 保存对话上下文，实现连续对话、迭代修改网页
chat_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("===== 智谱网页生成工具【升级版】 =====")
print("功能：支持迭代修改网页，每次生成自动新建带时间戳HTML，不会覆盖旧文件")
print("输入 exit 退出程序\n")

while True:
    try:
        user_input = input("你：")
        if user_input.lower() == "exit":
            print("对话结束")
            break

        # 用户消息加入对话历史
        chat_history.append({"role": "user", "content": user_input})

        # 请求模型
        res = client.chat.completions.create(
            model=MODEL_NAME,
            messages=chat_history
        )

        result = res.choices[0].message.content
        # AI回复存入上下文，下一轮可以继续修改
        chat_history.append({"role": "assistant", "content": result})

        print(f"\n智谱：已生成网页代码")

        # 按时间戳生成新文件，不会覆盖旧文件
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        filename = f"index_{timestamp}.html"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"✅ 文件保存成功：{filename}")
        print("👉 去浏览器打开这个文件预览\n")

    except Exception as e:
        print(f"\n❌ 出错了！错误信息：{e}")
        print("请检查网络、API余额，程序不会崩溃，可以继续提问\n")