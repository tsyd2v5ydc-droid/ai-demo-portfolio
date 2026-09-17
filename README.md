# ai-demo-portfolio
# 智谱大模型网页生成工具
> Python + 智谱GLM API 实现的网页代码生成Demo

## 项目介绍
调用智谱GLM-5.3-Flash大模型，搭建支持多轮迭代对话的网页生成工具。
通过系统提示词限定模型只输出纯HTML代码；维护对话上下文，可以持续修改网页。生成文件附带时间戳，防止覆盖旧版本。

## 技术要点
- 大模型API调用，使用.env存放密钥，保障密钥安全
- Prompt工程，约束模型输出格式
- chat_history 保存对话上下文，实现连续对话
- try异常捕获，提升程序稳定性

## 使用
1. pip install openai
2. 配置.env填入智谱API Key
3. 运行脚本，输入网页需求，exit退出
