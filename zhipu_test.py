# 只本地VSCode运行时启用下面3行，部署streamlit请注释掉这三行
# import subprocess
# import sys
# subprocess.check_call([sys.executable, "-m", "pip", "install", "openai"])

from openai import OpenAI
import streamlit as st
import json

#【配置区】
client = OpenAI(
    api_key=st.secrets["ZHIPU_API_KEY"],
    base_url="https://openai.bigmodel.cn/api/paas/v4/"
)
MODEL_NAME = "glm-5.3-flash"
# 系统设定提示词
SYSTEM_PROMPT = "你是网页前端工程师。只输出完整纯HTML代码，不要```html```标记，不要任何文字解释、前言后语，直接返回完整网页代码。"

# 初始化对话历史，存入streamlit会话缓存
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# 网页UI标题
st.title("智谱网页生成工具")
st.caption("输入需求，AI直接生成完整HTML网页代码")

# 渲染历史对话
for msg in st.session_state.chat_history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# 网页输入框
user_input = st.chat_input("在这里输入网页需求，例如：写一个简洁个人简历网页")

if user_input:
    # 用户消息存入对话
    st.session_state.chat_history.append({"role":"user", "content":user_input})
    st.chat_message("user").write(user_input)
    try:
        # 请求智谱模型
        res = client.chat.completions.create(
            model=MODEL_NAME,
            messages=st.session_state.chat_history
        )
        # 安全读取返回结果
        st.write(type(res))
        st.write(res)
        result = res.choices[0].message.content
        # AI回复存入对话
        st.session_state.chat_history.append({"role":"assistant", "content":result})
        st.chat_message("assistant").write(result)
    except Exception as e:
        st.error(f"调用失败：{str(e)}")
