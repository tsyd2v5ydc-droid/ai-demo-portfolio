# 智谱大模型网页生成工具
> Python + Streamlit + 智谱GLM API AI网页生成Demo
> 线上体验：【https://ai-demo-portfolio-pbqg3fhwtuhzyeu6vumbas.streamlit.app/】

## 项目介绍
业务侧AI应用Demo，基于Streamlit搭建交互界面，接入智谱GLM大模型API。用户通过自然语言描述需求，自动生成带完整CSS的HTML页面，支持实时预览、多轮对话迭代修改页面。适合快速制作简历、活动落地页等静态网页。

## 核心功能
- 自然语言生成HTML代码，自带样式，网页实时预览
- 对话上下文保存，持续迭代调整页面
- 接口异常捕获，提升程序稳定性

## 技术栈
Python、Streamlit、智谱GLM API、OpenAI兼容SDK

## 技术要点
- API密钥使用Streamlit Secrets管理，不硬编码，保障安全
- Prompt工程约束模型输出规范HTML
- chat_history维护对话上下文
- try异常捕获处理接口报错

## 本地运行
1.安装依赖包
bash
pip install streamlit openai
2.配置大模型 API 密钥：在 Streamlit Secrets 填入智谱 API Key
3.启动项目
bash
streamlit run zhipu_test.py
4.在页面输入网页需求，即可生成 HTML 并实时预览

## 项目亮点
1.业务落地视角：不需要前端基础，业务人员通过自然语言快速产出静态页面，降低页面制作成本，可拓展到报表页面、表单页面等更多业务场景
2.可扩展性强：可新增下拉切换模型，兼容 DeepSeek 等多家大模型 API，一键切换不同模型生成效果
3.完整产品链路：从用户输入、大模型调用、结果返回、代码渲染预览，全流程闭环，适合 AI 业务应用岗作品集
